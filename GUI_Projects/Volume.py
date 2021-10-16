from guietta import _, Gui, Quit
import random

gui= Gui(
    [_,"Dice",_],
    [_, ["Roll"], _],
    [_, 'number', _],
    [_, Quit, _]
    )

def rolldie(gui):
    n= random.randint(1,6)
    gui.number= n

gui.Roll=rolldie

gui.run()

