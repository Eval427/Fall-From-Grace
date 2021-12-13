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
                $ eval_adine_mood += 1
                $ eval_ffg_ch5_romance = True
                m "Seizing the opportunity, I leaned forward and pressed her smooth, scaly lips to my own. For a few moments, time around us stopped." #Our lips parted...
                m "As our lips parted, Adine smiled and returned her gaze to the fireworks."
                $ renpy.pause (0.5)
                Ad blush hurt "That was nice. Thank you."

            "[[Reject]":
                m "Looking back to the window, I saw Adine awkwardly return her gaze back to the fireworks outside."
    
    $ renpy.pause (0.5)

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
        $ eval_adine_mood += 1
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
    c "The fireworks make the perfect time for his getaway. The area around te portal is almost completely deserted and the sounds of the fireworks could cover up any of his gunshots."
    Ad disappoint hurt "I see. Well, what should we do?"
    c "Adine, you should stay here. Remy, could you get us some assistance? I'll try to buy us time by confronting him." #Excuse for map: Adine asked one of the hospital employees (or maybe Seb?) to get it from her apartment for entertainment
    Ry "On it."
    Ad none hurt "Good luck, [player_name]. Please be safe."
    c "I'll try my best."
    stop soundloop fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (0.5)
    
    scene np1r at Pan((100, 0), (500, 150), 6.0) with dissolveslow
    $ renpy.pause (3.5)
    call endingjustafewminuteslater from _call_ffg_eval_justafewminuteslater

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
    Ad giggle "That's good to hear."
    Ad normal "Hey, I have some really good news, [player_name]. The doctor told me that I could leave the hospital tomorrow!"
    c "Really? That's wonderful, Adine!"
    Ad none "I guess so..."
    c "Is something wrong?"
    Ad "I'm out of a job now. I'm not sure how I'm going to support myself."
    Ad sigh "That job was awful, but it was keeping me afloat. Now... I'm not sure what to do."
    c "Adine, I-"
    m "Suddenly, a flash of inspiration hit me."
    c "What if you moved in with me? The council has allowed me to keep my apartment. You could stay there until you recover."
    Ad "You would really do that for me, [player_name]?"
    c "Of course, Adine. I would love to have your company."
    Ad giggle "Thank you! You don't know how much this means to me."
    hide adine with dissolve
    m "Awkwardly, Adine reached her uninjured wing around my body and squeezed."
    show adine normal with dissolve
    Ad "Is it alright if I come over tomorrow morning? That's supposedly when I'm supposed to get out of this place."
    Ad giggle "But you can never be sure with doctors. They might keep me prisoner even longer!"
    m "I chuckled."
    c "Take care, Adine. I'll see you tomorrow."
    Ad normal "Bright and early. I'm getting out of here as soon as possible."
    stop music fadeout 2.0
    scene black with dissolveslow


#Bad ending: You spend your last moments with Adine in the hospital when the comet comes down. m "And then..." s "There was nothing."
label eval_adine5_remydead_bad:

label eval_adine5_nomap_bad: