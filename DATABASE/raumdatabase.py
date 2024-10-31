import json
from datetime import datetime

class RaumManager:
    def __init__(self, filename='raeume.json'):
        self.filename = filename
        self.data = self._load_data()

    def _load_data(self):
        """Lädt die JSON-Daten aus der Datei. Falls die Datei nicht existiert, wird eine leere Liste zurückgegeben."""
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def _save_data(self):
        """Speichert die Daten in der JSON-Datei."""
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_raum(self, raumname, mac, secret):
        """Fügt einen neuen Raum hinzu oder aktualisiert einen bestehenden Raum basierend auf dem Raumnamen."""
        raum = next((r for r in self.data if r['Raumname'] == raumname), None)
        if raum is None:
            # Neuen Raum hinzufügen
            raum = {
                'Raumname': raumname,
                'MAC-Adresse': mac,
                'Secret': secret,
                'LastSeen': datetime.now().isoformat(),
                'LastDeepSleep': None  # Anfangswert auf None gesetzt
            }
            self.data.append(raum)
        else:
            # Raum aktualisieren
            raum['MAC-Adresse'] = mac
            raum['Secret'] = secret
            raum['LastSeen'] = datetime.now().isoformat()

        self._save_data()

    def update_last_seen(self, raumname):
        """Aktualisiert das LastSeen-Datum eines Raums anhand des Raumnamens."""
        raum = next((r for r in self.data if r['Raumname'] == raumname), None)
        if raum:
            raum['LastSeen'] = datetime.now().isoformat()
            self._save_data()
        else:
            print("Raum nicht gefunden.")

    def update_last_deep_sleep(self, raumname, minutes):
        """Aktualisiert die Zeit des letzten Tiefschlafs (in Minuten) eines Raums anhand des Raumnamens."""
        raum = next((r for r in self.data if r['Raumname'] == raumname), None)
        if raum:
            raum['LastDeepSleep'] = minutes
            self._save_data()
        else:
            print("Raum nicht gefunden.")

    def get_raum(self, raumname):
        """Gibt die Raumdaten anhand des Raumnamens zurück."""
        return next((r for r in self.data if r['Raumname'] == raumname), None)