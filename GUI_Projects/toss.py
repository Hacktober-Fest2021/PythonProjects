from guietta import _, Gui, Quit
import random

gui= Gui(
    [_,"Coin Toss",_],
    [_, ["Toss"], _],
    [_, 'number', _],
    [_, Quit, _]
    )

def roll(gui):
    n= random.randint(1,2)
    if n==1:
       gui.number = "Heads"
    else:
        gui.number= "Tails"

gui.Toss=roll

gui.run()

