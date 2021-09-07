label eval_adine4_changes:
    menu:
        #Default path
        "[[Mention Amely.]":
            c "What about Amely? If something happened to you, how do you think they would explain to her that you just suddenly stopped showing up, huh?"
            jump eval_adine4_default_path
        
        #Modded path
        "[[Say nothing.]":
            Ad "Listen, [player_name]. I have to do this for myself. I have to prove to myself, my parents, and every other person who has doubted me my entire life that I can do this."
            c "Adine, what you are doing could have consequences. What if you hurt yourself even more?"
            Ad "You know what? If I keep having that mindset, I'll never do anything with my life. I will fly and do the best damn job I've ever done, and there's nothing you can do to stop me."
            hide adine with dissolve
            m "You didn't mention Amely. What does that mean?"