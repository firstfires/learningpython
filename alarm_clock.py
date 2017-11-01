"""A program that acts as a sort of alarm clock. The user sets a time, and when the time is reached, a random Youtube
video is pulled from a list of links in a text file. This is a task that was set out in the following:
https://www.reddit.com/r/beginnerprojects/comments/4n9hne/project_idea_alarm_clock/"""

import webbrowser, datetime, time, random

#stores current time as variable
dt = datetime.datetime.now()

#turns time in to 4 digits
def time_int(x,y):
    return int("%s%s" %(x,y))

#takes user input of selected alarm time
alarm = int(raw_input("What time would you like to be awoken?"))
if alarm < 0000 or alarm > 2359:
    print "That ain't no time, yo..."
else:
    print "Your alarm is set for ",alarm

#checks current time every 5 seconds to see if it matches user selected time
alarm_check = True
while alarm_check == True:
    dt = datetime.datetime.now()
    tn = time_int(dt.hour, dt.minute)
    if alarm != tn:
        # insert a delay of 5 seconds between checks
        time.sleep(5)
        print tn
        alarm_check = True
    else:
        #once current time matches 'alarm' variable, the below is set off, pulling a random line/link from the songs.txt file
        sfile = open("songs.txt").read().splitlines()
        song = random.choice(sfile)
        # 0 = same browser window, 1 = new browser window, 2 =
        webbrowser.open(song, new=2, autoraise=True)
        break