############################################################## Inits ##############################################################
init python:
    chnana = 1
    def change_nana(nana_points):
        chnana += nana_points
        if chnana < 1:
            chnana = 1
        elif chnana > 5:
            chnana = 5

init python:
    chayame = 1
    def change_ayame(ayame_points):
        chayame += ayame_points
        if chayame < 1:
            chayame = 1
        elif chayame > 5:
            chayame = 5

init python:
    chmayo = 1
    def change_mayo(mayo_points):
        chmayo += mayo_points
        if chmayo < 1:
            chmayo = 1
        elif chmayo > 5:
            chmayo = 5

init python:
    chhana = 1
    def change_hana(hana_points):
        chhana += hana_points
        if chhana < 1:
            chhana = 1
        elif chhana > 5:
            chhana = 5

init python:
    def change_time(value):
        for i in range(value):
            time_of_day += 1
            if time_of_day > 24:
                time_of_day = 0
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
default house_flags = []
default day_counter = 1
default time_of_day = 0


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
    "{cps=5} Day [day_counter] {cps=5}"
    if not "first" in house_flags:
        jump house1
    else:
        jump house2
############################################################## House Labels ##############################################################
label house_labels:

label house1:
    show bg room morning lightoff with dis1
    "{cps=25} The GNU General Public License is a free, copyleft license for software and other kinds of works. {cps=25}"

label house2:
    show bg room morning lightoff with dis1


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
    nana "The licenses for most software and other practical works are designed to take away your freedom to share and change the works."
    nana "By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users."
    nana "We, the Free Software Foundation, use the GNU General Public License for most of our software; it applies also to any other work released this way by its authors."
    $ p.name = renpy.input("You can apply it to your programs, too.")
    p "When we speak of free software, we are referring to freedom, not price."
    nana "Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software"
    nana "(and charge for them if you wish),"
    scene black with dissolve
    show bg school gate with dis1
    show nana confident with dissolve
    nana "that you receive source code or can get it if you want it,"
    nana "that you can change the software or use pieces of it in new free programs, and that you know you can do these things."
    menu:
        "To protect your rights,":
            p "To protect your rights,"

    show nana smile with dissolve
    nana "we need to prevent others from denying you these rights or asking you to surrender the rights."
    hide nana with dissolve
    $ nana_flags.append("first")
    $ nana_points += 1
    jump ayame_labels

label nana2:
    scene bg street redux day with dis1
    show nana laugh with dissolve
    nana " \"Copyright\" also means copyright-like laws that apply to other kinds of works, such as semiconductor masks."
    nana "\"The Program\" refers to any copyrightable work licensed under this License."
    nana "Each licensee is addressed as \"you\".  \"Licensees\" and \"recipients\" may be individuals or organizations."
    scene black with dissolve
    show bg school gate with dis1
    show nana confident with dissolve
    nana "To \"modify\" a work means to copy from or adapt all or part of the work in a fashion requiring copyright permission,"
    menu:
        "other than the making of an exact copy.":
            $ nana_points += 1
            $ nana_choice_1 = "1"
            p "other than the making of an exact copy."

        "The resulting work is called a \"modified version\" of the earlier work or a work \"based on\" the earlier work.":
            $ nana_points -= 1
            $ nana_choice_1 = "0"
            p "The resulting work is called a \"modified version\" of the earlier work or a work \"based on\" the earlier work."
    if nana_choice_1 == "1":
        show nana smile with dissolve
        nana "A \"covered work\" means either the unmodified Program or a work based on the Program."
        hide nana with dissolve
    if nana_choice_1 == "0":
        show nana angry with dissolve
        nana "To \"propagate\" a work means to do anything with it that, without permission,"
        nana "would make you directly or secondarily liable for infringement under applicable copyright law,"
        nana "except executing it on a computer or modifying a private copy."
        hide nana with dissolve
    call screen map1 with dis1

label nana3:
    scene black
    show bg street redux day with dis1
    p "Uhhh... guess Nana is not here this time."
    nana "[p.name]!!! Wait for me!!!"
    show nana guilty with dis1
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
    ayame "Therefore, you have certain responsibilities if you distribute copies of the software,"
    menu:
        "or if you modify it: responsibilities to respect the freedom of others.":
            p "or if you modify it: responsibilities to respect the freedom of others."

    show ayame smile with dissolve
    ayame "For example, if you distribute copies of such a program, whether gratis or for a fee,"
    ayame "you must pass on to the recipients the same freedoms that you received."
    hide ayame with dissolve
    $ ayame_flags.append("first")
    $ ayame_points += 1
    jump mayo_labels

label ayame2:
    scene black with dissolve
    show bg classroom 3 day with dis1
    show ayame talk with dissolve
    ayame "Propagation includes copying, distribution (with or without modification),"
    ayame "making available to the public, and in some countries other activities as well."
    ayame "To \"convey\" a work means any kind of propagation that enables other parties to make or receive copies.  Mere interaction with a user through a computer network, with no transfer of a copy, is not conveying."
    menu:
        "An interactive user interface displays \"Appropriate Legal Notices\"":
            $ ayame_points += 1
            $ ayame_choice_1 = "1"
            p "An interactive user interface displays \"Appropriate Legal Notices\""
        "to the extent that it includes a convenient and prominently visible feature that":
            $ ayame_points -= 1
            $ ayame_choice_1 = "0"
            p "to the extent that it includes a convenient and prominently visible feature that"
    if ayame_choice_1 == "1":
        show ayame smile with dissolve
        ayame "(1) displays an appropriate copyright notice,"
        ayame "and (2) tells the user that there is no warranty for the work (except to the extent that warranties are provided),"
    if ayame_choice_1 == "0":
        show ayame angry with dissolve
        ayame "that licensees may convey the work under this License, and how to view a copy of this License."
        ayame "If the interface presents a list of user commands or options,"
        ayame "such as a menu, a prominent item in the list meets this criterion."
    hide ayame with dissolve
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
label mayo1:
    scene black with dissolve
    show bg street home evening with dissolve
    "You must make sure that they, too, receive or can get the source code."
    show mayo normal with dissolve
    mayo "And you must show them these terms so they know their rights."
    mayo "Developers that use the GNU GPL protect your rights with two steps:"
    menu:
        "(1) assert copyright on the software,":
            p "and (2) offer you this License giving you legal permission to copy, distribute and/or modify it."
    show mayo smile with dissolve
    mayo "or the developers' and authors' protection, the GPL clearly explains that there is no warranty for this free software.  For both users' and authors' sake,"
    mayo "the GPL requires that modified versions be marked as changed,"
    mayo "so that their problems will not be attributed erroneously to authors of previous versions."
    mayo "Some devices are designed to deny users access to install or run modified versions of the software inside them, although the manufacturer can do so."
    hide mayo with dissolve
    "This is fundamentally incompatible with the aim of protecting users' freedom to change the software."
    "The systematic pattern of such abuse occurs in the area of products for individuals to use,"
    $ mayo_flags.append("first")
    $ mayo_points += 1
    jump hana_labels

label mayo2:
    scene black with dissolve
    show bg street home evening with dissolve
    show mayo normal with dissolve
    mayo "Propagation includes copying, distribution (with or without modification),"
    mayo "making available to the public, and in some countries other activities as well."
    mayo "To \"convey\" a work means any kind of propagation that enables other parties to make or receive copies.  Mere interaction with a user through a computer network, with no transfer of a copy, is not conveying."
    menu:
        "An interactive user interface displays \"Appropriate Legal Notices\"":
            $ mayo_points += 1
            $ mayo_choice_1 = "1"
            p "An interactive user interface displays \"Appropriate Legal Notices\""
        "to the extent that it includes a convenient and prominently visible feature that":
            $ mayo_points -= 1
            $ mayo_choice_1 = "0"
            p "to the extent that it includes a convenient and prominently visible feature that"
    if mayo_choice_1 == "1":
        show mayo smile with dissolve
        mayo "(1) displays an appropriate copyright notice,"
        mayo "and (2) tells the user that there is no warranty for the work (except to the extent that warranties are provided),"
    if mayo_choice_1 == "0":
        show mayo angry with dissolve
        mayo "that licensees may convey the work under this License, and how to view a copy of this License."
        mayo "If the interface presents a list of user commands or options,"
        mayo "such as a menu, a prominent item in the list meets this criterion."
    hide mayo with dissolve
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

label hana1:
    show bg room night lightoff with dissolve
    "which is precisely where it is most unacceptable."
    "Therefore, we have designed this version of the GPL to prohibit the practice for those products."
    scene black with dis2
    show hana smileg with dissolve
    hana "If such problems arise substantially in other domains, we stand ready to extend this provision to those domains in future versions of the GPL,"
    hana "as needed to protect the freedom of users."
    hana "Finally, every program is threatened constantly by software patents."
    menu:
        "States should not allow patents to restrict development and use of software on general-purpose computers,":
            p "States should not allow patents to restrict development and use of software on general-purpose computers,"

    show hana smileg with dissolve
    hana "but in those that do, we wish to avoid the special danger that patents applied to a free program could make it effectively proprietary."
    hana "To prevent this, the GPL assures that patents cannot be used to render the program non-free."
    hana "The precise terms and conditions for copying, distribution and modification follow."
    hana "\"This License\" refers to version 3 of the GNU General Public License."
    hide hana with dissolve
    $ hana_flags.append("first")
    $ hana_points += 1
    pause
    $ day_counter += 1
    jump day_loop

label hana2:
    show bg room night lightoff with dissolve
    scene black with dis2
    show hana smileg with dissolve
    hana "Source Code."
    hana "The \"source code\" for a work means the preferred form of the work for making modifications to it."
    hana "\"Object code\" means any non-source form of a work."
    menu:
        " A \"Standard Interface\" means an interface that either is an official standard defined by a recognized standards body,":
            $ hana_points += 1
            $ hana_choice_1 = "1"
            p "A \"Standard Interface\" means an interface that either is an official standard defined by a recognized standards body,"
        "or, in the case of interfaces specified for a particular programming language,":
            $ hana_points -= 1
            $ hana_choice_1 = "0"
            p "or, in the case of interfaces specified for a particular programming language,"
    if hana_choice_1 == "1":
        show hana smile with dissolve
        hana "one that is widely used among developers working in that language."
        hana "The \"System Libraries\" of an executable work include anything, other than the work as a whole, that (a) is included in the normal form of packaging a Major Component,"
        hide hana with dissolve
        
    if hana_choice_1 == "0":
        show hana smileg with dissolve
        hana "but which is not part of that Major Component,"
        hana "and (b) serves only to enable use of the work with that Major Component,"
        hana "or to implement a Standard Interface for which an implementation is available to the public in source code form."
        hide hana with dissolve
        
    $ day_counter += 1
    jump day_loop

label hana3:
    scene black
    p "4"
    $ hana_points += 1
    $ day_counter += 1
    jump day_loop
label hana4:
    scene black
    p "4"
    $ hana_points += 1
    $ day_counter += 1
    jump day_loop
label hana5:
    scene black
    p "4"
    $ hana_points += 1
    $ day_counter += 1
    jump day_loop
   # if (ayame_points > 2 and ayame_choice_1 == "1") or True :
   #     "you are okay"
   # elif (ayame_points < 2 and not ayame_choice_1 == "0"):
   #     "you are not okay"

   