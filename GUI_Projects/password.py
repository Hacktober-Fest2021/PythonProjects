import random
from guietta import _, Gui, Quit

gui = Gui (
    ["Length of the password ", '__n__'],
    [   ['Generate'], _],
    ["Password = ",'password']
)

chars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+}{"

def password(gui):
    n= int(gui.n)
    password=""
    for i in range(n+1):
        password += random.choice(chars)
    gui.password= password

gui.Generate= password

gui.run()
