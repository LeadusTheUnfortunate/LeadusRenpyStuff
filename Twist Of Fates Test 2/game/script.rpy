#characters
define y = Character('Yako', color="#ff0000")
define m = Character('Leadus', color="#ffd000")

#Music
define Becoming_Friends = "audio/becoming_friends.ogg"

#leadus Voice Lines
define lumm = "audio/leadus_vo_ummm.ogg"
define lok = "audio/leadus_vo_okay.ogg"
define lsure = "audio/leadus_vo_sure.ogg"
define lhello = "audio/leadus_vo_hello.ogg"

#Yako Voice Lines (To be worked on)

label start:
    play music Becoming_Friends

    scene bg outside
    with fade

    "Yako called me to his place"

    "He says he wants to show me something."

    "Of course I'm gonna see it. I mean, come on. It's Yako we're talking about"

    "So that means it's gonna be cool!"

    scene black
    with dissolve

    "I go up to Yako's door and give it a knock."

    y "come in"

    "And so I enter."

    scene bg living room
    with dissolve

    m "Oooh. Nice place you have here!"

    y "Yeah. The living room's pretty big."

    play sound lumm
    
    m "Is this what you wanted to show me?"

    y "Not quite. You'll see."

    "Yako reaches in to a suitcase lying on the floor."

    "It opens with a click."

    y "Now THIS..."

    "Yako pulls something out of the suitcase that leaves me in shock"

    y "Is my pride and joy."

    m "WOAH. Okay. That's awesome."

    "It was a freaking rail gun"

    "A"

    "Freaking"

    "Rail"

    "Gun"

    "Needless to say, I was very impressed"

    scene black
    with fade

    "Yako and I grew a little closer today"

    scene bg living room
    with dissolve

    y "Hey."

    y "Hello?"

    y "HEY!"

    m "Wha- What is it?"

    "I was so focused on the freaking gun he brought that I just kinda... zoned out, I guess."

    y "I have a question."

    play sound lok

    m "Go ahead."

    y "So, why did you pick me for the team?"

    y "I mean, I thank you for picking me. but, why?"

    y "Don't Muto's and Humans have a rivalry"

    play sound lumm
    
    m "Yes, but you're different."

    menu:
        "You are very helpful to me":
            jump helpful
        "You are one of my best friends":
            jump friends

label helpful:
    m "You're very helpful to me Yako. And becuase of that, I think you're different."

    m "Sure, you may have a monster's body. but you have a human's heart."

    y "No. I dont."

    m "I meant figureatvly"

    y "I know, I was giving you a hard time."

    "We both laughed."

    "Seems like we had a great time"
    return

label friends:
    m "Yako, you are one of my best friends. You've stuck with me through a lot."
    
    m "Because of that, I think you're different."
    
    m "Sure, you may have a monster's body. but you have a human's heart."

    y "No. I dont."

    m "I meant figureatvly"

    y "I know, I was giving you a hard time."

    "We both laughed."

    "Seems like we had a great time"
    return