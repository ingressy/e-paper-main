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
                if(i['battery']) <= "30":
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




warnBats()