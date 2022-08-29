import requests
player = ''
headers = {
    'AUTHORIZATIONS': 'something',
}
response = requests.get('https://api.hypixel.net/'+player, headers=headers)

#wins = response['player']['stats']['wins']

wins = 2

f = open("/Users/ripkoye/Desktop/WinstreakProject/winstreak.txt", "w")
f.write("Winstreak: "+str(wins))
f.close()