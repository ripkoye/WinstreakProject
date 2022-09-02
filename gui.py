#import all of tkinter and also updated widgets
from tkinter import *
from tkinter import ttk
import main

#sets up main application window
root = Tk()
root.title("Winstreak Counter GUI")

#creating a content frame (frame widget, hold content of user interface)
#we do this because it'll allow us to control the background color and allow for more themed widgets
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=10, row=10, sticky=(N, W, E, S))
root.columnconfigure(10, weight=1)
root.rowconfigure(10, weight=1)

f = open('/Users/ripkoye/Desktop/WinstreakProject/winstreak.txt', 'r')
#store the information into a variable
winstreak = StringVar(mainframe)
winstreak.set(f.read())
#creates a winstreaklabel
winstreaklabel = ttk.Label(mainframe,width=20, padding='5 5 5 5')
winstreaklabel.grid()
winstreaklabel['textvariable'] = winstreak
#assigns the text to the variable named winstreak
f.close()

is_on = True

on = PhotoImage(file='on.png')
off = PhotoImage(file='off.png')
buttonOnOff = ttk.Button(mainframe, image=on, width=0.5, padding='5 5 5 5')

def switch():
    global is_on

    if is_on:
        buttonOnOff.config(image = off)
        is_on = False
    else:
        buttonOnOff.config(image = on)
        is_on = True

buttonOnOff.config(command=switch())
buttonOnOff.grid()


root.mainloop()