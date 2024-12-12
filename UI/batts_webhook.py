import requests, json

# Discord Channel Webhook:
webhook_url = "https://discordapp.com/api/webhooks/1316828498849038346/ao7P6352CIRyxdCigP7GRjxtwJSAlRE9dBus0jD9P4gGjJl4wxNZ24_gXb_2GdHOQlsU"
try:
    with open('../config.json', 'r') as config_file:
        config_data = json.load(config_file)

        # Roomdatabase File aus Config abrufen:
        roomdatabase = config_data['config'][0]['roomdatabase']
except FileNotFoundError:
    print("batts_webhook.py: Config file not found! PLease check the File!")

# Vordefinineren der Varibale, um Errors zu vermeiden:

def warnBats():
    # Für jeden Raum den Batteriestand abfragen:
    with open((f"../UNTIS-WRAPPER/{roomdatabase}"), 'r') as file:
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