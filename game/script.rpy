# Characters
define nana = Character("Nana", who_color="#cb8872", what_color="#FFF") 
define ayame = Character("Ayame", who_color="#746060", what_color="#FFF")
define mayo = Character("Mayonaise", who_color="#957372", what_color="#FFF")
define hana = Character("Hana", who_color="#d7cbc4", what_color="#FFF")
define p = Character("Unknown", who_color="#1f4eff", what_color="#FFF")

# Variables
default nana_points = 0
default ayame_points = 0
default mayo_points = 0
default hana_points = 0

# Character Images
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

# Backgrounds
image bg day 1 = "images/other/day1.jpg"
image bg room morning lightoff = "images/001/room_morning_light_off.jpg"
image bg street redux day = "images/001/street_redux_day.jpg"
image bg school gate = "images/001/generic_school_gate.jpg"
image bg classroom 3 day = "images/001/classroom_03_day.jpg"
image bg room = "images/001/room_morning_light_off.jpg"
image bg street home evening = "images/001/street_home_evening.jpg"
image bg room night lightoff = "images/001/room_evening_light_off.jpg"

# Transitions
define dis1 = Dissolve(1.0)
define dis2 = Dissolve(2.0)
label start:
    jump day_loop

label day_loop:
   # play sound daydream
    scene black
    show bg day 1 with dissolve
    "Day 1"
    show bg room morning lightoff with dis1
    pause
    "I should hurry to school!"
    scene black
    show bg street redux day with dis1
    show nana laugh with dissolve
    nana "Hi!"
    nana "You must be in the same school as me{w=0.4}{nw}"
    nana "My name is Brandy, What is your name?"
    $ p.name = renpy.input("What is your name?")
    p "My name is [p.name]"
    nana " Oh! [p.name], what a cool name!"
    nana "let's go to school together"
    scene black with dissolve
    show bg school gate with dis1
    show nana confident with dissolve
    nana "Yes! we have arrived at time!"
    nana "Have a good day, See ya!"
    scene black with dissolve
    show bg classroom 3 day with dis1
    show ayame talk with dissolve
    ayame "Hello [p.name], you where a little late, where you have been?"
    menu:
        "I fall asleep":
            $ ayame_points += 1
            $ ayame_choice_1 = "1"
            p "I fall asleep"

        "That's non of your business":
            $ ayame_points -= 1
            $ ayame_choice_1 = "0"
            p "That's non of your business"
    if ayame_choice_1 == "1":
        show ayame smile with dissolve
        ayame "Aha!, make sure you don't miss classes."
        ayame "Bye for now."
        hide ayame with dissolve
    if ayame_choice_1 == "0":
        show ayame angry with dissolve
        ayame "[p.name]! That's rude!"
        ayame "ah! What's the matter with you today?"
        ayame "i can't believe you said that to me!"
        hide ayame with dissolve
    pause
    scene black with dissolve
    show bg street home evening with dissolve
    "What's that sound?"
    show mayo normal with dissolve
    mayo "Oh! Hello [p.name]"
    mayo "How are you?"
    menu:
        "Who are you?":
            $ mayo_points += 1
            $ mayo_choice_1 = "1"
            p "Who are you?"

        "I'm good, Sorry but who are you?":
            $ mayo_points -= 1
            $ mayo_choice_1 = "0"
            p "I'm good, And who are you?"
    if mayo_choice_1 == "1":
        show mayo angry with dissolve
        mayo "You don't know me?"
        mayo "I'm Mayonaise! the witch!"
        mayo "You can find me in the Jungle"
        mayo "Sorry! gotta go, BYE!"
        hide mayo with dissolve
    if mayo_choice_1 == "0":
        show mayo smile with dissolve
        mayo "Good to hear that."
        mayo "I'm Mayonaise the witch."
        mayo "You can find me in the Jungle"
        mayo "Sorry! gotta go, BYE!"
        hide mayo with dissolve
    "Oh, She just left!"
    "Anyway, i should go to home it's getting dark around here"
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
            $ hana_points += 1
            $ hana_choice_1 = "1"
            p "OK, i like that"

        "Oh, that's a weird job":
            $ hana_points -= 1
            $ hana_choice_1 = "0"
            p "Oh, that's a weird job"
    if hana_choice_1 == "0":
        show hana angryg with dissolve
        hana "You really are a tough one ha?"
        hana "Anyway, you may see me in your dreams from times to times"
        hana "You have to wake up"
        hana "Bye for now"
        hide hana with dissolve
    if hana_choice_1 == "1":
        show hana smileg with dissolve
        hana "Good to hear that."
        hana "Since it's your dream you can change things in it"
        hana "We will discuss that next time we saw each other"
        hana "You have to wake up, it's morning, bye for now"
        hide hana with dissolve
    pause
   # if (ayame_points > 2 and ayame_choice_1 == "1") or True :
   #     "you are okay"
   # elif (ayame_points < 2 and not ayame_choice_1 == "0"):
   #     "you are not okay"

    
    return
