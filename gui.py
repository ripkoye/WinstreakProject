#import all of tkinter and also updated widgets
from re import L
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time
import threading
import call
import json
import os, sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

settingsFile = open(resource_path("settings.json"), 'r')
data = json.load(settingsFile)
apiKey = data['playerInfo']['API-Key']
uuid = data['playerInfo']['uuid']
settingsFile.close()

#sets up main application window
root = Tk()
root.title("Winstreak Counter GUI")

#creating a content frame (frame widget, hold content of user interface)
#we do this because it'll allow us to control the background color and allow for more themed widgets
mainframe = ttk.Frame(root)
mainframe.grid(column=10, row=10, sticky=(N, W, E, S))
root.columnconfigure(10, weight=1)
root.rowconfigure(10, weight=1)
root.geometry('600x400')

f = open(resource_path('winstreak.txt'), 'r')
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
onImage = Image.open(resource_path('on.png'))
onResized = onImage.resize((imageWidth,imageHeight))
on = ImageTk.PhotoImage(onResized)
offImage = Image.open(resource_path('off.png'))
offResized = offImage.resize((imageWidth,imageHeight))
off = ImageTk.PhotoImage(offResized)

buttonOnOff = Button(mainframe, image=on)

def keepRequesting():
    global winstreak
    while is_on:
        call.read()
        call.write()
        with open(resource_path("winstreak.txt"), 'r') as outfile:
            winstreak.set(outfile.read())
        time.sleep(10)

def switch():
    global is_on
    
    if is_on:
        buttonOnOff.config(image = off)
        is_on = False

    else:
        buttonOnOff.config(image = on)
        is_on = True
        call.read()
        threading.Thread(target=keepRequesting, daemon=True).start()


buttonOnOff.config(image=off, command=switch, bd=0, width=imageWidth, height=imageHeight)
buttonOnOff.grid(row=1, column=0)

def showWidget():
    apiKeyInput.grid()
    uuidInput.grid()
    apiKeyInput.insert(0, apiKey)
    uuidInput.insert(0, uuid)
    buttonSave.grid()
    buttonShow.config(text='Hide',command=hideWidget)
    
def hideWidget():
    apiKeyInput.grid_remove()
    uuidInput.grid_remove()
    buttonSave.grid_remove()
    buttonShow.config(text="Show", command=showWidget)

def changeJson():
    global uuid, apiKey
    uuid = uuidInput.get()
    apiKey = apiKeyInput.get()

    jsonWrite ={
        "playerInfo":{
            "uuid": uuid,
            "API-Key": apiKey
        }
    }

    infoJson = json.dumps(jsonWrite)
    with open(resource_path("settings.json"), "w") as outfile:
        outfile.write(infoJson)
    call.read()

buttonShow = Button(mainframe, text="Show", command=showWidget)
buttonShow.grid(row=2,column=1)

apiKeyInput = Entry(mainframe, textvariable=apiKey)
apiKeyInput.grid(row=3, column=1)
apiKeyInput.grid_remove()

uuidInput = Entry(mainframe, textvariable=uuid)
uuidInput.grid(row=4, column=1)
uuidInput.grid_remove()

uuidLabel = Label(mainframe, text='uuid')
uuidLabel.grid(row=4, column=0)

apiKeyLabel = Label(mainframe, text="Api-Key")
apiKeyLabel.grid(row=3, column=0)

buttonSave = Button(mainframe, text='Save', command=changeJson)
buttonSave.grid(row=5, column=1)
buttonSave.grid_remove()

root.mainloop()

#uuid 9621788a942d48bbbfb6f05484e4dca2
#apikey 5434a1b3-6c62-4db5-8449-b6ab2109cb89

{
    "playerInfo":{
        "uuid": "",
        "API-Key": ""
    }
}