#Content at the start of chapter 5 to signify that Adine is now awake
label eval_adine5_phonecall:

    #Ignore this if the mod path wasn't chosen
    if not eval_ffg_mod_path:
        m "After a night of turbulent dreams, my consciousness returned to the shores of the waking world."
        m "(Today is the day of the big fireworks. Who shall I bring?)"
        jump eval_adine5_phonecall_end
    
    play soundloop "fx/phonering.mp3"
    $ renpy.pause (2.0)
    m "After a night of turbulent dreams, I was awoken by the ringing of a phone."
    m "I got up and answered the call."
    stop soundloop
    $ renpy.pause (0.5)
    c "Hello?"

    if eval_ffg_ch4_character == "Anna":
        An "Hey, [player_name]."
        c "Anna? Aren't you going to go and see the fireworks tonight?"

        if not anna4unplayed:
            An smirk "Maybe if I had a special someone to go with."
        else:
            An "I'm too busy to see those damn fireworks."
            
        An smirk "Listen, I'm at the hospital currently. Your lovebird wanted to know if you would come to the hospital for the fireworks show tonight."
        c "Wait, she's up?"
        An "She's not allowed to leave her room or go far from her bed, but yes, she's awake."
        c "Why was I not informed of this earlier?"
        An face "Don't ask me, I'm just relaying information I recently gathered when I walked by her room earlier."
        c "Alright. Well, thank you, Anna."
        An "I make a great messenger pigeon, don't I?"
        c "You've done a fine job so far."
        An smirk "Gee, thanks."
    
    else:
        Sb "Hey, [player_name]."
        c "Sebastian? Aren't you going to see the fireworks tonight?"

        if sebastiansaved:
            Sb "Yes, I was just sent down on a quick trip to the hospital to drop off some paperwork."
        else:
            Sb "No, I have to guard the portal tonight. We never know when Reza may try an escape, and I'm on watch duty tonight."
            c "That's too bad."
            Sb "It's okay. I'll probably still be able to see most of the show from the portal."
        
        Sb "Anyways, I passed by Adine's room while I was here, and she pleaded that I asked you if you would come to the hospital to watch the fireworks show with her tonight."
        c "Wait, she's awake?"
        Sb "That was news to me as well. She's mostly bedridden, but she can get up every once and a while and stretch her legs."
        c "Wow. Well, thank you, Sebastian."
        Sb "Happy to assist. Have a nice time at the fireworks tonight."
        
        if sebastiansaved:
            c "You too."
        else:
            c "Thank you!"
        
    m "With that, the line went silent."
    c "(Who should I bring to the fireworks?)"

    jump eval_adine5_phonecall_end

#Also includes code for the good ending
label eval_adine5_fireworks:
    $ save_name = (_("Chapter 5 - Adine"))
    scene black with dissolvemed
    $ renpy.pause (2.0)

    c "Adine?"
    Ad "[player_name]? Come in!"

    scene evalhospitalroomnight
    show adine optimism hurt
    with dissolveslow
    #Add options for kiss during the fireworks scene
    play music "mx/pier.mp3" fadein 2.0
    Ad "You came."
    c "What? Did you think I wouldn't?"
    Ad sigh hurt "It's just that I thought you would want to go to the fireworks, instead."
    c "The second I heard that you were awake, I came over here. I was so worried, Adine."
    Ad "Yes, worried by something that was entirely my fault."
    c "What do you mean?"
    Ad sad hurt "Look at me! I didn't listen to you and I almost {i}died!{/i}. I was so focused on trying to be special and prove myself that I didn't even stop to consider the consequences of my actions."
    Ad "I'm a terrible friend, my injuries and your stresses? They're all my fault."
    c "Adine..."
    Ad sigh hurt "Listen. I'm sorry for everything. I take full responsibility for my actions."
    c "Adine, I don't blame you for any of this?"
    Ad none hurt "What?"
    c "This was your dream and your passion. You had been training for most of your life for that show to prove how talented you really are."
    c "In your situation, I probably would have done the same thing."
    Ad "I... {w=0.4}I just wanted to do more with my life. I was so sick and tired of being a waitress and delivery flyer that I had to compete, no matter what."
    Ad sad hurt "But now I can't do any of that. With my wing in the current state it's in, I'm out of a job and I won't be participating in any competitions anytime soon, if ever."
    c "You'll recover. It'll just take time for your wing to heal."
    Ad "Injuries like this can take flyers out of the air permanantly, [player_name]. Without care and a bit of luck, I'll be stuck on the ground for the rest of my life."
    m "I rested my hand lightly against her uninjured shoulder."
    c "We'll go through this recovery process together, Adine. I promise."
    $ renpy.pause (0.5)
    Ad optimism hurt "I guess we will, won't we?"
    m "Suddenly, I felt Adine's tail wrap around my body and give me a genle squeeze."
    Ad "I can't hug you normally, so this will have to do for now."
    m "She loosened her grip and returned her tail to its resting position."    
    c "That was a very unique experience, that's for sure."
    Ad none hurt "Is that a good or a bad thing?"
    c "It was nice, I liked it."
    Ad normal hurt "I liked it too."
    Ad "Let's go to the window, the fireworks should be happening any minute now."
    hide adine with dissolve
    m "The two of us made our way over to the window."
    play soundloop "fx/fireworks3.ogg"
    Ad normal hurt "Look! It's starting!"
    m "Looking out across the landscape, the sky lit up with bursts of color."
    show fireworks at Pan((0, 545), (0, 0), 15.0) with dissolveslow
    $ renpy.pause (6.0)
    stop music fadeout 2.0
    hide fireworks with dissolveslow
    if adinestatus == "good":
        m "The two of us turned away from the window and locked eyes."
        m "Hesitating for a moment, Adine brought her muzzle closer to my face and closed her eyes."

        menu:
            "[[Accept]":
                $ eval_adine5_mood += 1
                $ eval_ffg_ch5_romance = True
                m "Seizing the opportunity, I leaned forward and pressed her smooth, scaly lips to my own. For a few moments, time around us stopped." #Our lips parted...
                m "As our lips parted, Adine smiled and returned her gaze to the fireworks."
                $ renpy.pause (0.5)
                Ad blush hurt "That was nice. Thank you."

            "[[Reject]":
                m "Looking back to the window, I saw Adine awkwardly return her gaze back to the fireworks outside."
    
    $ renpy.pause (0.5)

    #If Remy is dead, jump to the bad ending where Remy is dead
    if remydead:
        jump eval_adine5_remydead_bad
        
    Ry look "Adine?"
    Ad normal hurt "Come in!"
    show adine normal hurt at right with move
    show remy normal flip at left with easeinleft
    Ry smile flip "Adine! You're awake!"
    Ad "Remy!"
    Ry "You don't understand how glad I am to see you! As soon as I heard you were awake I came straight over here."
    Ad "Well, I'm glad to see you too, Remy."
    m "Carefully, Adine wrapped her uninjured wing around Remy and hugged him for a few moments."
    Ry normal flip "Hello to you as well, [player_name]."
    c "Hey again, Remy."
    if eval_ffg_ch4_hospital_leave == "late":
        Ry look flip "What happened after I left the hospital last time we were here?"
        c "Not much. I just spent a bit more time with Adine before I left as well."
        Ry normal "Oh, that's good."
        Ad laugh hurt "I'm right here, you know."
        Ry "I guess a bit of context couldn't hurt. The two of us visited you in the hospital the night of your crash even though we really shouldn't have."
        Ry look flip "[player_name] decided to stay back for a little while longer, too, despite the possibility that they might have gotten in trouble."
        Ad normal hurt "Awwww, that's so sweet of you two!"
        show remy shy flip with dissolve
        c "It was nothing, really. We were both just so worried about you."
    elif eval_ffg_ch4_hospital_leave == "sleep":
        $ eval_adine5_mood += 1
        Ry look flip "What happened after I left the hospital last time we were here?"
        c "Not much. I decided to spend the night and [eval_ffg_ch4_character] escorted me out the following morning."
        Ry "[player_name]! We could have gotten in serious trouble if we were caught by someone other than [eval_ffg_ch4_character]."
        Ad laugh hurt "Care to explain?"
        Ry normal "I guess a bit of context couldn't hurt. The two of us visited you in the hospital the night of your crash even though we really weren't supposed to."
        Ry look flip "And it seems [player_name] decided to stay the night and risk getting us in trouble."
        c "I'm sorry, Remy. I just couldn't leave her alone in the room. I was just so worried, and... and..."
        m "My words trailed off as my mind struggled to express the emotions I had felt that night."
        Ad optimism hurt "You really did that, [player_name]?"
        c "Yeah, I stayed the night in your hospital room with you. I hope that isn't weird."
        Ad "No, I just didn't think you cared so much about me. Thanks."
    
    Ad normal hurt "But enough about that, we're going to miss all of the fireworks at this rate!"
    m "The three of us returned to the window and gazed out at the colorful display through the hospital window once more."
    hide adine
    hide remy
    with dissolve

    stop music fadeout 2.0
    $ renpy.pause(1.5)

    m "As I listened to the bursts of the fireworks in the night sky, a terrible realization came over me."
    play music "mx/judgement.ogg" fadein 0.5
    m "Considering how public of an event this was and how everyone would be watching the fireworks, now would be the best time for Reza to make his move."
    m "Not only wa the village basically deserted, but the sounds of the fireworks would also overshadow any gunshots, giving him as much security as he would ever need."
    m "As the portal had been repaired by the mysterious person I met, now was the perfect time for Reza to make his getaway, and I was the only one who knew."
    c "I think I know where Reza is."
    show adine contemplate hurt at right
    show remy look flip at left
    with dissolve
    Ad "What do you mean?"
    c "The fireworks make the perfect time for his getaway. The area around the portal is almost completely deserted and the sounds of the fireworks could cover up any of his gunshots."
    Ad disappoint hurt "I see. Well, what should we do?"
    c "Adine, you should stay here. Remy, could you get us some assistance? I'll try to buy us time by confronting him." #Excuse for map: Adine asked one of the hospital employees (or maybe Seb?) to get it from her apartment for entertainment
    Ry "On it."
    Ad none hurt "Good luck, [player_name]. Please be safe."
    c "I'll try my best."
    stop soundloop fadeout 2.0
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (0.5)
    
    scene np1r at Pan((100, 0), (500, 150), 6.0) with dissolveslow
    $ renpy.pause (3.5)
    call endingjustafewminuteslater from _call_ffg_eval_justafewminuteslater

    #If you don't have the map, jump to the bad ending similar to basegame
    if not adinegoodending:
        jump eval_adine5_nomap_bad

    #This is mostly just taken from basegame with a bit of rephrasing I felt flowed better
    Rz "I mean, what are you doing to do? You can't stop me now, anyway."    
    play sound "fx/rev.ogg"
    show reza gunself with dissolve
    m "He pulled out his gun and pointed it at me."
    c "Reza, wait! Why can't we just talk about this?"
    Rz "We just did."
    c "No! What about-{w=0.7}{nw}"
    Rz "Wait a minute..."
    Rz annoyed "You're just trying to distract me, aren't you?"
    c "No, I'm just-{w=0.7}{nw}"
    show reza angry with dissolve
    Rz "Shut up!" with hpunch
    play sound "fx/rev.ogg"
    show reza gunself with dissolve
    queue sound "fx/gunshot3.ogg"
    queue sound "fx.impact3.ogg"
    $ renpy.pause (0.5)
    m "Suddenly, Reza shot me in the leg, causing me to fall over and squirm in pain." with vpunch
    Rz annoyed "You really thought your little plan would work, didn't you?"
    Rz "They're probably already on their way, aren't they?"
    show reza annoyed flip with dissolve
    $ renpy.pause (0.3)
    show reza at Position(xpos = 0.8) with ease
    play sound "fx/box2.wav"
    $ renpy.pause (0.3)
    show reza at Position(xpos = 0.5) with ease
    $ renpy.pause (0.3)
    show reza at Position(xpos = 0.2) with ease
    $ renpy.pause (0.3)
    hide reza with easeoutleft
    m "I watched as Reza ran to the box containing the generator. He lifted it up using both of his hands before making his way towards the exit as fast as he could."
    show maverick angry at Position(xpos = 1.3)
    show maverick  at Position(xpos = -0.4) with ease
    m "As Reza neared the entrance of the facility, a flurry of gray zipped past me with a thunderous gallop."
    show reza normal at Position(xpos = 0.2) with dissolve
    show reza normal flip
    $ renpy.pause (0.3)
    show reza angry flip with dissolve
    play sound "fx/box1.wav"
    m "I looked towards Reza who turned around, dropped the box, and reached for his pistol."
    show maverick angry at Position(xpos = 1.4)
    play sound "fx/rev.ogg"
    show reza gunpoint flip behind maverick with dissolve
    show maverick at Position(xpos = 0.45, xanchor = "center") with move9
    play sound "fx/impact3.ogg"
    show maverick at Position(xpos = 0.2, xanchor = "center", ypos = 1.0, yanchor = "top")
    show reza at Position(xpos = 0.0, xanchor = "center", ypos = 1.0, yanchor = "top")
    with move9
    queue sound "fx/bite.ogg"
    m "It was Maverick, who pounced immediately. Reza fell to the ground, and before he could so much as react, Maverick buried his teeth in Reza's neck and bit down."
    m "Reza slumped instantly and didn't move again."
    
    show rezabitten2 at Pan((0, 326), (580, 0), 10.0) with fade
    $ renpy.pause (8.5)
    hide rezabitten2
    show maverick normal c at left
    with fade
    
    m "Then, Remy appeared from down the hallway and called out to Maverick."
    show remy look at right with dissolve
    Ry "Maverick, did you really have to kill him?"
    $ renpy.pause (0.3)
    show maverick normal c flip
    $ renpy.pause(0.3)
    Mv "I wasn't going to be taking any chances."
    c "What took you so long, Remy?"
    Ry "[player_name], are you alright?"
    c "He shot me in the leg. Maybe there's a first aid kit in one of these rooms."
    hide maverick
    hide adine
    with dissolve
    m "Remy disappeared into one of the adjoining rooms, only to reappear with a first aid kit shortly after."
    show remy normal with dissolve
    m "Clumsily opening the kit, he slid it in my direction."
    Ry "I don't think there's much I can do to help you. Can you dress your wounds yourself?"
    c "I should be able to. Thank you, Remy."
    m "I carefully tightened a bandage around my injured leg, wincing slightly with the pain."
    Ry look "I'm sorry it took us so long. Before I left to get Maverick, Adine gave me a map of this facility. When I met up with Maverick, he wanted to storm the place head-on. When we heard you two talking, we figured we could surprise him if we went in another way."
    c "Good thinking, Remy. Things could have gone south if you just walked in on Reza."
    Ry "Thanks, but we should probably be getting you some real help."
    show maverick normal c at Position(xpos = -0.4)
    
    $ renpy.pause (0.0)
    show remy at right
    show maverick at Position(xpos = 0.1)
    with ease

    m "He turned to Maverick."
    Ry "What are you waiting for, Maverick?"
    c "Maybe he thinks I'm going to take the generator while you're gone."
    Mv "..."
    $ renpy.pause (0.3)
    show maverick normal c flip
    $ renpy.pause (0.3)
    Mv "I guess you really did want to stop Reza. My apologies."
    $ renpy.pause (0.3)
    show maverick normal c
    $ renpy.pause (0.3)
    hide maverick with easeoutleft
    hide remy with easeoutleft
    stop music fadeout 2.0
    m "He turned and they both left."

    #More taken from basegame
    m "Shortly thereafter, the Administrator appeared from the hallway and came towards me."
    show izumi normal with dissolve
    play music "mx/clocks.ogg" fadein 2.0
    c "Hello, Izumi. You're a bit late this time."
    As "How ironic that you would remember her name now."
    As "Besides, it didn't seem like you really needed me, anyways. Good job."
    c "Her name? What are you talking about?"
    As "I'm not Izumi."
    hide izumi with dissolve
    play sound "fx/undress.ogg"
    $ renpy.pause (0.3)
    m "The person I thought was the Administrator took off their mask, only to reveal a strangely familiar face underneath."
    m "The person before me had my face, down to the tiniest detail. It was loke looking into a mirror or at a twin. It was...{w} me."
    play sound "fx/undress.ogg"
    $ renpy.pause (0.5)
    show izumi normal with dissolve
    As "You understand why I'm waring the mask now?"
    c "How is this possible."
    As "It's complicated. By now, I guess you know that this always ends with you travelling back in time when something goes wrong."
    As "When I was in your position, Izumi died udring out confrontation with Reza, and as all the experience from all the different attempts vanished with her, I decided that I had to become the person who would oversee the next one."
    As "I didn't know just how complicated it would be."
    As "Luckily, she left a lot behind to help me, and I executed her plan just as she would."
    c "So... what now?"
    As "Well, with the generators still intact, we will have no trouble diverting the comet and saving this world, but I also know that you feel very strongly about executing the mission you were sent here for."
    As "Unfortunately, I'm starting to realize now that this won't be possible."
    c "What are you talking about?"
    As "As outlined in Izumi's plan, I deleted the coordinates that would lead back to humanity's portal when I repaired this one, replacing them with coordinates to travel back in time to the day of your arrival in this world."
    As "Unfortunately, this means that our connection to humanity's portal is lost."
    c "Are you saying we could've saved humanity if you just didn't remove those coordinates?"
    As "I'm afraid so."
    c "Then why did you do it?"
    As "I didn't realize it would come to this. I just executed her plan as she would have. I can understand her reasoning for it, though."
    As "It presents an extraordinary risk. Eliminating these coordinates also eliminates the possibility of Reza getting away through the portal and taking the generator we need with him."
    c "Why not just tie them to my biometric data like the coordinates we need to travel back in time?"
    As "That wouldn't be much help, because in scenarios where Reza escapes with the generator, he wouldn't hesitate to kill you to take what he needs to bypass the biometrics scan and use the portal anyway."
    c "Then the only way to achieve what we want is to not delete those coordinates."
    As "Can we really take that risk? You know that if we fail badly enough even once - if the portal gets destroyed, or if both the Administrator and you die - there won't be any more chances."
    c "If you have seen what goes on from the Administrator's side during my stay here, I suppose you should be the one to decide that."
    c "That still doesn't address the question of what we should do now, though."
    As "If we want to make this happen, one of us will have to go back and do this all over again."
    c "And what happens to the other?"
    As "They could stay here and live their life however they wanted."
    c "What about Adine?"
    As "I wish I could stay with her. All she does for the orphans... I wish I could be part of that."
    As "I wish I could be done with this already and settle down, but someone has to go back and ensure we can reach the outcome both of us want. No matter if it's you or me, one of us has to do it."
    As "Otherwise, all those we know back home, they... I don't think I need to tell you."
    c "Why are you making me think of those who suffer?"
    As "You'll never forget them, and if you don't do this, it will haunt you. I know."
    c "What do you want me to do? Go back in time and do it all over again?"
    As "It's what we've been trying to do all this time, you know. No compromise."
    c "And of course you want me to do it so you can stay here, huh?"
    As "I will do it myself if that's what it takes. I just hoped it wouldn't have to be me."
    c "Don't we both?"
    As "If we wanted to settle for an outcome where we just stop the comet and stay here, we could have done so a long time ago."
    c "That doesn't mean that we're both not tired of this."
    As "Maybe forgetting everything again by stepping through the portal would be a boon, then."
    c "Don't try to make this more palatable for me. How many times have we done this now?"
    As "..."
    As "I don't know."

    #Back to your dose of Eval original content. Sorry for that little copy-paste block
    show izumi at Position(xpos = 0.3) with ease
    m "With that, the Administrator, or myself, started making their way to the portal."
    c "Wait."
    show izumi normal flip
    $ renpy.pause (0.3)
    As "Yes?"
    m "I looked up at the last human person I would most likely ever see again."
    c "Okay, you can go now."
    As "Goodbye, [player_name]."
    show izumi normal
    $ renpy.pause (0.3)
    hide izumi with easeoutleft
    $ renpy.pause (1.0)
    scene black with dissolveslow

    nvl clear
    window show

    n "It was not long until Remy and Maverick returned with a few other dragons, who proceeded to dress the wound on my leg."
    n "Luckily, the bullet had cleanly passed through the soft tissue of my leg, and they were done in a matter of minutes."
    n "I spent the next few days resting in the hospital, just a few rooms away from Adine, who visited from time to time."

    window hide
    nvl clear
    window show

    n "In this time, I warned the dragons of the incoming comet, telling them to check the PDAs that I had given them for verification of my claims."
    n "My warning were taken seriously, and a plan was put into motion to divert the comet."
    n "With the power of the generators stored within the facility, the dragons were easily able to put their plan into motion, using their energy to change the trajectory of the fiery ball of rock." #Meh

    window hide
    nvl clear
    window show

    n "Upon later discovering that the portal was no longer operational, it was decided that my ambassador status would be revoked."
    n "However, the council allowed me to keep my apartment and paid for my medical expenses."
    n "Finally able to leave the hospital, I stopped by Adine's room one last time."

    window hide
    nvl clear

    $ renpy.pause (2.0)

    scene evalhospitalroom with dissolveslow
    show adine normal hurt with dissolve
    play music "mx/hopefulAMELY.ogg" fadein 2.0
    $ renpy.pause (0.3)
    c "How are you feeling today, Adine?"
    Ad "Aside from this damn bandage, I'm feeling better today. How about you."
    c "I think my leg has completely healed at this point. I don't feel any pain on it anymore."
    Ad giggle hurt "That's good to hear."
    Ad normal hurt "Hey, I have some really good news, [player_name]. The doctor told me that I could leave the hospital tomorrow!"
    c "Really? That's wonderful, Adine!"
    Ad none hurt "I guess so..."
    c "Is something wrong?"
    Ad "I'm out of a job now. I'm not sure how I'm going to support myself."
    Ad sigh hurt "That job was awful, but it was keeping me afloat. Now I'm not sure what to do."
    c "Adine, I-"
    m "Suddenly, a flash of inspiration hit me."
    c "What if you moved in with me? The council allowed me to keep my apartment, so you could stay there until you recover."
    Ad "You would really do that for me, [player_name]?"
    c "Of course, Adine. I would love to have your company."
    Ad giggle hurt "Thank you! You don't know how much this means to me."
    hide adine with dissolve
    m "Awkwardly, Adine reached her uninjured wing around my body and squeezed."
    play sound "fx/hug.mp3"
    show adine normal hurt with dissolve
    Ad "Is it alright if I come over tomorrow morning? That's supposedly when I'm supposed to get out of this place."
    Ad giggle hurt "But you can never be sure with doctors. They might keep me prisoner even longer!"
    m "I chuckled."
    c "Take care, Adine. I'll see you tomorrow."
    Ad normal hurt "Bright and early. I'm getting out of here as soon as possible."
    stop music fadeout 2.0
    scene black with dissolveslow
    jump eval_ffg_ch6
    
    #Temporary. Delete later
    $ renpy.pause (5.0)
    $ renpy.pop_call
    jump mainmenu


#Bad ending: You spend your last moments with Adine in the hospital when the comet comes down. m "And then..." s "There was nothing."
label eval_adine5_remydead_bad:
    m "As I listened to the bursts of the fireworks in the night sky, a terrible realization came over me."
    play music "mx/judgement.ogg" fadein 0.5
    m "Considering how public of an event this was and how everyone would be watching the fireworks, now would be the best time for Reza to make his move."
    m "Not only wa the village basically deserted, but the sounds of the fireworks would also overshadow any gunshots, giving him as much security as he would ever need."
    m "As the portal had been repaired by the mysterious person I met, now was the perfect time for Reza to make his getaway, and I was the only one who knew."
    c "I think I know where Reza is."
    show adine contemplate hurt with dissolve
    Ad "What do you mean?"
    c "The fireworks make the perfect time for his getaway. The area around te portal is almost completely deserted and the sounds of the fireworks could cover up any of his gunshots."
    Ad disappoint hurt "I see. Well, what should we do?"
    c "You're in no shape to do anything at the moment. I'll go to the portal and confront Reza myself."
    Ad "By yourself?"
    c "He would hesitate to shoot another human and I'll raise less suspicion going there alone."
    Ad sigh hurt "Just... Please be safe out there."
    c "I will, Adine."

    stop soundloop fadeout 2.0
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (0.5)
    
    scene np1r at Pan((100, 0), (500, 150), 6.0) with dissolveslow
    $ renpy.pause (3.5)
    call endingjustafewminuteslater from _call_ffg_eval_justafewminuteslater

    Rz gunself "Now, I recommend you just stay right where you are. I won't hesitate to shoot you if I catch the slightest hint of retaliation."
    Rz angry "I've been risking my life for this every day for the last two weeks. What did you do during that time? sip champange in your nice apartment?"
    Rz "Besides, this generator and the whole building came from our time."
    show izumi normal behind reza at Position(xpos=1.25, xanchor="center")
    Rz "They belong to humanity!" with Shake((0, 0, 0, 0), 2, dist=10)

    show reza at Position(xpos=0.45, xanchor="center")

    m "Suddenly, the Administrator came out of the shadows in the hallway behind Reza."

    show izumi normal at right with ease

    As "No, they belong to me."
    play sound "fx/rev.ogg"
    show reza angry flip
    m "Confused, Reza sput around, aiming his gun at the newcomer who was slowly walking towards him."
    Rz "Who the fuck are you? Freeze! I said freeze!"
    show izumi at Position(xpos=0.8, xanchor="center") with ease
    As "Want to waste your bullets on me? Feel free. It will change nothing."
    play sound "fx/rev.ogg"
    Rz gunpoint flip "If you say so."
    play sound "fx/gunshot2.wav"
    $ renpy.pause(0.5)play sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/impact3.ogg"

    hide izumi with easeoutbottom

    m "He pulled the trigger, and the Administrator fell to the ground with a dull thud that knocked her mask off."

    $ persistent.izumiseen = True

    show izumiinjured6 at Pan((300, 0), (600, 608), 7.0) with fade

    $ renpy.pause (5.0)

    hide izumiinjured6
    show reza annoyed at Position(xpos=0.9)
    with fade

    Rz "Don't try anything, [player_name]."
    m "I did as he said and could only watch as he took the generator and left."
    
    show reza annoyed flip at Position (xpos = 0.8) with ease
    play sound "fx/box2.wav"
    $ renpy.pause (2.0)
    show reza annoyed
    $ renpy.pause (0.3)
    show reza at Position (xpos = 0.5) with ease
    $ renpy.pause (0.3)
    show reza at Position (xpos = 0.2) with ease
    $ renpy.pause (0.3)
    hide reza with easeoutleft

    m "As Reza left the building, I reflected for a moment."
    m "If Reza got away with those generators, the dragon would would be destined to fall to the comet."
    m "No matter how foolish or rash it may be, I had no other choice but to get those generators back from him."

    jump eval_adine5_remydead_insert

label eval_adine5_nomap_bad:
    Mv "Maybe I can."
    play music "mx/martyr.ogg" fadein 0.5
    m "Suddenly, Maverick and Remy appeared next to me."
    show reza at Position(xpos = 0.9) with ease
    show maverick normal flip at Position(xpos = 0.2, xanchor = "center") with easeinleft
    show remy look flip at Position(xpos = 0.05, xanchor = "center") with easeinleft
    Rz angry "You planned this, didn't you, [player_name]?"
    Rz "Traitor!" with hpunch
    Rz "And to think I let you distract me with such a cheap trick! Just because I thought there was still a stred of humanity within you..."
    c "I'm not the one killing innocent dragons, here."
    Rz "And I'm not the one risking the existance of humanity by befriending a bunch of big lizards!"
    play sound "fx/rev.ogg"
    show reza gunself with dissolve
    show reza gunpoint with dissolve
    m "He pulled out his gun, not sure which one of us he should be aiming at."
    Rz "Just let me go, and I'll forget this thing ever happened."
    c "You've got six bullets for three people. Do you really think you can do that, Reza? Do you think this is worth risking your life for?"
    Rz "I've been risking my life for this every day for the last two weeks. What did you do during that time? Sip champagne in your nice apartment?"
    c "But if we have just cooperated with the drago-{w=1.0}{nw}"
    Rz "I don't want to hear it. Cooperation would have led to the failure of our plans and the fall of humanity."
    Rz "Besides, this generator and the whole building came from out time."
    show izumi normal behind reza at Position(xpos = 1.25, xanchor = "center")
    Rz "They belong to humanity!" with Shake((0, 0, 0, 0), 2, dist = 10)

    show reza at Position(xpos = 0.45, xanchor = "center")
    show remy at Position(xpos = -0.3, xanchor = "center")
    show maverick at Position(xpos = -0.3, xanchor = "center")
    with ease

    m "Suddenly, the Administrator came out of the shadow in the hallway behind Reza."
    show izumi normal at right with ease
    As "No, they belong to me."
    play sound "fx/rev.ogg"
    show reza angry flip
    m "Confused, Reza spun around, aiming his gun at the newcomer who was slowly walking towards him."
    Rz "Who the fuck are you? Freeze! I said freeze!"
    show izumi at Position(xpos = 0.8, xanchor = "center") with ease
    As "Want to waste your bullets on me? Fell free. You can't stop all of us."
    play sound "fx/rev.ogg"
    Rz gunpoint flip "If you say so."
    play sound "fx/gunshot2.wav"
    $ renpy.pause (0.5)

    play sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/impact3.ogg"

    hide izumi with easeoutbottom

    m "He pulled the trigger, and the Administrator fell to the ground with a dull thud that knocked her mask off."

    $ persistent.izumiseen = True

    show izumiinjured6 at Pan((300, 0), (600, 608), 7.0) with fade

    $ renpy.pause (5.0)

    hide izumiinjured6
    show maverick normal flip at Position(xpos=0.2, xanchor='center')
    show adine at Position(xpos=0.1, xanchor='center')
    show reza at Position (xpos = 0.9)
    with fade

    show reza gunpoint
    play sound "fx/gunshot2.wav"
    $ renpy.pause (0.5)
    hide remy with easeoutbottom
    m "Reza was quick with his gun and shot Remy in the side before Maverick even had a chance to charge."
    play sound "fx/snarl.ogg"
    show maverick angry flip with dissolve
    $ renpy.pause (1.0)
    play sound "fx/gunshots2.ogg"
    show maverick at Position (xpos = 0.35) with ease
    $ renpy.pause (0.2)
    show maverick at Position (xpos = 0.5) with ease
    $ renpy.pause (0.2)
    hide maverick
    hide reza
    with easeoutbottom

    m "Despite mutliple bullet wounds, Maverick managed to bring Reza to the floor with him."
    play sound "fx/gunshot2.wav"
    m "Maverick was able to bite Reza on his side, but a bullet to the head caused him to slump over, lifeless."

    show reza annoyed b with easeinbottom

    Rz angry "What now, [player_name]? Are you going to let me through, or do I have to finish the job with you?"
    m "Remy was lying on the ground next to me, injured, while Maverick and the Administrator lay dead in a pool of their own blood."

    show maverickdead1 at Pan((500, 500), (250, 400), 7.0) with fade
    $ renpy.pause (5.0)
    show izumidead6 at Pan((0, 0), (140,79), 7.0) with fade
    $ renpy.pause (5.0)
    hide izumidead6
    hide maverickdead1
    show reza at center
    with fade

    c "Now you hesitate to kill, after doing all this?"
    show reza annoyed with dissolve
    show reza at Position (xpos = 0.8) with ease
    play sound "fx/rev.ogg"
    Rz gunself b "It's your choice."
    Ry "{size=-5}Please...{/size}"
    c "Just... go."
    Rz angry b "If you told me that just a few minutes ago, I wouldnt have had to do all of this. Heck, you could've come with me, you stupid idiot. But if you want to die here with everyone else, feel free."
    Rz annoyed b "Alright, step over there and lie on the ground. If I see either of you moving before I'm gone, I'll shoot."
    m "I did as he said and could only watch as he took the generator and left."
    show reza annoyed flip at Position(xpos = 0.8) with ease
    
    play sound "fx/box2.wav"
    $ renpy.pause (2.0)
    show reza annoyed
    $ renpy.pause (0.3)
    show reza at Position (xpos = 0.5) with ease
    $ renpy.pause (0.3)
    show reza at Position (xpos = 0.2) with ease
    $ renpy.pause (0.3)
    hide reza with easeoutleft

    $ renpy.pause(2.0)
    Ry "[player_name] you need to stop him."
    c "But how? He's armed and I've got nothing to defend myself with."
    Ry sad "I'm not sure, but you have to try."
    m "Remy was right. Without the power of those generators, this world was destined to meet it's end. No matter how rash the decision seemed, I needed to do everything I could."
    c "Don't move, Remy, you're injured. I'll go."
    m "Remy groaned as he turned around to look at me."
    Ry sad "Good luck, [player_name]."
    label eval_adine5_remydead_insert:
        pass
    c "I carefully got up, following where Reza had left the facility and slowly opened the door outside."

    scene black with dissolveslow
    $ renpy.pause(1.5)
    scene np1r at Pan((500, 150), (500, 150), 6.0) with dissolvemed
    play music "mx/confrontation.ogg"

    m "When I opened the doors, I spotted Reza at the portal's terminal."
    c "{size=+5}Reza!{/size}" with hpunch
    m "Reza looked up from the terminal, his eyes furrowed in rage."
    show reza rage with dissolve
    Rz "Didn't I tell you to sit still, [player_name]?"
    Rz "I give you one simple request and you fail it miserably."
    Rz normal "You really think you can stop me, don't you? You think you're strong enough to take on a person with a loaded gun."
    Rz laugh "I question how someone as stupid as you was given the opportunity to visit this world in the first place. Normally they would send someone more qualified for the job."
    c "Reza, please. This world needs those generators to deflect the meteor. Without it the dragons are doomed!"
    Rz normal "And why should I care if these big lizards get hit by the meteor? They're not the future for humanity, these generators are."
    Rz "Listen, [player_name], you should feel honored that I haven't already shot hot lead through your skull. Just stand back and let me go."
    Rz gunself "Or else."

    menu:
        "[[Let him go.]":
            m "There was no way I was going to stop him. I had tried to convince him, but his gun was much more powerful than my words." #Meh
            c "Fine. You win."
            Rz normal "Good. Now don't move a muscle, or you'll never have to opportunity to do so again."
        
        "[[Grab the gun.]":
            $ eval_ffg_ch5_bad_shot = True
            m "I suddenly lunged at Reza's gun and grabbed the barrel, pointing it down from my head."
            play sound "fx/gunshot3.ogg"
            m "Reza pull on the trigger, sending a searing pain up my leg. I released my grip from the gun and held my leg in anguish."
            Rz rage "You actually tried that? I can't believe how utterly rash and naive you are."
            Rz "I should fucking kill you, but I'm not here to end human lives, I'm here to save them."
            Rz "Next time I recommend cooperating with the person with the gun, [player_name]. Not like there will be a next time for you after that meteor strikes."
            c "Reza...{w=1.5){nw}"
            Rz gunself "One more word and I'll change my mind about killing you."
            m "I stayed silent, clutching my bloody leg and gritting my teeth in pain."
            Rz normal "Good. Now you've learned your lesson."

    show reza normal flip
    hide reza with easeoutright
    m "I watched as Reza made his way back to the portal's terminal."
    play sound "fx/portalhit.mp3"
    m "He interacted with it briefly before the portal sprang to life. With the butt of his gun he smashed the terminal panel, shattering the glass."
    queue sound "fx/quicktel.mp3"
    m "Grabbing the generators, he stepped into the portal and, after a flash of light, was gone."
    
    if eval_ffg_ch5_bad_shot:
        m "I laid down on the ground in pain, taking off my shirt and tying it around my leg to hinder the blood flow."
        m "Soon, multiple dragons arrived on the scene, seemingly called in by the musterious bang after the fireworks show had already ended."
    else:
        m "Soon, multiple dragons arrived on the scene, seemingly called in by the activation of the portal."
    
    nvl clear
    window show

    if eval_ffg_ch5_bad_shot:
        n "I laid down on the ground in pain, taking off my shirt and tying it around my leg to hinder the blood flow."
    n "Soon, multiple dragons arrived on the scene, seemingky called in by the activation of the portal."
    if eval_ffg_ch5_bad_shot:
        n "I was quickly transported to the hospital and treated for my wounds."
    if not remydead:
        n "While both Maverick and the Administrator were dead, it turned out that Remy's injury was fairly minor, and he soon got the medical attention he needed."
    n "When I attempted to use the portal to follow Reza, however, I discovered that the portal's terminal was completely destroyed, and the only person who would know how to fix it laid buried in the earth."
    n "After Reza had arrived on the other side, he or humanity must have quickly deactivated the portal in order to prevent anyone from connecting with it again."
    n "I warned the dragons about the comic, but without the generators from the underground building, they failed at diverting the comet enough to make a difference."

    window hide
    nvl clear
    window show

    n "I was out of options. Reza had destroyed the portal on his way out and the comet was bound to hit the earth in a matter of days."
    n "As the hours passed, I found myself at a loss, aimlessly wandering the deserted streets and looking into the closed buildings."
    n "I met up with Adine in her hospital room, hoping to spend my final few hours in her presence."

    window hide
    nvl clear

    scene evalhospitalroom
    show adine sad hurt
    with dissolveslow
    play music "mx/sad.ogg"
    Ad "I guess this is the end, isn't it?"
    c "I'm sorry."
    Ad "You can't blame yourself. You did what you could. Even if it had to end like this, I enjoyed my time with you. Let's not have any regrets now."
    c "Thank you."
    Ad disappoint hurt "Remember when I asked you what you were going to do if you knew the world was going to end?"

    if adine1choice == "fullest":
        Ad "You told me you would enjoy life to the fullest until the last moment. Does that mean spending time with me is living your life to the fullest?"
        c "Yes, Adine. I wouldn't trade this moment for anything else."
        Ad optimism hurt "Thank you, [player_name]. That means a lot."
    elif adine1choice == "goodbyes":
        Ad "You told me you would say your last goodbyes and hope for the best. Is this what this is, your last goodbyes?"
        c "No, because I'm not leaving you until the end."
        Ad optimism hurt "Oh, [player_name]. That's very sweet of you."
    elif adine1choice == "outside":
        Ad "You told me you would stay outside and watch it all unfold before your eyes."
        c "Yes, but I'd like to stay inside and watch it happen with you."
        Ad optimism hurt "Together until the end."
    else:
        Ad "You told me you'd hide in a bunker deep underground, but I'm not sure we can do that."
        c "Even if we did, we wouldn't be able to survive on the barren landscape."
        Ad "Yeah..."
    
    m "The sky started to grow darker as the comet drew closer."
    Ad sad hurt "I can't believe it has to end like this."
    Ad "I was so close to winning that competition, I just know it! But my damn wing had to give out at the very last moment."
    Ad disappoint hurt "Look at me, [player_name]. I'm nothing more than a waitress making minimum wage and a terrible flyer."
    c "Adine, you're so much more than that."
    Ad "I got one opportunity in my life to make a difference and I blew it. Now the world's going to end and I'm still just a nobody."
    c "Adine, you are an amazing person, I really mean it."
    if varasaved:
        c "Think about Amely and Vara. What would they do without you? You are the light of their lives."
    else:
        c "Think about Amely. What would she do without you? You are the light of her life."
    c "I also know firsthand that you are a spectacular flyer, and despite the incident during the event, your drive and motivation to reach your goals is inspiring."
    Ad "..."
    if eval_ffg_ch5_romance:
        hide adine with dissolve
        m "Suddenly, I found myself in the warm embrace of Adine's wings. Her soft scales enveloping my upper body."
        Ad optimism hurt "If this is the end, I'm glad I'll be spending it with you."
        c "Me too, Adine."
        m "The two of us looked out the window in silence, watching the grow larger and larger."
        m "Adine pressed her frills against my cheek, and I could feel her lips quivering in fear."

    else:
        m "Suddenly, I felt Adine grab my hand in her wingclaw and squeeze tightly."
        Ad optimism hurt "If this is the end, I'm glad I'll be spending it with you."
        c "Me too, Adine."
        m "The two of us looked out the window in silence, watching the grow larger and larger."
    
    Ad "{size-=5}Goodbye, [player_name].{/size}"
    m "I gulped, holding back tears."
    c "Goodbye, Adine."

    m "Tears rolled from her eyes as the room got darker."
    m "Blackness overtook the sky, screaming and crying could be heard somewhere off in the distance."
    m "And then...{w=3.0}{nw}"
    scene black
    stop music
    $ renpy.pause (3.0)
    play sound "system3.wav"
    s "There was nothing."

    #I almost cried writing this. I hope it lands

    #This was also written on an airplane with TERRIBLE turbulence if that interests whoever is reading this

    #Roll credits