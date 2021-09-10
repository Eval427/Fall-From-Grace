label eval_adine4_music:
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    Ad disappoint b "I... just have to try, you know?"
    play music "mx/outpost.mp3" fadein 1.0
    jump eval_adine4_music_end

label eval_adine4_changes:
    menu:
        #Default path
        "[[Mention Amely.]":
            c "What about Amely? If something happened to you, how do you think they would explain to her that you just suddenly stopped showing up, huh?"
            jump eval_adine4_default_path
        
        #Modded path
        "[[Say nothing.]":
            Ad "Listen, [player_name]. I have to do this for myself. I have to prove to myself, my parents, and every other person who has doubted me my entire life that I can do this."
            c "Adine, what you are doing could have consequences. What if you hurt yourself? Or worse..."
            Ad "You know what? If I keep having that mindset, I'll never do anything with my life. I will fly and do the best damn job I've ever done, and there's nothing you can do to stop me."
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
            m "I nervously glanced up at the stage, spotting Adine fiddling with some sort of device on it."
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
            if len(adinestagename) > 1:
                m "With grim determination, she gained even more altitude and started moving in calculated motions. Soon, smoke formed the letter [adinestagename[0]]."
                c "(Is she writing out her stage name?)"
                if len(adinestagename) > 7:
                    c "(That's quite a long thing to write out with smoke.)"
                "However, while working on the letter [adinestagename[1]], her body sharply twisted and Adine quickly started loosing altitude."
                
            else:
                m "With grim determination, she gained even more altitude and started moving in calculated motions. Soon, smoke formed the letter [adinestagename[0]]."
                c "(I'm glad I kept her stage name short.)"
                m "However, upon finishing the letter, her body sharply twisted and Adine quickly started loosing altitude."
            m "The crowd gasped, but with some difficulty Adine regained her composure." #Get rid of this
            m "Seeming to think it was part of the performance, the dragons cheered and applauded." #Or this
            m "Adine once again started to ascend back into the air creating circles in the air which gradually got smaller and smaller."
            c "(This is it. This is her special move.)"
            m "As her circles became tiny, she suddenly tucked in her wings and went into a nosedive through the circles, disrupting the smoke in beautiful patterns."
            m "She descended quickly, and as she unfurled her wings to stop her downward momentum, she screamed in pain and lost her balance."
            m "She had lost control. All I could do was watch as Adine desperately attempt to correct herself as she came closer and closer to th-{w=1.0}{nw}"
            stop music
            play sound "fx/adinecrash.mp3"
            scene black with Shake ((0, 0, 0, 0), 2, dist=50)
            m "I couldn't watch. I shut my eyes before Adine hit the ground with a horrifying thud."
            #When adine crashes, have a smoke overlay since the smoke device will burst