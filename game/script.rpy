# things to do:
# empty label for each location
# time passing system for home
# change the time after each encounter
# +1 and -1 icon for menus
# each label should have 2 bgs
# splash screen
# ending screen
# ending label for each character
# with glasses and no glasses labels for hanas
# use text tags
# change font
# change style and colors
# change start meuu
# sound effects
# special heart icon for 5 point selection
# go to sleep button on bed
# today flag for each character and remove it at the end of the day
#

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
image bg room dawn lightoff = "images/001/room_dawn_light_off.jpg"
image bg room dawn lighton = "images/001/room_dawn_light_on.jpg"
image bg room evening lightoff = "images/001/room_evening_light_on.jpg"
image bg room night lightoff = "images/001/room_night_light_off.jpg"

image bg street redux day = "images/001/street_redux_day.jpg"
image bg street redux evening = "images/001/street_redux_evening.jpg"
image bg street redux night = "images/001/street_redux_night.jpg"
image bg street home evening = "images/001/street_redux_evening.jpg"
image bg school gate = "images/001/generic_school_gate.jpg"

image bg classroom 3 day = "images/001/classroom_03_day.jpg"
image bg classroom 3 evening = "images/001/classroom_03_evening.jpg"
image bg classroom 3 night = "images/001/classroom_03_night.jpg"
image bg classroom 4 day = "images/001/classroom_04_day.jpg"
image bg classroom 4 evening = "images/001/classroom_04_evening.jpg"
image bg classroom 4 night = "images/001/classroom_04_night.jpg"

image bg jungle earlymorning = "images/001/philippines_003_early_morning.jpg"
image bg jungle morning = "images/001/philippines_003_morning.jpg"
image bg jungle day = "images/001/philippines_003_day.jpg"
image bg jungle afternoon = "images/001/philippines_003_afternoon.jpg"
image bg jungle night = "images/001/philippines_003_night.jpg"




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
                action NullAction()#, function(change_time, 6)
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

screen map2():
    add "mapbg"
    style_prefix "map2"
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
                action NullAction()#, function(change_time, 6)
            button:
                text "Jungle"
                action Jump("mayo_labels")#, function(change_time, 6)

style map2_button:
    xysize (268,268)
    idle_background "mapbt_idle"
    hover_background "mapbt_hover"
    hover_sound "audio/re2_coursor.wav"
    activate_sound "audio/re2_decide.wav"
style map2_text:
    align(.5,.5)

screen map3():
    add "mapbg"
    style_prefix "map3"
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
                action NullAction()#, function(change_time, 6)

style map3_button:
    xysize (268,268)
    idle_background "mapbt_idle"
    hover_background "mapbt_hover"
    hover_sound "audio/re2_coursor.wav"
    activate_sound "audio/re2_decide.wav"
style map3_text:
    align(.5,.5)

screen map4():
    add "mapbg"
    style_prefix "map4"
    vbox:
        align .5,.5
        hbox:
            button:
                text "House"
                action NullAction()#, function(change_time, 6)
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

style map4_button:
    xysize (268,268)
    idle_background "mapbt_idle"
    hover_background "mapbt_hover"
    hover_sound "audio/re2_coursor.wav"
    activate_sound "audio/re2_decide.wav"
style map4_text:
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
    "A \"Major Component\", in this context, means a major essential component (kernel, window system, and so on) of the specific operating system (if any) on which the executable work runs,"
    nana "or a compiler used to produce the work, or an object code interpreter used to run it."
    show nana guilty with dis1
    nana "The \"Corresponding Source\" for a work in object code form means all the source code needed to generate,"
    nana "install, and (for an executable work) run the object code and to modify the work,"
    nana "including scripts to control those activities.  However, it does not include the work's System Libraries,"
    menu:
        "or general-purpose tools or generally available free programs which are used unmodified in performing those activities but which are not part of the work.":
            $ nana_points += 1
            $ nana_choice_1 = "1"
            p "or general-purpose tools or generally available free programs which are used unmodified in performing those activities but which are not part of the work."

        "For example, Corresponding Source includes interface definition files associated with source files for the work,":
            $ nana_points -= 1
            $ nana_choice_1 = "0"
            p "For example, Corresponding Source includes interface definition files associated with source files for the work,"
    if nana_choice_1 == "1":
        show nana smile with dissolve
        nana "and the source code for shared libraries and dynamically linked subprograms that the work is specifically designed to require,"
        nana "such as by intimate data communication or control flow between those subprograms and other parts of the work."
        hide nana with dissolve
    if nana_choice_1 == "0":
        show nana angry with dissolve
        nana "The Corresponding Source need not include anything that users can regenerate automatically from other parts of the Corresponding Source."
        nana "The Corresponding Source for a work in source code form is that same work."
        hide nana with dissolve
    call screen map1 with dis1

label nana4:
    scene bg street redux day with dis1
    show nana laugh with dissolve
    nana "This License will therefore apply, along with any applicable section 7 additional terms,"
    nana "to the whole of the work, and all its parts, regardless of how they are packaged."
    nana "This License gives no permission to license the work in any other way,"
    scene black with dissolve
    show bg school gate with dis1
    show nana confident with dissolve
    nana "but it does not invalidate such permission if you have separately received it."
    nana "d) If the work has interactive user interfaces, each must display Appropriate Legal Notices; however,"
    nana "if the Program has interactive interfaces that do not display Appropriate Legal Notices, your work need not make them do so."
    menu:
        "A compilation of a covered work with other separate and independent works, which are not by their nature extensions of the covered work,":
            $ nana_points += 1
            $ nana_choice_1 = "1"
            p "A compilation of a covered work with other separate and independent works, which are not by their nature extensions of the covered work,"

        "and which are not combined with it such as to form a larger program,":
            $ nana_points += 1
            $ nana_choice_1 = "1"
            p "and which are not combined with it such as to form a larger program,"
        
        "in or on a volume of a storage or distribution medium, is called an \"aggregate\"":
            $ nana_points += 1
            $ nana_choice_1 = "1"
            p "in or on a volume of a storage or distribution medium, is called an \"aggregate\""

        "if the compilation and its resulting copyright are not used to limit the access or legal rights of the compilation's users beyond what the individual works permit.":
            $ nana_points -= 1
            $ nana_choice_1 = "0"
            p "if the compilation and its resulting copyright are not used to limit the access or legal rights of the compilation's users beyond what the individual works permit."
        
    if nana_choice_1 == "1":
        show nana smile with dissolve
        nana "Inclusion of a covered work in an aggregate does not cause this License to apply to the other parts of the aggregate."
        nana "Conveying Non-Source Forms."
        hide nana with dissolve
    if nana_choice_1 == "0":
        show nana angry with dissolve
        nana "You may convey a covered work in object code form under the terms of sections 4 and 5, provided that you also convey the"
        nana "machine-readable Corresponding Source under the terms of this License, in one of these ways:"
        nana "a) Convey the object code in, or embodied in, a physical product (including a physical distribution medium),"
        hide nana with dissolve
    call screen map1 with dis1

label nana5:
    scene bg street redux day with dis1
    show nana laugh with dissolve
    nana "But this requirement does not apply if neither you nor any third party retains the ability to install modified object code on the User Product"
    nana "(for example, the work has been installed in ROM)."
    nana "The requirement to provide Installation Information does not include a requirement to continue to provide support service,"
    scene black with dissolve
    show bg school gate with dis1
    show nana confident with dissolve
    nana "warranty, or updates for a work that has been modified or installed by the recipient,"
    nana "or for the User Product in which it has been modified or installed."
    nana "Access to a network may be denied when the modification itself materially and adversely affects the operation of the network or violates the rules and protocols for communication across the network."
    menu:
        "Corresponding Source conveyed, and Installation Information provided,":
            $ nana_points += 1
            $ nana_choice_1 = "1"
            p "Corresponding Source conveyed, and Installation Information provided,"

        "in accord with this section must be in a format that is publicly documented":
            $ nana_points -= 1
            $ nana_choice_1 = "0"
            p "in accord with this section must be in a format that is publicly documented"
        
    if nana_choice_1 == "1":
        show nana smile with dissolve
        nana "(and with an implementation available to the public in source code form),"
        nana "and must require no special password or key for unpacking, reading or copying."
        hide nana with dissolve
    if nana_choice_1 == "0":
        show nana angry with dissolve
        nana "7. Additional Terms."
        nana "\"Additional permissions\" are terms that supplement the terms of this License by making exceptions from one or more of its conditions."
        nana "Additional permissions that are applicable to the entire Program shall be treated as though they were included in this License,"
        hide nana with dissolve
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
        hide ayame with dissolve

    if ayame_choice_1 == "0":
        show ayame angry with dissolve
        ayame "that licensees may convey the work under this License, and how to view a copy of this License."
        ayame "If the interface presents a list of user commands or options,"
        ayame "such as a menu, a prominent item in the list meets this criterion."
        hide ayame with dissolve
    call screen map2 with dis1

label ayame3:
    scene black with dissolve
    show bg classroom 3 day with dis1
    show ayame talk with dissolve
    ayame "Basic Permissions."
    ayame "All rights granted under this License are granted for the term of copyright on the Program,"
    ayame "and are irrevocable provided the stated conditions are met."
    ayame "This License explicitly affirms your unlimited permission to run the unmodified Program."
    menu:
        "The output from running a covered work is covered by this License only if the output,":
            $ ayame_points += 1
            $ ayame_choice_1 = "1"
            p "The output from running a covered work is covered by this License only if the output,"
        "given its content, constitutes a covered work.":
            $ ayame_points -= 1
            $ ayame_choice_1 = "0"
            p "given its content, constitutes a covered work."
    if ayame_choice_1 == "1":
        show ayame smile with dissolve
        ayame "This License acknowledges your rights of fair use or other equivalent,"
        ayame "as provided by copyright law."
        ayame "You may make, run and propagate covered works that you do not convey,"
        ayame "without conditions so long as your license otherwise remains in force."
        ayame "You may convey covered works to others for the sole purpose of having them make modifications exclusively for you, or provide you with facilities for running those works,"
        hide ayame with dissolve
    if ayame_choice_1 == "0":
        show ayame angry with dissolve
        ayame "provided that you comply with the terms of this License in conveying all material for which you do not control copyright."
        hide ayame with dissolve
    call screen map2 with dis1

label ayame4:
    scene black with dissolve
    show bg classroom 3 day with dis1
    show ayame talk with dissolve
    ayame "accompanied by the Corresponding Source fixed on a durable physical medium customarily used for software interchange."
    ayame "b) Convey the object code in, or embodied in, a physical product (including a physical distribution medium),"
    ayame "accompanied by a written offer,"
    ayame "valid for at least three years and valid for as long as you offer spare parts or customer support for that product model,."
    menu:
        "to give anyone who possesses the object code either":
            $ ayame_points += 1
            $ ayame_choice_1 = "1"
            p "to give anyone who possesses the object code either"

        "(1) a copy of the Corresponding Source for all the software in the product that is covered by this License,":
            $ ayame_points += 1
            $ ayame_choice_1 = "1"
            p "(1) a copy of the Corresponding Source for all the software in the product that is covered by this License,"

        "on a durable physical medium customarily used for software interchange, for a price no more than your reasonable cost of physically performing this conveying of source, or":
            $ ayame_points -= 1
            $ ayame_choice_1 = "0"
            p "on a durable physical medium customarily used for software interchange, for a price no more than your reasonable cost of physically performing this conveying of source, or"

    if ayame_choice_1 == "1":
        show ayame smile with dissolve
        ayame "(2) access to copy the Corresponding Source from a network server at no charge."
        ayame "c) Convey individual copies of the object code with a copy of the written offer to provide the Corresponding Source."
        ayame "This alternative is allowed only occasionally and noncommercially,"
        hide ayame with dissolve
    if ayame_choice_1 == "0":
        show ayame angry with dissolve
        ayame "and only if you received the object code with such an offer, in accord with subsection 6b."
        ayame "d) Convey the object code by offering access from a designated place"
        ayame "(gratis or for a charge),"
        hide ayame with dissolve
    call screen map2 with dis1

label ayame5:
    scene black with dissolve
    show bg classroom 3 day with dis1
    show ayame talk with dissolve
    ayame "to the extent that they are valid under applicable law.  If additional permissions apply only to part of the Program,"
    ayame "that part may be used separately under those permissions,"
    ayame "but the entire Program remains governed by this License without regard to the additional permissions."
    ayame "When you convey a copy of a covered work,"
    menu:
        "you may at your option remove any additional permissions from that copy,":
            $ ayame_points += 1
            $ ayame_choice_1 = "1"
            p "you may at your option remove any additional permissions from that copy,"

        "or from any part of it.":
            $ ayame_points -= 1
            $ ayame_choice_1 = "0"
            p "or from any part of it."

    if ayame_choice_1 == "1":
        show ayame smile with dissolve
        ayame "(Additional permissions may be written to require their own removal in certain cases when you modify the work.)"
        ayame "You may place additional permissions on material,"
        ayame "added by you to a covered work, for which you have or can give appropriate copyright permission."
        hide ayame with dissolve
    if ayame_choice_1 == "0":
        show ayame angry with dissolve
        ayame " Notwithstanding any other provision of this License, for material you add to a covered work,"
        ayame "you may (if authorized by the copyright holders of that material) supplement the terms of this License with terms:"
        ayame "a) Disclaiming warranty or limiting liability differently from the terms of sections 15 and 16 of this License; or"
        hide ayame with dissolve
    call screen map2 with dis1

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
    call screen map3 with dis1

label mayo3:
    scene black with dissolve
    show bg street home evening with dissolve
    show mayo normal with dissolve
    mayo "Those thus making or running the covered works for you must do so exclusively on your behalf,"
    mayo "under your direction and control,"
    mayo "on terms that prohibit them from making any copies of your copyrighted material outside their relationship with you."
    menu:
        "Conveying under any other circumstances is permitted solely under the conditions stated below.":
            $ mayo_points += 1
            $ mayo_choice_1 = "1"
            p "Conveying under any other circumstances is permitted solely under the conditions stated below."
        "Sublicensing is not allowed; section 10 makes it unnecessary.":
            $ mayo_points -= 1
            $ mayo_choice_1 = "0"
            p "Sublicensing is not allowed; section 10 makes it unnecessary."
    if mayo_choice_1 == "1":
        show mayo smile with dissolve
        mayo "Protecting Users' Legal Rights From Anti-Circumvention Law."
        mayo "No covered work shall be deemed part of an effective technological measure under any applicable law fulfilling obligations under article 11 of the WIPO copyright treaty adopted on 20 December 1996,"
        mayo "similar laws prohibiting or restricting circumvention of such measures."
        hide mayo with dissolve
    if mayo_choice_1 == "0":
        show mayo angry with dissolve
        mayo "When you convey a covered work,"
        mayo "you waive any legal power to forbid circumvention of technological measures to the extent such circumvention is effected by exercising rights under this License with respect to the covered work,"
        mayo "and you disclaim any intention to limit operation or modification of the work as a means of enforcing, against the work's users,"
        mayo "your or third parties' legal rights to forbid circumvention of technological measures."
        hide mayo with dissolve
    call screen map3 with dis1

label mayo4:
    scene black with dissolve
    show bg street home evening with dissolve
    show mayo normal with dissolve
    mayo "and offer equivalent access to the Corresponding Source in the same way through the same place at no further charge."
    mayo "You need not require recipients to copy the Corresponding Source along with the object code."
    mayo "If the place to copy the object code is a network server, the Corresponding Source may be on a different server (operated by you or a third party)"
    menu:
        "that supports equivalent copying facilities,":
            $ mayo_points += 1
            $ mayo_choice_1 = "1"
            p "that supports equivalent copying facilities,"
        "provided you maintain clear directions next to the object code saying where to find the Corresponding Source.":
            $ mayo_points += 1
            $ mayo_choice_1 = "1"
            p "provided you maintain clear directions next to the object code saying where to find the Corresponding Source."
        "Regardless of what server hosts the Corresponding Source,":
            $ mayo_points -= 1
            $ mayo_choice_1 = "0"
            p "Regardless of what server hosts the Corresponding Source,"

    if mayo_choice_1 == "1":
        show mayo smile with dissolve
        mayo "e) Convey the object code using peer-to-peer transmission,"
        mayo "provided you inform other peers where the object code and Corresponding Source of the work are being offered to the general public at no charge under subsection 6d."
        mayo "A separable portion of the object code,"
        hide mayo with dissolve
    if mayo_choice_1 == "0":
        show mayo angry with dissolve
        mayo "whose source code is excluded from the Corresponding Source as a System Library,"
        mayo "need not be included in conveying the object code work."
        mayo "A \"User Product\" is either (1) a \"consumer product\","
        mayo "which means any tangible personal property which is normally used for personal,"
        hide mayo with dissolve
    call screen map3 with dis1

label mayo5:
    scene black with dissolve
    show bg street home evening with dissolve
    show mayo normal with dissolve
    mayo "b) Requiring preservation of specified reasonable legal notices or author attributions in that material or in the Appropriate Legal Notices displayed by works containing it; or"
    mayo "c) Prohibiting misrepresentation of the origin of that material, or requiring that modified versions of such material be marked in reasonable ways as different from the original version; or"
    mayo "d) Limiting the use for publicity purposes of names of licensors or authors of the material; or"
    menu:
        "e) Declining to grant rights under trademark law for use of some trade names, trademarks, or service marks; or":
            $ mayo_points += 1
            $ mayo_choice_1 = "1"
            p "e) Declining to grant rights under trademark law for use of some trade names, trademarks, or service marks; or"

        "f) Requiring indemnification of licensors and authors of that material by anyone who conveys the material":
            $ mayo_points -= 1
            $ mayo_choice_1 = "0"
            p "f) Requiring indemnification of licensors and authors of that material by anyone who conveys the material"

    if mayo_choice_1 == "1":
        show mayo smile with dissolve
        mayo "(or modified versions of it) with contractual assumptions of liability to the recipient,"
        mayo "for any liability that these contractual assumptions directly impose on those licensors and authors."
        mayo "All other non-permissive additional terms are considered \"further restrictions\" within the meaning of section 10."
        hide mayo with dissolve
    if mayo_choice_1 == "0":
        show mayo angry with dissolve
        mayo "If the Program as you received it, or any part of it,"
        mayo "contains a notice stating that it isngoverned by this License along with a term that is a further restriction,"
        mayo "you may remove that term."
        mayo "If a license document contains a further restriction but permits relicensing or conveying under this License,"
        hide mayo with dissolve
    call screen map3 with dis1

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
        "A \"Standard Interface\" means an interface that either is an official standard defined by a recognized standards body,":
            $ hana_points += 1
            $ hana_choice_1 = "1"
            $ hana_flags.append("noglass")
            p "A \"Standard Interface\" means an interface that either is an official standard defined by a recognized standards body,"
        "or, in the case of interfaces specified for a particular programming language,":
            $ hana_points += 1
            $ hana_choice_1 = "1"
            p "or, in the case of interfaces specified for a particular programming language,"
        "...":
            $ hana_points -= 1
            $ hana_choice_1 = "0"
            p "..."
    if hana_choice_1 == "1":
        show hana smile with dissolve
        hana "one that is widely used among developers working in that language."
        hana "The \"System Libraries\" of an executable work include anything, other than the work as a whole, that (a) is included in the normal form of packaging a Major Component,"
        hide hana with dissolve
        
    if hana_choice_1 == "0":
        show hana angryg with dissolve
        hana "but which is not part of that Major Component,"
        hana "and (b) serves only to enable use of the work with that Major Component,"
        hana "or to implement a Standard Interface for which an implementation is available to the public in source code form."
        hide hana with dissolve
        
    $ day_counter += 1
    jump day_loop

label hana3:
    show bg room night lightoff with dissolve
    scene black with dis2
    show hana smileg with dissolve
    hana "Conveying Verbatim Copies."
    hana "You may convey verbatim copies of the Program's source code as you receive it,"
    hana "in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice;"
    hana "keep intact all notices stating that this License and any non-permissive terms added in accord with section 7 apply to the code;"
    hana "keep intact all notices of the absence of any warranty;"
    hana "and give all recipients a copy of this License along with the Program."
    menu:
        "You may charge any price or no price for each copy that you convey, and you may offer support or warranty protection for a fee.":
            $ hana_points += 1
            $ hana_choice_1 = "1"
            p "You may charge any price or no price for each copy that you convey, and you may offer support or warranty protection for a fee."
        "Conveying Modified Source Versions.":
            $ hana_points -= 1
            $ hana_choice_1 = "0"
            p "Conveying Modified Source Versions."
    if hana_choice_1 == "1":
        show hana smile with dissolve
        hana "You may convey a work based on the Program, or the modifications to produce it from the Program,"
        hana "a) The work must carry prominent notices stating that you modified it,"
        hana "and giving a relevant date."
        hide hana with dissolve
        
    if hana_choice_1 == "0":
        show hana smileg with dissolve
        hana " b) The work must carry prominent notices stating that it is released under this License and any conditions added under section 7."
        hana "This requirement modifies the requirement in section 4 to \"keep intact all notices\"."
        hana "c) You must license the entire work, as a whole,"
        hana "under this License to anyone who comes into possession of a copy."
        hide hana with dissolve
        
    $ day_counter += 1
    jump day_loop

label hana4:
    show bg room night lightoff with dissolve
    scene black with dis2
    show hana smileg with dissolve
    hana "family, or household purposes, or (2) anything designed or sold for incorporation into a dwelling."
    hana "In determining whether a product is a consumer product, doubtful cases shall be resolved in favor of coverage."
    hana "For a particular product received by a particular user,"
    hana "\"normally used\" refers to a typical or common use of that class of product,"
    hana "regardless of the status of the particular user or of the way in which the particular user actually uses,"
    hana "or expects or is expected to use, the product."
    menu:
        "A product is a consumer product regardless of whether the product has substantial commercial,":
            $ hana_points += 1
            $ hana_choice_1 = "1"
            p "A product is a consumer product regardless of whether the product has substantial commercial,"
        "industrial or non-consumer uses, unless such uses represent the only significant mode of use of the product.":
            $ hana_points += 1
            $ hana_choice_1 = "1"
            p "industrial or non-consumer uses, unless such uses represent the only significant mode of use of the product."
        "\"Installation Information\" for a User Product means any methods, procedures,":
            $ hana_points -= 1
            $ hana_choice_1 = "0"
            p "\"Installation Information\" for a User Product means any methods, procedures,"
    if hana_choice_1 == "1":
        show hana smile with dissolve
        hana "authorization keys,"
        hana "or other information required to install and execute modified versions of a covered work in that User Product from a modified version of its Corresponding Source."
        hana "The information must suffice to ensure that the continued functioning of the modified object code is in no case prevented or interfered with solely because modification has been made."
        hide hana with dissolve
        
    if hana_choice_1 == "0":
        show hana smileg with dissolve
        hana "If you convey an object code work under this section in, or with,"
        hana "or specifically for use in, a User Product,"
        hana "and the conveying occurs as part of a transaction in which the right of possession and use of the User Product is transferred to the recipient in perpetuity or for a fixed term "
        hana "(regardless of how the transaction is characterized), the Corresponding Source conveyed under this section must be accompanied by the Installation Information."
        hide hana with dissolve
        
    $ day_counter += 1
    jump day_loop

label hana5:
    show bg room night lightoff with dissolve
    scene black with dis2
    show hana smileg with dissolve
    hana "you may add to a covered work material governed by the terms of that license document,"
    hana "provided that the further restriction does not survive such relicensing or conveying."
    hana "If you add terms to a covered work in accord with this section, you must place,"
    hana "in the relevant source files, a statement of the additional terms that apply to those files, or a notice indicating where to find the applicable terms."
    hana "Additional terms, permissive or non-permissive, may be stated in the form of a separately written license,"
    hana "or stated as exceptions; the above requirements apply either way.
"
    menu:
        "8. Termination.":
            $ hana_points += 1
            $ hana_choice_1 = "1"
            p "8. Termination."

        "You may not propagate or modify a covered work except as expressly provided under this License.":
            $ hana_points -= 1
            $ hana_choice_1 = "0"
            p "You may not propagate or modify a covered work except as expressly provided under this License."
    if hana_choice_1 == "1":
        show hana smile with dissolve
        hana "Any attempt otherwise to propagate or modify it is void, and will automatically terminate your rights under this License"
        hana "(including any patent licenses granted under the third paragraph of section 11)."
        hana "However, if you cease all violation of this License, then your license from a particular copyright holder is reinstated"
        hide hana with dissolve
        
    if hana_choice_1 == "0":
        show hana smileg with dissolve
        hana "(a) provisionally, unless and until the copyright holder explicitly and finally terminates your license, and"
        hana "(b) permanently, if the copyright holder fails to notify you of the violation by some reasonable means prior to 60 days after the cessation."
        hana "Moreover, your license from a particular copyright holder is reinstated permanently if the copyright holder notifies you of the violation by some reasonable means,"
        hana "this is the first time you have received notice of violation of this License (for any work) from that copyright holder,"
        hide hana with dissolve
        
    $ day_counter += 1
    jump day_loop





   # unused stuff:
   #    if 6 < time_of_day < 12:
   #       $ change_time()
   # if (ayame_points > 2 and ayame_choice_1 == "1") or True :
   #     "you are okay"
   # elif (ayame_points < 2 and not ayame_choice_1 == "0"):
   #     "you are not okay"

   