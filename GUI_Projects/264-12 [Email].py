from guietta import _, Gui, Quit

#defining the interface
gui = Gui(

  [  "Info: ", _, '__info__'  ],
  [_, ['Find'], _],
  [  _, Quit, _ ],
  ["Email Server: ", _, 'mailserver'],
  ["Sent on: ", _, 'date_time'])


def finder(gui):
    info= gui.info #declaring inputs 
    start= info.find("@")+1 
    end= info.find("com")+4
    mailserver= info[start:end] #mailserver 

    start=end
    end=len(info)
    date_time= info[start:end] #date_time

    #passing results to gui interface 
    gui.mailserver= mailserver
    gui.date_time= date_time

gui.Find= finder

gui.run()
