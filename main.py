import requests
import json

uuid = '9621788a942d48bbbfb6f05484e4dca2'
headers = {
    'API-Key': '5434a1b3-6c62-4db5-8449-b6ab2109cb89',
}

#setting up the variables and calling it once
response = requests.get('https://api.hypixel.net/player?uuid='+uuid,headers=headers)
responserate = requests.get('https://api.hypixel.net/key', headers=headers)

data = response.json()
datarate = responserate.json()
success = data['success']
wins = data['player']['stats']['Bedwars']['winstreak']

def read():
    #requests to the api (winstreak data and rate information)
    response = requests.get('https://api.hypixel.net/player?uuid='+uuid,headers=headers)
    responserate = requests.get('https://api.hypixel.net/key', headers=headers)

    #making it readable
    data = response.json()
    datarate = responserate.json()

    #pull the information out from json
    success = data['success']
    wins = data['player']['stats']['Bedwars']['winstreak']

#function to write the information into the txt file for streamlabs to run
def write():
    f = open("/Users/ripkoye/Desktop/WinstreakProject/winstreak.txt", "w")
    f.write("Winstreak: "+str(wins))
    f.close()


#calling and showing response
write()
print(success)
print(response)
print(datarate)

