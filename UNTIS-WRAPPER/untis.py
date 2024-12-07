# needs an .env file with the login data
import datetime, os, webuntis.objects, json
from dotenv import load_dotenv

#loading data from the .env
load_dotenv()
SRV = os.getenv('SRV')
USR = os.getenv('USR')
PWD = os.getenv('PWD')
SHO = os.getenv('SHO')
USRA = os.getenv('USRA')

time = datetime.datetime.now()
chtime = (time.strftime("%H%M"))
chdate = (time.strftime("%Y-%m-%d"))
start = datetime.datetime.now()
end = start + datetime.timedelta(days=5)

def untis_get(raum):
    s = webuntis.Session(
        server=SRV,
        username=USR,
        password=PWD,
        school=SHO,
        useragent=USRA
    )
    s.login()
    if isinstance(s, str):
        print(f"Keine Daten von Raum ",{raum})
    elif isinstance(s, str):
        print(f"Fehlerhafte Daten von Raum", {raum})
    else:
        rooms = s.rooms().filter(name=raum)

        tt = s.timetable(room=rooms[0], start=start, end=end)
        tt = sorted(tt, key=lambda x: x.start)

        time_format_end = "%H%M"
        time_format_start = time_format_end
        time_format_date = "%Y-%m-%d"

        for po in tt:
            d = po.start.strftime(time_format_date)
            s = po.start.strftime(time_format_start)
            e = po.end.strftime(time_format_end)
            k = " ".join([k.name for k in po.klassen])
            try:
                t = " ".join([t.full_name for t in po.teachers])
            except IndexError:
                print(f"Fehler bei einem Eintrag einer Lehrkraft von Raum {raum}")
            r = " ".join([r.name for r in po.rooms])
            sub = " ".join([r.long_name for r in po.subjects])
            c = "(" + po.code + ")" if po.code is not None else ""

            if chtime < e:
                print(d, s + "-" + e, k, sub, t, r, c)
        print(f"Daten von Raum {raum} erhalten ...")

def main():
    #loading config file
    try:
        with open('../config.json', 'r') as config_file:
            config_data = json.load(config_file)

            #check a few things and do things
            for i in config_data['config']:
                if (i['enabled']) == "true":

                    roomdatabase = i['roomdatabase']

                    # load a json file with the rooms
                    # use an own file because dev stat ~yeah
                    try:
                        with open(roomdatabase, 'r') as file:
                            data = json.load(file)

                            # check if active stat
                            for i in data['rooms']:
                                if (i['enabled'][0]) == "t":
                                    print(i['roomnumber'])
                                elif (i['enabled'][0]) == "f":
                                    print(i['roomnumber'] + " is disabled")
                                    # do nothing here
                                else:
                                    print("ERROR: Reading Room Database! | " + i['roomnumber'])
                    except FileNotFoundError:
                        print("File Not Found - Please check the File!")
                else:
                    print("untis-wrapper disabled - Please enabled in config.json")
                    exit(0)
    except FileNotFoundError:
        print("File Not Found - Please check the File!")
if __name__ == "__main__":
    main()