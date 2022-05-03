
define rg = Character('Record Guy', color="#1900ff")
define m = Character('Leadus', color='#ffe000')
define lsure = "audio/leadus_vo_sure.ogg"
define lokay = "audio/leadus_vo_okay.ogg"
define lumm = "audio/leadus_vo_umm.ogg"
define lhello = "audio/leadus_vo_hello.ogg"


    

label start:        
        scene bg living room
        with fade
        
        play music "audio/becoming_friends.ogg"
        
        "So here i am. sitting at home."

        "Kinda boring actually"

        "*Knock Knock*"

        m "Come in!"

        show record guy idle
        with dissolve

        rg "Hey! What's up?"

        play sound lhello

        m "Nothing much, you?"

        rg "Nothing here either. Just wanted to hang out!"

        m "Alright. Well, by all means. Make yourself at home!"

        hide record guy idle
        with dissolve

        scene black
        with fade

        "And so we hung out"

        scene black
        with fade

        "Me and Record Guy grew a little closer today"

        scene bg living room
        with dissolve

        show record guy idle
        with dissolve

        m "Hey, that was fun!"

        rg "Thanks."

        m "No problem!"

        rg "Hey i want to ask you something."

        play sound lumm

        m "What is it?"

        rg "Wanna play some Ultra Custom Night?"

        menu:
                "Sure, Why not?":
                        jump SureWhyNot
                
                "No thanks, Maybe Later":
                        jump nothanks

label SureWhyNot:
        hide record guy idle

        scene black
        with fade

        "And so, me and Record Guy played some Ultra Custom Night."

        "I then promptly managed to die at least fifteen times. All the while, Record Guy was laughing"

        "Seems like Record Guy and I had some fun!"

        return

label nothanks:
        rg "Awww maaaan. Alright. see you later!"

        m "See ya later!"

        hide record guy idle

        scene black
        with fade

        "And so, record guy went home."

        "Welp, Back to being bored"

        "*sigh*"

        return

