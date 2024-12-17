import requests, json,os
from dotenv import load_dotenv

# Discord Channel Webhook:
try:
    with open('../config.json', 'r') as config_file:
        config_data = json.load(config_file)

        # Roomdatabase File aus Config abrufen:
        roomdatabase = config_data['config'][0]['roomdatabase']
except FileNotFoundError:
    print("batts_webhook.py: Config file not found! PLease check the File!")
try:
    global webhook_url
    load_dotenv('../UNTIS-WRAPPER/.env')
    webhook_url = os.getenv('DCWEBHOOK')
except:
    print("batts_webhook.py: Get .env Error!")
# Vordefinineren der Variable, um Errors zu vermeiden:

def warnBats():
    # Für jeden Raum den Batteriestand abfragen:
    with open(f"../UNTIS-WRAPPER/{roomdatabase}", 'r') as file:
        data = json.load(file)

        for i in data['rooms']:
            if(i['enabled'][0]) == "t":
                if(i['battery']) <= "20":
                    displayName = (i['roomnumber'])
                    lowBatMsg = {
                        "username": "Display Status",
                        "avatar_url": "https://www.ionos.de/digitalguide/fileadmin/_processed_/b/e/csm_was-ist-ein-server-t_22a78122ca.webp",
                        "embeds": [ {
                            "title": "Achtung!",
                            "description": f"Das Display {displayName} muss aufgeladen werden! Aktueller Batteriestand: {i['battery']}%.",
                            "color": 16776960,
                        } ],
                    }
                    response = requests.post(webhook_url, json=lowBatMsg)
                    print(response.text)
            else:
                print(f"{i['roomnumber']} is not enabled! (Skipped)")
def connectionWarn(room,lastResponse):
    with open(f"../UNTIS-WRAPPER/{roomdatabase}",'r') as file:
        data = json.load(file)
        for i in data['rooms']:
            if i['roomnumber'] == room:
                lastBattStat = i['battery']
        connLostMsg = {
            "username": "Display Status",
            "avatar_url": "https://www.ionos.de/digitalguide/fileadmin/_processed_/b/e/csm_was-ist-ein-server-t_22a78122ca.webp",
            "embeds": [{
                "title": "Kritisch!",
                "description": f"Das Display {room} hat keinen Response mehr gegeben!",
                "color": 16711680,
                "fields": [{
                    "name": "Letzter Batteriestand:",
                    "value": lastBattStat,
                    "inline": True
                },
                {
                    "name": "Letzter Response:",
                    "value": lastResponse,
                    "inline": True
                }
                ]
            }]
        }
        response = requests.post(webhook_url, json=connLostMsg)


# warnBats soll jeden Tag nur einmal ausgeführt werden, sie geht einmal alles durch.
warnBats()
connectionWarn("2.311","23:16")
# Das sind nur Tests, diese Func in Server.py importieren bei gegebenen Events
