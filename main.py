import requests
import json

uuid = '9621788a942d48bbbfb6f05484e4dca2'
headers = {
    'uuid': '9621788a942d48bbbfb6f05484e4dca2',
    'API-Key': '5434a1b3-6c62-4db5-8449-b6ab2109cb89',
}

response = requests.get('https://api.hypixel.net/player?uuid='+uuid,headers=headers)

data = response.json()

success = data['success']

wins = data['player']['stats']['Bedwars']['winstreak']

print(success)
print(response)

f = open("/Users/ripkoye/Desktop/WinstreakProject/winstreak.txt", "w")
f.write("Winstreak: "+str(wins))
f.close()