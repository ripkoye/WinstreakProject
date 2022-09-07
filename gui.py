#import all of tkinter and also updated widgets
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
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

imageWidth = 100
imageHeight = 50

is_on = False
onImage = Image.open('on.png')
onResized = onImage.resize((imageWidth,imageHeight))
on = ImageTk.PhotoImage(onResized)
offImage = Image.open('off.png')
offResized = offImage.resize((imageWidth,imageHeight))
off = ImageTk.PhotoImage(offResized)
buttonOnOff = Button(mainframe, image=on)


def switch():
    global is_on
    
    while True:
        if is_on:
            buttonOnOff.config(image = off)
            is_on = False
        else:
            buttonOnOff.config(image = on)
            is_on = True


buttonOnOff.config(image=off, command=switch, bd=0, width=imageWidth, height=imageHeight)
buttonOnOff.grid(row=1, column=0)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()