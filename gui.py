#import all of tkinter and also updated widgets
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time
import threading
import call

#sets up main application window
root = Tk()
root.title("Winstreak Counter GUI")

#creating a content frame (frame widget, hold content of user interface)
#we do this because it'll allow us to control the background color and allow for more themed widgets
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=10, row=10, sticky=(N, W, E, S))
root.columnconfigure(10, weight=1)
root.rowconfigure(10, weight=1)
root.geometry('600x400')

f = open('winstreak.txt', 'r')
#store the information into a variable
winstreak = StringVar(mainframe)
winstreak.set(f.read())
#creates a winstreaklabel
winstreaklabel = Label(mainframe,width=10)
winstreaklabel.grid()
winstreaklabel['textvariable'] = winstreak
#assigns the text to the variable named winstreak
f.close()

imageWidth = 200
imageHeight = 100

is_on = False
onImage = Image.open('on.png')
onResized = onImage.resize((imageWidth,imageHeight))
on = ImageTk.PhotoImage(onResized)
offImage = Image.open('off.png')
offResized = offImage.resize((imageWidth,imageHeight))
off = ImageTk.PhotoImage(offResized)

buttonOnOff = Button(mainframe, image=on)

def keepRequesting():
    while is_on:
        print("Threading...")
        call.read()
        call.write()
        time.sleep(10)

def switch():
    global is_on
    
    if is_on:
        buttonOnOff.config(image = off)
        is_on = False

    else:
        buttonOnOff.config(image = on)
        is_on = True
        threading.Thread(target=keepRequesting, daemon=True).start()


buttonOnOff.config(image=off, command=switch, bd=0, width=imageWidth, height=imageHeight)
buttonOnOff.grid(row=1, column=0)

root.mainloop()

