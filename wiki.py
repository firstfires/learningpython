"""A short program utilising the Wikipedia API for generating random articles.
   The program returns a title to the user, and they can either choose to read it or skip.
   This was a set task taken from the below link:
   https://www.reddit.com/r/beginnerprojects/comments/1jg2ru/project_random_wikipedia_article/
   """
import urllib2,json,webbrowser

print "Welcome to the random Wikipedia article generator."
print "Enter = Next article | Y = Open article | X = Exit\n"

#Enclose in While True loop so the user is continually presented with articles until they choose to exit
while True:
    #pulling in the JSON data and creating the specific article variables from the nested data
    url = "https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json"
    response = urllib2.urlopen(url)
    random_page = json.load(response)
    article = random_page['query']['random'][0]
    art_title = article['title']
    art_link = "http://en.wikipedia.org/wiki?curid="+str(article['id'])

    #present user with question as to whether they want to read article or not
    question = raw_input("Would you like to read about "+art_title+"?")

    #if user selects y - link opens, x - program exits, any other key (i.e. Enter) will present them with another article
    if question.lower() == "y":
        webbrowser.open(art_link, new=2, autoraise=True)
    elif question.lower() == "x":
        break