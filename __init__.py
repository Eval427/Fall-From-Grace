import renpy
import renpy.ast as ast
import renpy.display.im as im
import renpy.parser as parser

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod): 
    def mod_info(self):
        return ("Fall from Grace", "0.1.0", "Eval")
    
    def mod_load(self):
        ml = modinfo.get_mods()["MagmaLink"].import_ml()
        
        #Adine 4 hooks
        
        #Better music transition
        ml.find_label("adine4") \
            .search_say("Do you want them to see you in this condition and judge you based on that rather than when you're at your best?", 400) \
            .hook_to("eval_adine4_music") \
            .search_say("What if something goes wrong, though? You don't want to be in that position.") \
            .link_from("eval_adine4_music_end")
        
        #Content start
        ml.find_label("adine4") \
            .search_say("I don't want to wonder if I'll ever amount to anything more than a waitress. I want to be able to follow my dream, and I don't want to wait another year to find out.", 400) \
            .hook_to("eval_adine4_changes") \
            .search_say("What about Amely? If something happened to you, how do you think they would explain to her that you just suddenly stopped showing up, huh?") \
            .link_from("eval_adine4_default_path")

        #Let Remy die again
        #ml.find_label("c4library") \
        #    .search_python("renpy.pause (3.3)") \
        #    .hook_call_to("eval_anti_remy_persistence")

        #remy_conditional = ml.find_label("c4library").search_if("remystatus == \"good\"")
         
        #remy_conditional.branch("persistent.remygoodending == True") \
        #    .hook_call_to("eval_anti_remy_persistence")
        
        #remy_conditional.branch_else() \
        #    .hook_to("eval_anti_remy_persistence_jump") \
        
        #ml.find_label("c4postsections") \
        #    .search_show("sebastian normal b") \
        #    .hook_call_to("eval_remydeath_check") \
        
        #ml.find_label("chapter5") \
        #    .hook_call_to("eval_remydeath_check")

        #Chapter 5 phone call
        ml.find_label("chapter5") \
            .search_python("chapter5unplayed = False") \
            .hook_to("eval_adine5_phonecall") \
            .search_python("loremavailable = False") \
            .link_from("eval_adine5_phonecall_end")
        
        #Adine 5 changes
        ml.find_label("adine5") \
            .hook_to("eval_adine5_fireworks")
        
    def mod_complete(self):
        pass