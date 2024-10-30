import asyncio
from hbmqtt.broker import Broker

# Einfache Broker-Konfiguration ohne Authentifizierung und TLS
config = {
    'listeners': {
        'default': {
            'type': 'tcp',
            'bind': '0.0.0.0:1883',  # Standard MQTT-Port
        }
    },
    'sys_interval': 10,
    'topic-check': {
        'enabled': False  # Deaktiviert die Themenüberprüfung
    }
}

# Funktion zum Starten des Brokers
async def start_broker():
    broker = Broker(config)
    await broker.start()
    print("MQTT Broker gestartet.")

# Hauptfunktion für den Event-Loop
async def main():
    await start_broker()
    while True:
        await asyncio.sleep(1)  # Halte den Broker aktiv

if __name__ == "__main__":
    try:
        # Startet die Hauptfunktion im Event-Loop
        asyncio.run(main())
    except KeyboardInterrupt:
        print("MQTT Broker gestoppt.")
