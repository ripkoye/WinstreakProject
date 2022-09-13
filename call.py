import requests
import json
import sys, os

apiKey = ''
wins = ''

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


def read():
    global wins

    settingsFile = open(resource_path("settings.json"), 'r')
    dataPersonal = json.load(settingsFile)
    apiKey = dataPersonal['playerInfo']['API-Key']
    uuid = dataPersonal['playerInfo']['uuid']
    settingsFile.close()

    headers = {
    'API-Key': apiKey
    }

    #requests to the api (winstreak data and rate information)
    response = requests.get('https://api.hypixel.net/player?uuid='+uuid,headers=headers)
    #responserate = requests.get('https://api.hypixel.net/key', headers=headers)

    #making it readable
    data = response.json()

    #pull the information out from json
    wins = data['player']['stats']['Bedwars']['winstreak']
    print("success")

#function to write the information into the txt file for streamlabs to run
def write():
    f = open(resource_path("winstreak.txt"), "w")
    f.write("Winstreak: "+str(wins))
    f.close()




