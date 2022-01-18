#That's right! Eval is downright insane and decided
#to add more chapters centered around everyone's favorite
#flyer! (I'm going to regret this, aren't I?)

label eval_ffg_ch6:
    #It's very possible that I do some sort of fancy transition here for chapter 6 and beyond. We'll see
    play sound "fx/door/doorbell.wav"
    $ renpy.pause (1.0)
    Ad normal hurt "The door's open. Come in!"
    play sound "fx/door/door_open.wav"
    scene adineapt at Pan ((300, 300), (128,300), 3.0)
    show adine normal hurt
    with dissolveslow
    Ad "Hello, [player_name]! Thanks for stopping by. There isn't much, but with this injured wing there's no way I'm carrying all of this alone."
    c "No problem. So, what do you need me to do?"
    Ad giggle hurt "Well, luckily for you I don't own many things, so this shouldn't take us all day."
    Ad normal hurt "I'll let you choose where we start and help you as much as I can."
    c "Sounds good to me."

    label eval_ffg_ch6_packmenu:
        menu:
            c "(Where should we pack?)"

            "Pack up the bathroom." if not eval_ffg_ch6_bathroom:
                jump eval_ffg_ch6_packbathroom
            
            "Pack up the closet." if not eval_ffg_ch6_closet:
                jump eval_ffg_ch6_packcloset
            
            "Pack up the bedroom." if not eval_ffg_ch6_bedroom:
                jump eval_ffg_ch6_packbedroom

label eval_ffg_ch6_packbathroom:
    eval_ffg_ch6_bathroom = True
    if not eval_ffg_ch6_closet and not eval_ffg_ch6_bedroom:
        c "Why don't we start in the bathroom first?"
    else:
        c "Why don't we do the bathroom next?"
    Ad "Sure! Don't forget to grab a box."
    m "I grabbed one of the empty boxes by the door and walked into Adine's bathroom."
    scene black with dissolvemed
    $ renpy.pause (1.0)
    #Potentially add a bg here? seems doubtful I'll find something fitting though
    m "The bathroom itself was quite small in size, taken up by a abnormally large shower."
    m "I placed down the box in the middle of the floor and started carefully packing Adine's shower belongings."

    menu:
        "[[Continue packing.]":
            pass
        
        "[[Ask about the shower.]":
            c "Hey Adine. Why is your shower so large?"
            Ad normal hurt "Well, as a flyer I need more room to maneuver around and stretch out my wings."
            c "I don't think the shower in my apartment is this big."
            Ad comtemplate hurt "Wait a minute... you have a good point. How big is it?"
            c "Probably about half the size of yours."
            Ad contemplate hurt "For the time, that should be adequate. I won't be getting dirty much anyways and, if necessary, there are public facilities I could visit."

    m "I carefully walked into the shower and grabbed every container. One container was a completely empty tube that read \"Scale Shiner\""
    c "Adine? Should I keep this?"
    Ad normal hurt "Of course! That stuff is expensive and there's still a little left."
    m "I placed it in the box and continued raiding the bathroom as Adine double and triple checked each drawer before deeming it free of her personal belongings."
    c "That should be it."
    if not eval_ffg_ch6_closet or not eval_ffg_ch6_bedroom:
        Ad normal hurt "Onto the next!"
        jump eval_ffg_ch6_packmenu
    else:
        Ad "That should be everywhere, [player_name]. You can load those boxes up on the cart next to my apartment door while I double check everything."
        c "You seem quite worried about leaving something behind."
        Ad "Well, I've never moved out before, and I really want to make sure I don't lose what little possessions I have."
        menu:
            "You should be less nervous.":
                c "You shouldn't stress too much about the little things like that, Adine. You've already checked everything more than once."
                Ad contemplate hurt "Maybe, but I still want to do it just to ease my mind."
            
            "That's understandable.":
                eval_adine6_mood += 1
                c "I understand that. When I was coming to the dragon world I was really nervous about leaving something important behind."