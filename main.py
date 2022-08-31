import requests
import json

player = 'koearn'
headers = {
    'API-Key': '5434a1b3-6c62-4db5-8449-b6ab2109cb89',
    'uuid': '9621788a942d48bbbfb6f05484e4dca2'
}

response = requests.get('https://api.hypixel.net/player', headers=headers)

data = response.json()

success = data['success']
cause = data['cause']

#wins = data['GameTypes']['Bedwars']['player']['stats']['winstreak']

print(success)
print(cause)
print(response)
print(headers)

#f = open("/Users/ripkoye/Desktop/WinstreakProject/winstreak.txt", "w")
#f.write("Winstreak: "+str(wins))
#f.close()