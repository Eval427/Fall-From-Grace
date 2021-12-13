#I can't believe I'm actually writing another mod with even more ambitions than the first. Here we go...
#Initial concepts which I am 100% sure will change:
    # Adine almost kills herself
    # Help her recover
#Perfect, let's write 100k+ words.

#Lawyer wyvern = Adine mom

#General mod format:
    #Start out with the crash, continue with full adine chapters. 1-2 options per chapter + guarenteed plot
    #3-5 chapters, depending how much I can headcannon

#Concepts for activities:
    #More magazines
    #Extended beach scene
        #Rock skipping
        #Walk along the shoreline
    #Peaceful fireworks
    #Philosophy
    #Hike (waddling)
    #Some sort of crafts?
    #Probably discussions of Adine's interests and beliefs
    #Something
    #Mess around with the idea of Adine being a human fanfic writer
    #Adine is a painter?
    #Adine shopping
    #Cooking
    #Swimming
    #Deep forst exploration
        #Explore ancient dragon civilizations? Uncover something? Who knows
    #Makeshift vehicle making
    #Mud sledding
    #ORPHANAGE
    #Cinema - Movie sucks though, so you leave
    #Ice cream
    #More truth or dare (cheap wine that Remy stocked)
    #Shower scene 2.0 - This one is probably a post-content after one of the other activities
        #Spur of the moment kiss leaves you soaked.
        #Decide that your clothes are already wet, so there's nothing to lose so you embrace her further.
        #Nothing implied (I don't think, need to start writing this to figure that stuff out.)
        #Post-shower you come out borrowing one of Adine's towels as your clothes dry.
            #Does Adine have towels? Probably not, so she can grab one from somewhere, or this is dragon sweat 2.0

#Random concepts throughout the mod
    #Stolen purse while taking a walk? - Could be a quest to find and get it back with the police?

#Cool idea: You actually have 2 options for the Anna thing with Adine: Tell Adine why Anna is willing to pay for her hospital bills or not.
#If you do, Adine is concerned and angry. You have to comfort her otherwise she will reject the funds maybe?
#If you don't she will become extremely angry that you don't trust her enough, and this will either lead to very decreased mod mood points or
#Death in the hiking scene where she doesn't trust you and falls off a cliff

#After further thoughts, the idea above isn't very good, instead...

    #Lawyervern, headcannoned as Adine's mother, visits the area to check on Adine and her client (Anna)
    #There is some tension between the two regarding the fact that Adine didn't want to go to school like her parents wanted her to
    #Lawyervern implies that the reason she is in this situation is because she didn't follow her mother's wishes (seems harsh)

#Chapters:
    #Chapter 1: Move in day
    #Chapter 2: Lawyervern visits
    #Chapter 3: Extended shower scene
    #Chapter 4: Extended fireworks scene
    #Chapter 5 (secret): The second flight competition


init python:
    #Literally the most important variable in the entire mod. - Doubt this will be used lol
    eval_adine_mood = 0

    #Whether you are going on the mod pah (determined by first menu option)
    eval_ffg_mod_path = False

    #Whether you will get the bad ending or not
    eval_ffg_bad_ending = False

    #Who you met during the c4 date change to let you into the hospital room
    eval_ffg_ch4_character = ""

    #Whether you discover Adine is ticklish
    eval_ffg_ch4_tickle = False

    #When you left the hospital in Adine 4 - value of early, late, or sleep
    eval_ffg_ch4_hospital_leave = ""

    #Whether you romance Adine in chapter 5
    eval_ffg_ch5_romance = False

#Remove Remy's persistent survival. AKA, Remy can now die if his status is bad or abandoned despite having his good ending
label eval_anti_remy_persistence:
    if remystatus == "bad" or remystatus == "abandoned":
        jump eval_anti_remy_persistence_jump
    else:
        return

label eval_anti_remy_persistence_jump:
    jump eval_anti_remy_persistence_jump_return

label eval_remydeath_check:
    if remystatus == "abandoned" or remystatus == "bad":
        $ remydead = True
    return