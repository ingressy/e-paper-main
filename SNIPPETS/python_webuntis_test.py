import webuntis
from datetime import datetime

# WebUntis Login-Daten
school = 'TBZ+Mitte+Bremen'  # Name deiner Schule (wie in der WebUntis-URL)
username = 'dummy3'  # Dein WebUntis-Benutzername
password = 'NewShit24!'  # Dein WebUntis-Passwort
server = 'https://tipo.webuntis.com'  # WebUntis-Server (wie in der URL)

# Raumname oder Raumnummer (Beispiel: "101" für Raum 101)
room_name = '2.311'

# Verbinde dich mit WebUntis
session = webuntis.Session(
    server=server,
    username=username,
    password=password,
    school=school,
    useragent='Python WebUntis API Client'
)

try:
    # Einloggen
    session.login()

    # Hol dir das aktuelle Datum
    today = datetime.today()

    # Suche nach dem Raum
    rooms = session.rooms()
    room = next((r for r in rooms if r.name == room_name), None)
    #print(rooms)
    
    if room is None:
        print(f"Raum {room_name} nicht gefunden.")
        session.logout()
        exit()

    # Hol dir den Stundenplan für den Raum am heutigen Tag
    timetable = session.timetable(room=room, start=today, end=today)

    if not timetable:
        print(f"Keine Stunden für Raum {room_name} am {today.strftime('%Y-%m-%d')}.")
    else:
        print(f"Stundenplan für Raum {room_name} am {today.strftime('%Y-%m-%d')}:")
        for lesson in timetable:
            start_time = lesson.start.strftime('%H:%M')
            end_time = lesson.end.strftime('%H:%M')
            subject = lesson.subjects[0].name if lesson.subjects else 'Kein Fach'
            teacher = lesson.teachers[0].name if lesson.teachers else 'Kein Lehrer'
            print(f"{start_time} - {end_time}: {subject} mit {teacher}")

except Exception as e:
    print(f"Fehler beim Abrufen des Stundenplans: {e}")

finally:
    # Sitzung beenden
    session.logout()
