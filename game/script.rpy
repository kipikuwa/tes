############################################################## Inits ##############################################################
init python:
    chnana = 1
    def change_nana(nana_points):
        chnana += nana_points
        if chnana < 1:
            chnana = 1
        elif chnana > 5:
            chnana = 5
############################################################## Characters ##############################################################

define nana = Character("Nana", who_color="#cb8872", what_color="#FFF") 
define ayame = Character("Ayame", who_color="#746060", what_color="#FFF")
define mayo = Character("Mayonaise", who_color="#957372", what_color="#FFF")
define hana = Character("Hana", who_color="#d7cbc4", what_color="#FFF")
define p = Character("Unknown", who_color="#1f4eff", what_color="#FFF")

############################################################## Character Images ##############################################################

image nana amazed = "images/Nana/amazed.png"
image nana angry = "images/Nana/angry.png"
image nana flustered = "images/Nana/flustered.png"
image nana guilty = "images/Nana/guilty.png"
image nana happy = "images/Nana/happy.png"
image nana sad = "images/Nana/sad.png"
image nana smile = "images/Nana/smile.png"
image nana laugh = "images/Nana/laugh.png"
image nana confident = "images/Nana/confident.png"
image nana talk = "images/Nana/talk.png"

image ayame angry = "images/Ayame/angry.png"
image ayame embarrased = "images/Ayame/embarrased.png"
image ayame errkk = "images/Ayame/errkk.png"
image ayame happy = "images/Ayame/happy.png"
image ayame laugh = "images/Ayame/laugh.png"
image ayame lecture = "images/Ayame/lecture.png"
image ayame sad = "images/Ayame/sad.png"
image ayame smile = "images/Ayame/smile.png"
image ayame surprised = "images/Ayame/surprised.png"
image ayame talk = "images/Ayame/talk.png"

image mayo angry = "images/Mayonaise/angry.png"
image mayo awkward = "images/Mayonaise/awkward.png"
image mayo happy = "images/Mayonaise/happy.png"
image mayo emotalk = "images/Mayonaise/emotalk.png"
image mayo noemo = "images/Mayonaise/noemo.png"
image mayo normal = "images/Mayonaise/normal.png"
image mayo sad = "images/Mayonaise/sad.png"
image mayo smile = "images/Mayonaise/smile.png"
image mayo talk = "images/Mayonaise/talk.png"
image mayo wah = "images/Mayonaise/wah.png"

image hana amused = "images/Hana/noglasses/amused.png"
image hana angry = "images/Hana/noglasses/angry.png"
image hana awkward = "images/Hana/noglasses/awkward.png"
image hana concentrate = "images/Hana/noglasses/concentrate.png"
image hana dissapointed = "images/Hana/noglasses/dissapointed.png"
image hana impressed = "images/Hana/noglasses/impressed.png"
image hana noemo = "images/Hana/noglasses/noemo.png"
image hana serious = "images/Hana/noglasses/serious.png"
image hana smile = "images/Hana/noglasses/smile.png"
image hana talk = "images/Hana/noglasses/talk.png"

image hana amusedg = "images/Hana/noglasses/amusedg.png"
image hana angryg = "images/Hana/noglasses/angryg.png"
image hana awkwardg = "images/Hana/noglasses/awkwardg.png"
image hana concentrateg = "images/Hana/noglasses/concentrateg.png"
image hana dissapointedg= "images/Hana/noglasses/dissapointedg.png"
image hana impressedg = "images/Hana/noglasses/impressedg.png"
image hana noemog = "images/Hana/noglasses/noemog.png"
image hana seriousg = "images/Hana/noglasses/seriousg.png"
image hana smileg = "images/Hana/noglasses/smileg.png"
image hana talkg = "images/Hana/noglasses/talkg.png"

############################################################## Backgrounds ##############################################################

image bg room morning lightoff = "images/001/room_morning_light_off.jpg"
image bg street redux day = "images/001/street_redux_day.jpg"
image bg school gate = "images/001/generic_school_gate.jpg"
image bg classroom 3 day = "images/001/classroom_03_day.jpg"
image bg room = "images/001/room_morning_light_off.jpg"
image bg street home evening = "images/001/street_home_evening.jpg"
image bg room night lightoff = "images/001/room_evening_light_off.jpg"

############################################################## Variables ##############################################################

default nana_points = 1
default nana_flags = []
default ayame_points = 1
default ayame_flags = []
default mayo_points = 1
default mayo_flags = []
default hana_points = 1
default hana_flags = []
default day_counter = 1
default time_of_day = 0
init python:
    def change_time(value):
        for i in range(value):
            time_of_day += 1
            if time_of_day > 24:
                time_of_day = 0

############################################################## Transitions ##############################################################

define dis1 = Dissolve(1.0)
define dis2 = Dissolve(2.0)

############################################################## Screens ##############################################################
screen map1():
    add "mapbg"
    style_prefix "map1"
    vbox:
        align .5,.5
        hbox:
            button:
                text "House"
                action Jump("hana_labels")#, function(change_time, 6)
            button:
                text "Street"
                action Jump("nana_labels")#, function(change_time, 6)
        hbox:
            button:
                text "School"
                action Jump("ayame_labels")#, function(change_time, 6)
            button:
                text "Jungle"
                action Jump("mayo_labels")#, function(change_time, 6)

style map1_button:
    xysize (268,268)
    idle_background "mapbt_idle"
    hover_background "mapbt_hover"
    hover_sound "audio/re2_coursor.wav"
    activate_sound "audio/re2_decide.wav"
style map1_text:
    align(.5,.5)

############################################################## Start Label ##############################################################
label start:
    jump day_loop

label day_loop:
    #play sound daydream
    
    scene black
    "Day [day_counter]"
    show bg room morning lightoff with dis1
    "I should hurry to school!"
    
############################################################## Nana's Labels ##############################################################
label nana_labels:
    scene black
    if not "first" in nana_flags:
        jump nana1
    elif nana_points == 2:
        jump nana2
    elif nana_points == 3:
        jump nana3
    elif nana_points == 4:
        jump nana4
    elif nana_points == 5:
        jump nana5

label nana1:
#    if 6 < time_of_day < 12:
#       $ change_time()
    show bg street redux day with dis1
    show nana laugh with dissolve
    nana "Hi!"
    nana "You must be in the same school as me{w=0.4}{nw}"
    nana "My name is Nana, What is your name?"
    $ p.name = renpy.input("What is your name?")
    p "My name is [p.name]"
    nana " Oh! [p.name], what a cool name!"
    nana "let's go to school together"
    scene black with dissolve
    show bg school gate with dis1
    show nana confident with dissolve
    nana "Yes! we have arrived at time!"
    nana "Have a good day, See ya!"
    menu:
        "Thank you, you have a good day too.":
            p "Thank you, you have a good day too."

    show nana smile with dissolve
    nana "Thanks, See ya later"
    hide nana with dissolve
    $ nana_flags.append("first")
    $ nana_points += 1
    call screen map1 with dis1

label nana2:
    scene bg street redux day with dis1
    show nana laugh with dissolve
    nana "Hey! [p.name] how are you today?"
    nana "Going to school?"
    nana "let's go together"
    scene black with dissolve
    show bg school gate with dis1
    show nana confident with dissolve
    nana "OK, i hope you have a good time today"
    menu:
        "Ummm... You too, i hope you a good score in your exams today.":
            $ nana_points += 1
            $ nana_choice_1 = "1"
            p "Ummm... You too, i hope you a good score in your exams today."

        "Whatever!":
            $ nana_points -= 1
            $ nana_choice_1 = "0"
            p "Whatever!"
    if nana_choice_1 == "1":
        show nana smile with dissolve
        nana "Thanks, See ya later"
        hide nana with dissolve
    if nana_choice_1 == "0":
        show nana angry with dissolve
        nana "[p.name]! What's up with that?"
        nana "I didn't except that"
        nana "ugh!"
        hide nana with dissolve
        call screen map1 with dis1

label nana3:
    scene black
    p "3"
    $ nana_points += 1
    call screen map1 with dis1

label nana4:
    scene black
    p "4"
    $ nana_points += 1
    call screen map1 with dis1

label nana5:
    scene black
    p "5"
    $ nana_points += 1
    call screen map1 with dis1
            
############################################################## Ayame's Labels ##############################################################
label ayame_labels:
     scene black
    if not "first" in ayame_flags:
        jump ayame1
    elif ayame_points == 2:
        jump ayame2
    elif ayame_points == 3:
        jump ayame3
    elif ayame_points == 4:
        jump ayame4
    elif ayame_points == 5:
        jump ayame5

label ayame1:
    scene black with dissolve
    show bg classroom 3 day with dis1
    show ayame talk with dissolve
    ayame "Hello [p.name], you where a little late, where you have been?"
    menu:
        "I fall asleep":
            p "I fall asleep"

    show ayame smile with dissolve
    ayame "Aha!, make sure you don't miss classes."
    ayame "Bye for now."
    hide ayame with dissolve
    $ ayame_points += 1
    call screen map1 with dis1

label ayame2:
    scene black
    p "2"
    $ ayame_points += 1
    call screen map1 with dis1

label ayame3:
    scene black
    p "3"
    $ ayame_points += 1
    call screen map1 with dis1

label ayame4:
    scene black
    p "4"
    $ ayame_points += 1
    call screen map1 with dis1

label ayame5:
    scene black
    p "5"
    $ ayame_points += 1
    call screen map1 with dis1

############################################################## Mayo's Labels ##############################################################

label mayo_labels:
     scene black
    if not "first" in mayo_flags:
        jump mayo1
    elif mayo_points == 2:
        jump mayo2
    elif mayo_points == 3:
        jump mayo3
    elif mayo_points == 4:
        jump mayo4
    elif mayo_points == 5:
        jump mayo5

    scene black with dissolve
    show bg street home evening with dissolve
    "What's that sound?"
    show mayo normal with dissolve
    mayo "Oh! Hello [p.name]"
    mayo "How are you?"
    menu:
        "I'm good, Sorry but who are you?":
            p "I'm good, And who are you?"
    show mayo smile with dissolve
    mayo "Good to hear that."
    mayo "I'm Mayonaise the witch."
    mayo "You can find me in the Jungle"
    mayo "Sorry! gotta go, BYE!"
    hide mayo with dissolve
    "Oh, She just left!"
    "Anyway, i should go to home it's getting dark around here"
    $ mayo_points += 1
    call screen map1 with dis1

label mayo2:
    scene black
    p "4"
    $ mayo_points += 1
    call screen map1 with dis1

label mayo3:
    scene black
    p "4"
    $ mayo_points += 1
    call screen map1 with dis1

label mayo4:
    scene black
    p "4"
    $ mayo_points += 1
    call screen map1 with dis1

label mayo5:
    scene black
    p "4"
    $ mayo_points += 1
    call screen map1 with dis1

############################################################## Hana's Labels ##############################################################

label hana_labels:
     scene black
    if not "first" in hana_flags:
        jump hana1
    elif hana_points == 2:
        jump hana2
    elif hana_points == 3:
        jump hana3
    elif hana_points == 4:
        jump hana4
    elif hana_points == 5:
        jump hana5

    show bg room night lightoff with dissolve
    "ah... i'm so exhausted today"
    "i will just sleep right away"
    scene black with dis2
    show hana smileg with dissolve
    hana "Hello [p.name]!"
    hana "I'm Hana, the random wanderer in peoples dreams"
    hana "We can be friends if you want"
    menu:
        "OK, i like that":
            p "OK, i like that"

    show hana smileg with dissolve
    hana "Good to hear that."
    hana "Since it's your dream you can change things in it"
    hana "We will discuss that next time we saw each other"
    hana "You have to wake up, it's morning, bye for now"
    hide hana with dissolve
    $ hana_points += 1
    pause
    $ day_counter += 1
    jump day_loop

label hana2:
    scene black
    p "4"
    $ hana_points += 1
    call screen map1 with dis1

label hana3:
    scene black
    p "4"
    $ hana_points += 1
    call screen map1 with dis1

label hana4:
    scene black
    p "4"
    $ hana_points += 1
    call screen map1 with dis1

label hana5:
    scene black
    p "4"
    $ hana_points += 1
    call screen map1 with dis1

   # if (ayame_points > 2 and ayame_choice_1 == "1") or True :
   #     "you are okay"
   # elif (ayame_points < 2 and not ayame_choice_1 == "0"):
   #     "you are not okay"

   