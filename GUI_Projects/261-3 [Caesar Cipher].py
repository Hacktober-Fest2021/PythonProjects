from guietta import _, Gui, Quit

gui= Gui(
    ["Message: ",_, '__msg__'],
    [_,['Encrypt'], _],
    ["Encrypted Message: ", _, 'emsg'],
    [_, Quit, _]
    )

def cipheren(gui):
    message=  gui.msg
    index=0
    emsg=""
    while (index< len(message)):
        letter= message[index]
        emsg= emsg + (chr(ord(letter) +3))
        index+=1   
    gui.emsg= emsg


gui.Encrypt= cipheren

gui.run()

