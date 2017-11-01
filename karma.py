"""This was a task set to compare the most recent posts of two different users on the site Reddit, and return which
oof the users had the higher score. I wanted to use it as a practise of classes.
https://www.reddit.com/r/beginnerprojects/comments/1i951e/project_compare_recent_karma/"""

import json, urllib2, requests
from time import sleep

#class for pulling in post details and comparing scores
class Profile (object):

    def __init__(self,username):
        self.username = username
        self.profile_url = ""
        self.top_post_date = 0
        self.top_score = 0

    #this method checks whether or not the username is valid using the request status code
    def check_url(self):
        checker = False
        while checker == False:
            profile_url = "https://www.reddit.com/user/" + self.username + "/submitted.json"
            request = requests.get(profile_url)
            # 200 means the page opened successfully
            if request.status_code == 200:
                checker = True
                self.profile_url = "https://www.reddit.com/user/" + self.username + "/submitted.json"
            #status 429 means too many requests have been sent
            elif request.status_code == 429:
                checker = False
                sleep(2)
                print "Trying to connect.."
            #other returned responses mean the url failed and therefore the username is incorrect
            else:
                self.username = raw_input(self.username + " does not exist. Please try again: ")

    #Wthis method pulls post times/dates from users profile and puts them in to a list, then stores the largest
    def post_date_pull(self):
        response = urllib2.urlopen(self.profile_url)
        user_profile = json.loads(response.read())
        incrementer = 0
        com_list = []
        for i in user_profile['data']['children']:
            com_list.append(user_profile['data']['children'][incrementer]['data']['created_utc'])
            incrementer += 1
        self.top_post_date = max(com_list)

    #this method checks the newest date against the users posts and pulls the score from that post
    def pull_score(self):
        response = urllib2.urlopen(self.profile_url)
        user_profile = json.loads(response.read())
        incrementer = 0
        score = 0
        for i in user_profile['data']['children']:
            if user_profile['data']['children'][incrementer]['data']['created_utc'] == self.top_post_date:
                self.top_score = user_profile['data']['children'][incrementer]['data']['score']
            incrementer += 1
        return self.top_score


user1 = Profile(raw_input("Please enter your first user: "))
Profile.check_url(user1)
user2 = Profile(raw_input("...and now a second: "))
Profile.check_url(user2)
Profile.post_date_pull(user1)
Profile.post_date_pull(user2)
Profile.pull_score(user1)
Profile.pull_score(user2)

if user1.top_score > user2.top_score:
    print user1.username,"wins with", user1.top_score
else:
    print user2.username,"wins with", user2.top_score