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
        
        #Adine 4 hook
        ml.find_label("adine4") \
            .search_say("I don't want to wonder if I'll ever amount to anything more than a waitress. I want to be able to follow my dream, and I don't want to wait another year to find out.", 400) \
            .hook_to("eval_adine4_changes") \
            .search_say("What about Amely? If something happened to you, how do you think they would explain to her that you just suddenly stopped showing up, huh?") \
            .link_from("eval_adine4_default_path")
    
    def mod_complete(self):
        pass