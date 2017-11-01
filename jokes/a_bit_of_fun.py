"""First play with dictionaries in Python - a knock knock joke generator"""

import random

x = 1

while x == 1:

    def joke1():
        knock = raw_input("Knock Knock...\n")
        res = ["y","who's there","who's there?","whos there?","whos there","whose there","whose there?"]
        x = 2
        while x > 0:
            if knock.lower() not in res:
                print "C'mon, quit jokin' around"
                x -= 1
                knock = raw_input("Knock Knock...\n")
            else:
                break

    joke1()

    def joke2():
       punch =  {1:["Europe","Europe who?","No, you're a poo!"],
                2:["To","To who?","I think you'll find it's 'to whom'..."],
                3:["Biggish","Biggish who?","Not today, thanks."],
                4:["Cows go","Cows go who?","Actually, cow's go 'moo'."],
                5:["Etch","Etch who?","Bless you!"]}
       n = random.randint(1,len(punch))
       x = 2
       print punch[n][0]
       who = raw_input("")
       while x > 0:
           if who.lower() != punch[n][1].lower() and who.lower() != punch[n][1].lower()[:len(punch[n][1])-1]:
               print "Err, try again"
               who = raw_input("")
               x -= 1
           else:
               print punch[n][2],"\n"
               break
       else:
           print "Keyboard training or finger diet required, however, it's:",punch[n][2],"\n"


    joke2()