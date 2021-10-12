#Changes the music to better match the mood of the scene (and I hate funness.ogg)
label eval_adine4_music:
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    Ad disappoint b "I... just have to try, you know?"
    play music "mx/outpost.mp3" fadein 1.0
    jump eval_adine4_music_end

#Start of the scene changes, including the option to start mod content, the competition scene, and the crash (ow.)
label eval_adine4_changes:
    menu:
        #Default path
        "[[Mention Amely.]":
            c "What about Amely? If something happened to you, how do you think they would explain to her that you just suddenly stopped showing up, huh?"
            jump eval_adine4_default_path
        
        #Modded path
        "[[Say nothing.]":
            pass

    Ad determined b "Listen, [player_name]. I have to do this for myself. I have to prove to myself, my parents, and every other person who has doubted me my entire life that I can do this."
    c "Adine, what you are doing could have consequences. What if you hurt yourself? Or worse..."
    Ad determined c "You know what? If I keep having that mindset, I'll never do anything with my life. I will fly and do the best damn job I've ever done, and there's nothing you can do to stop me."
    hide adine with dissolve
    m "Before I could reply, she angrily stomped off towards the building and joined the group of contestants."
    m "She glanced at me over her shoulder one last time before making her way inside."
    m "In the end, I decided to stay and watch from the sidelines. I didn't want to join the rest of the audience, as I was sure it would get me unwanted attention."
    m "I was soon lost in my own thoughts, worrying about Adine's rash decision to participate in the competition."
    m "A booming voice brought me back to reality."
    "Announcer" "Ladies and gentlemen! It is my honor to be the announcer for this year's competition! We've got a lineup of some amazing flyers from all over the area here today!"
    m "The crowd cheered as the group of contestents made their way onto the stage. From my position it was difficult to see, but I spotted Adine massaging her injured shoulder."
    m "One by one, the contestants showed off their skills in a variety of moves, usually followed by a roar of applause from the audience."
    "Announcer" "Next up is contestent number five..." #If I need a name I can use "Jet"
    m "As more of the contestants finished their performance, I became increasingly anxious."
    "Announcer" "And now... contestant number nine!"
    m "I nervously glanced up at the stage, spotting Adine fiddling with some sort of device on her tail."
    c "(Looks like she hasn't reconsidered her choice.)"
    "Announcer" "Next on the stage is number 11! This contestant is a promising newcomer who will show her skills to the public here for the very first time in her debut performance. Please welcome... {w}[adinestagename]!"
    m "Claps arose once again from the crowd, who eargerly watched the newcomer."
    m "Adine slowly waddled to the edge of the stage, the number eleven draped across her chest."
    m "Bringing her tail forward, she fiddled with the device on her tail. In an instant, a thick, billowing cloud of smoke rose from the device."
    #m "Bringing her tail up to her face, she opened her mouth and two small streams of liquid made contact with the device on her tail. In an instant, a thick, billowing cloud of smoke rose from the device." - Saunders implied no fire breath
    m "A small murmur formed within the crowd. They seemed excited to see Adine's performance."
    m "She turned around and waved her tail in small ciruclar motions, creating rings of the smoke behind her."
    play sound "fx/takeoff.ogg"
    m "She turned to face the audience once more, and with a running start, took off through the rings of smoke she had just created."
    m "Her performance was a sight to behold. She began with a series of fluid twists and turns, creating patterns in the air with the smoke."
    m "However, as her performance continued, her motions became more jagged and she seemed to lean into her injured wing."
    $ eval_stage_name_letter = adinestagename[0].upper()
    if len(adinestagename) > 1:
        m "With grim determination, she gained even more altitude and started moving in calculated motions. Soon, smoke formed the letter \"[eval_stage_name_letter]\"."
        c "(Is she writing out her stage name?)"
        if len(adinestagename) > 7:
            c "(That's quite a long thing to write out with smoke.)"
        $ eval_stage_name_letter = adinestagename[1].upper()
        "However, while working on the letter \"[eval_stage_name_letter]\", her body sharply twisted and Adine quickly started loosing altitude."
        
    else:
        m "With grim determination, she gained even more altitude and started moving in calculated motions. Soon, smoke formed the letter \"[eval_stage_name_letter]\"."
        c "(I'm glad I kept her stage name short.)"
        m "However, upon finishing the letter, her body sharply twisted and Adine quickly started loosing altitude."
    m "The crowd gasped, but with some difficulty Adine regained her composure." #Get rid of this
    m "Seeming to think it was part of the performance, the dragons cheered and applauded." #Or this
    m "Adine once again started to ascend back into the air creating circles in the air which gradually got smaller and smaller."
    c "(This is it. This is her special move.)"
    m "As her circles became tiny, she suddenly tucked in her wings and went into a nosedive through the circles, disrupting the smoke in beautiful patterns."
    m "She descended quickly, and as she unfurled her wings to stop her downward momentum, she screamed in pain and lost her balance."
    m "She had lost control. All I could do was watch as Adine desperately attempted to correct herself as she came closer and closer to th-{w=1.0}{nw}"
    stop music
    play sound "fx/adinecrash.mp3"
    scene black with Shake ((0, 0, 0, 0), 2, dist=50)
    m "I couldn't watch. I shut my eyes before Adine hit the ground with a horrifying thud."
    $ renpy.pause (2.0)
    "Announcer" "Ladies and gentlemen it seems we have had an unfortunate accident. Please, stay calm. Paramedics are already on their way."
    m "Slowly, I decided to open my eyes and witness the horrors I knew stood before me."
    play soundloop "fx/murmur.wav" fadein 3.0
    scene fac12
    show evalsmokeoverlay
    with dissolveslow
    m "I was met with a thick cloud of smoke obscuring my vision. The device on her tail must have exploded on contact with the ground."
    m "Through the smoke I saw Adine's body lying in a small crater in the earth. It wasn't pretty."
    m "The right side of her body had taken most of the impact, but she was covered in dirty, bloodied scrapes. Her goggles lay with cracked lenses haphazardly across her face, and her right wing bent at an unnatural angle."
    m "I noticed something small poking out of her right wing elbow. Upon closer inspection it was a bit of bone. I couldn't look any longer."
    "???" "Stand clear everyone!"
    m "The paramedics had arrived. They quickly put Adine's limp body onto a stretcher and carried her off."
    m "I swallowed the lump in my throat and ran over to Adine."
    m "Before I could make it to her, I was stopped by Sebastian."
    show sebastian normal b behind evalsmokeoverlay with dissolve
    c "Sebastian? What are you doing here?"
    Sb "Well, I was here on duty during the event, but now I've been tasked with keeping the crowds away from the medical professionals."
    c "Please, Sebastian. I need to see her and make sure she's okay."
    Sb disapproval b "Sorry, no can do. We have strict policies to ensure that the professionals can do their jobs."
    c "Can you at least tell me if she's alive?"
    Sb normal b "Yes, but you must stay here."
    hide sebastian with dissolve
    m "Sebastian walked over to the paramedics and shared a few brief words before returning to me."
    show sebastian drop b behind evalsmokeoverlay with dissolve
    c "Well?"
    Sb "She... {w}is alive. {w}There is a pulse, but it's faint. She has to go to the hospital immediately and will probably be put under an artificial coma."
    Sb normal b "They didn't promise she would live, [player_name], but she's alive at the moment."
    m "It took me a moment to process this information. While it was a relief that she was still alive, the thought of losing her in the future could not escape my mind."
    c "Thank you, Sebastian."
    if sebastianunplayed:
        Sb "All part of the job."
    else:
        Sb "My best wishes, [player_name]."
    Sb "Hey! That area is currently off limits!"
    hide sebastian with easeoutleft
    $ renpy.pause (1.0)
    hide evalsmokeoverlay
    show evalsmokeoverlayflip
    with dissolve
    m "The smoke started to shift and dissipate as I watched Adine limp body rushed to the hospital."
    m "Shaken and defeated, I decided to make my way back to my apartment."
    stop soundloop fadeout 2.0
    stop music fadeout 2.0
    scene black with dissolveslow
    play sound "fx/footsteps.mp3"
    $ renpy.pause (5.0)

#Post-crash content including an introduction to Remy (or not) and the hospital scene
label eval_adine4_changes_post_crash:
    #Instance where Remy is dead. Guarenteed failure
    if remydead:
        $ eval_ffg_bad_ending = True
        stop sound fadeout 2.0
        scene o1 with dissolveslow
        jump eval_adine4_changes_apartment

    Ry sad "[player_name]."
    scene evalpark1
    show remy sad
    with dissolveslow
    $ remystatus = "good" #DELETE LATER
    $ annastatus = "good" #DELETE LATER

    #Remy can only have a good/neutral status or be dead
    play music "mx/forge.ogg" fadein 2.0
    Ry "Did you see it?"
    c "Yeah... {w}I was there for the whole thing."
    Ry "What happened?"

    menu:
        "[[Tell him about the incident.]":
            c "She had sprained her wing during one of our practice sessions. I tried to stop her from participating but{w=0.5}.{w=0.5}.{w=0.5}. she wouldn't listen."
            Ry angry "You let her join knowing full well that something like this may have happened?"
            c "Remy, I-{w=0.3}{nw}"
            Ry "Why would you not try to stop her? Why would you not try to do everything in your power to make sure she didn't enter that damn competition?" with hpunch
            c "She said she was worthless, Remy. She told me that she felt as if she was wasting her life away working as a waitress. She wanted to do more, and this was the only opportunity she felt she had."
            Ry "I{w=0.2}.{w=0.2}.{w=0.2}."
            $ renpy.pause (0.5)
            Ry sad "I guess I would have let her go, too."
        
        "[[Feign ignorance.]":
            c "I'm not sure. One moment she was in the air, and the next she was falling headfirst into the ground. It looks like she got hurt during the performance."

    Ry "I just wish I could have done more to help her. To prevent any of this from happening."
    c "I talked to Sebastian. She is still alive, but unstable."
    Ry shy "She is? I... I thought she was dead."
    c "Her body was not a pretty sight."
    Ry "I... wow. I thought we lost her. I'm so glad she's still here with us."
    c "I was as relieved as you are. Now we can only hope for the best."
    Ry "Can we sit down for a moment? I need some time to process all of this."
    c "Sure, I couldn't agree more."
    m "Together, we made our way over to a park bench and rested."
    scene black with dissolveslow
    m "I closed my eyes and tried to relax. Taking deep breaths in{w=0.5}.{w=0.5}.{w=0.5}. and out."
    m "Remy laid quietly on the soft grass by my feet, his side brushing up against me with the rise of each breath."
    m "I soon found myself drifting out of consciousness as sleep overtook my body."
    $ renpy.pause (4.0)
    Ry "[player_name]?"
    scene evalpark2
    show remy normal
    with dissolveslow
    m "I groggily wiped my eyes."
    c "Did I fall asleep?"
    Ry "We both did. I think we needed a little nap to recover."
    c "I guess so."
    Ry "Judging from the night sky, we must have been out for hours. We might be able to visit Adine now."
    c "You think so?"
    Ry "Yes. The local hospital is quite leniant when it comes to visitors."
    c "Sure, let's go."

    #Start of hospital scene
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene evalhospitalhall with dissolveslow
    show remy look with dissolve
    Ry "Now, to find Adine..."
    
    #More dramatic without music?
    #play music "mx/pier.mp3" fadein 2.0
    play sound "fx/hallwalk.mp3" fadein 3.0
    $ renpy.pause (3.0)
    stop sound
    if annastatus == "good" and not annadead:
        $ eval_ffg_ch4_character = "Anna"
        An "Are you two lost?"
        show remy at right with move
        show anna normal b flip at left with easeinleft
        c "Oh, hey Anna!"
        An "What are you two doing here?"
        c "We're here to see Adine."
        An "Oh, her? You know, I'm not supposed to let her have any visitors yet."
        An smirk b flip "But for you two lovebirds, I guess I can make it happen."
        Ry shy "Anna, it isn't like that..."
        An "Then I guess you don't need my help. I'll be on my way then."
        show anna smirk b
        $ renpy.pause (0.3)
        show anna smirk b at Position(xpos = -0.2) with move
        Ry look "Wait, please."
        show anna smirk b flip
        $ renpy.pause (0.3)
        An normal b flip "Fine then. Come with me before I change my mind."
        show anna normal b
        $ renpy.pause (0.3)
        hide anna with easeoutleft
        hide remy with easeoutleft
        scene black with dissolveslow
        play sound "fx/hallwalk.mp3"
        $ renpy.pause (3.5)
        stop sound fadeout 2.0
        $ renpy.pause (2.1)
        play sound "fx/door/opendoorslow.ogg"
        $ renpy.pause (3.5)
        play soundloop "fx/heartrate.mp3" fadein 2.0
        scene evalhospitalroom with dissolveslow
        show remy normal at right
        show anna normal b flip at left
        with dissolve
        $ renpy.pause (0.5)
        c "Thank you, Anna."
        An "Don't mention it."
        show anna normal b
        $ renpy.pause (0.3)
        show anna normal b at Position (xpos = -0.2) with move
        $ renpy.pause (0.6)
        show anna normal b flip
        $ renpy.pause (0.4)
        An smirk b flip "Seriously, though. If anyone caught me doing this, I would be in serious trouble."
        Ry look "{size=-5}Not like you aren't already.{/size}"
        An disgust b flip "Shut it, Remy."
        show anna normal b
        $ renpy.pause (0.3)
        hide anna with easeoutleft
        play sound "fx/door/door_close.wav"
        show remy sad with dissolve
        show remy sad at center with move
    else:
        $ eval_ffg_ch4_character = "Sebastian"
        Sb normal b "[player_name]?"
        show remy normal at right with move
        show sebastian normal b flip at left with easeinleft
        Sb "What are you two doing here?"
        c "We're here to see Adine."
        Sb "Adine? I don't think she should be receiving any guests at the moment. They just finished her surgery about an hour ago. She needs rest."
        Ry "Sebastian... please. I'm just so worried about her."
        Sb shy b flip "Well, I..."
        $ renpy.pause (0.5)
        if not sebastianunplayed:
            Sb normal b flip "Alright, you can come with me, but tell nobody about this or I might get fired."
            c "Our lips are sealed."
        else:
            Sb normal b flip "Fine, I trust you well enough to not tell anyone."
            Ry "We won't, I promise."
        show sebastian normal b
        $ renpy.pause (0.3)
        hide sebastian with easeoutleft
        hide remy with easeoutleft
        scene black with dissolveslow
        play sound "fx/hallwalk.mp3"
        $ renpy.pause (3.5)
        stop sound fadeout 2.0
        $ renpy.pause (2.1)
        play sound "fx/door/opendoorslow.ogg"
        $ renpy.pause (3.5)
        play soundloop "fx/heartrate.mp3" fadein 2.0
        scene testingroom with dissolveslow
        show remy normal at right
        show sebastian normal b flip at left
        with dissolve
        $ renpy.pause (0.5)
        c "Thank you, Sebastian."
        Sb "Anytime."
        show sebastian sad b
        $ renpy.pause (0.3)
        hide sebastian with easeoutleft
        play sound "fx/door/door_close.wav"
        show remy sad at center with move
    
    Ry sad "Look at her, the poor thing."
    hide remy with dissolve
    m "Remy made his way over to the bed where Adine lay. He rested his paw against her chest, having it slowly rise and fall with each of her short breaths."
    m "I joined his side and placed my hand on her body as well, feeling the faint bumps of her heart in her chest."
    m "The wing that had taken the impact of the fall was bandaged tightly to the front of her body, and she was covered with small bruises and abrasions."

    if remystatus == "good":
        m "Remy slid his paw over my hand, and for a few moments, the two of us sat motionless."
    else:
        m "Remy gently laid his muzzle across Adine's uninjured chest and lightly sighed."
    
    Ry sad "I... {w}I just wish I could have been there to help, is all."
    c "Remy..."
    
    if not remy3unplayed and remystatus == "good":
        Ry sad "I feel terrible. I distanced her from my life for so long because of Amelia. I couldn't handle the pain."
        Ry sad "She tried, [player_name]. She tried to reach out to me. But I ignored her, and look where that brought us now."
        Ry sad "Maybe all of this is my fault in some way."
        c "Remy, there is no way in which your actions of the past could have predicted this outcome. You can't blame yourself for her fate."
        $ renpy.pause(0.5)
        Ry sad "I guess so."
    else:
        Ry sad "I feel terrible. I distanced her from my life for so long because of..."
        m "His words trailed off."
        Ry sad "Nevermind, it doesn't matter, anyways."
    
    m "Adine stirred slightly in her sleep, and we moved away from her bed."
    show remy sad with dissolve

    Ry sad "Let's go, [player_name]. I don't think there's much else for us to do."

    menu:
        "You're probably right":
            c "You're probably right."
            Ry "Would you like me to walk back to your apartment with you?"

            label eval_adine4_stay_rethink:
                pass

            menu:
                "Sure.":
                    c "That's very nice of you, Remy. I would love to."
                    Ry normal "Okay, let's go then."
                
                "No thank you.":
                    c "That's okay, Remy. I'm sure you have other things to do."
                    Ry "Oh, alright. Let's go then."

            m "I glanced at Adine one last time before the two of us made our way back into the hallway."
            hide remy with dissolve
            play sound "fx/door/opendoorslow.ogg"
            $ renpy.pause (3.5)
            scene black with dissolveslow
            play sound "fx/door/door_close.wav"
            stop soundloop fadeout 4.0
            $ renpy.pause (4.0)
            jump eval_adine4_changes_apartment
    
    "I'd like to stay here.":
        c "I think I'm going to stay here for the night, Remy. I don't want to leave quite yet."
        Ry look "[player_name], I'd love to do the same, but we aren't supposed to be here in the first place."
        Ry "[eval_ffg_ch4_character_met] wanted us to promise that we wouldn't get caught."

        menu:
            "[[Insist.]":
                pass
            
            "[[Agree to leave.]":
                c "I guess you're right. I don't want anyone getting in trouble."
                Ry normal "We can always check back tomorrow, too. Listen to her heartrate."
                $ renpy.pause (4.5)
                c "I guess it is quite stable."
                Ry "Would you like me to walk back to your apartment with you?"
                jump eval_adine4_stay_rethink

        c "Despite whatever consequences may arise, I'm staying here, Remy."
        Ry "I guess I can't stop you. I think I'm going to leave for the night and check back in tomorrow, instead."
        c "I understand, Remy. See you around."
        Ry normal "Goodnight, [player_name]. Sleep well, I guess."
        hide remy with easeoutleft
        play sound "fx/door/opendoorslow.ogg"
        $ renpy.pause (3.5)
        play sound "fx/door/door_close.wav"
        $ renpy.pause (4.0)

        label eval_adine4_changes_stay_options:
            pass

        menu:
            c "(What now?)"

            "[[Go back to Adine.]" if not eval_ffg_ch4_tickle and adinestatus == "good":
                m "I decided to make my way back to Adine's bedside, standing over her bandaged body."
                m "She had shifted slightly since the last time I had seen her, and her tail seemed dangerously close to slipping off the bed."

                "[[Adjust her tail.]":
                    m "Carefully, I readjusted her tail back towards the center of the bed. It was much heavier than I thought, and I struggled to keep a good grip on her smooth scales."
                
                "[[Leave her tail alone.]":
                    c "(I shouldn't risk hurting her.)"
                
                m "I gently rested my hand against Adine's uninjured side and, subconsciously, lightly rubbed her scales." #without thinking?
                m "A faint murmur arose from the dragoness, and her lips weakly parted for a moment before returning to normal."
                c "(Maybe she's ticklish there?)"
                $ eval_ffg_ch4_tickle = True
                jump eval_adine4_changes_stay_options
            
            "[[Call it a night.]":
                m "Looking at the pale moonlight outside the window, I decided to get some sleep before morning came."
                m "There weren't many places in the room to sleep. In the end, I designnated a chair in the corner of the room as my temporary sleeping arrangement."
                m "As I sat down, exhaustion washed over my body. With the beeping of the heart monitor, I closed my eyes and drifted off to sleep."
                stop soundloop fadeout 4.0
                scene black with dissolveslow
                jump eval_adine4_changes_hospital_wakeup
            
            "[[Return to your apartment.]":
                m "Recalling what Remy had said, I decided it would be in my best interest to return to my apartment before anyone came to check on Adine."
                if eval_ffg_ch4_tickle:
                    m "She had reacted to my touch, which made me feel safer leaving her for the night."
                play sound "fx/door/opendoorslow.ogg"
                m "Glancing at Adine one last time over my shoulder, I closed the door and made my way back to my apartment."
                play sound "fx/door/door_close.wav"
                $ renpy.pause (4.0)
                jump eval_adine4_changes_apartment

#Post-hospital content if you decide to stay at the hospital
label eval_adine4_changes_hospital_wakeup:
    pass

#Post-hospotal content if you decide to leave the hospital at any point or Remy is dead
label eval_adine4_changes_apartment:
    pass