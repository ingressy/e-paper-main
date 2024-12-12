# needs a filled config.json file with the login data
# you find the file in the main folder of the server project
#by ingressy

import datetime, webuntis.objects, json
from untis2imagegen import untis2imagegen

#time things idk
time = datetime.datetime.now()
chtime = (time.strftime("%H%M"))
chdate = (time.strftime("%Y-%m-%d"))
start = datetime.datetime.now()
end = start + datetime.timedelta(days=0)

def untis_get(raum):
    #try to open the config json file
    try:
        with open('../config.json', 'r') as config_file:
            config_data = json.load(config_file)

            #login by the untis api
            s = webuntis.Session(
                server=config_data['config'][1]['server'],
                username=config_data['config'][1]['username'],
                password=config_data['config'][1]['password'],
                school=config_data['config'][1]['school'],
                useragent=config_data['config'][1]['useragent']
            )
            s.login()

            if isinstance(s, str):
                print(f"Fehlerhafte Daten von Raum ", {raum})
            else:
                rooms = s.rooms().filter(name=raum)

                tt = s.timetable(room=rooms[0], start=start, end=end)
                tt = sorted(tt, key=lambda x: x.start)

                time_format_end = "%H%M"
                time_format_start = time_format_end
                time_format_date = "%Y-%m-%d"

                #create a list for cache things
                cache = []

                #printed the timetable of a room
                for po in tt: #d = date; s = start time; e = end time; k = class; t = teacher; r = room; sub = subject; c = cancelled
                    d = po.start.strftime(time_format_date)
                    s = po.start.strftime(time_format_start)
                    e = po.end.strftime(time_format_end)
                    k = " ".join([k.name for k in po.klassen])

                    #fixed error | blank teacher field
                    try:
                        t = " ".join([t.name for t in po.teachers])
                    except IndexError:
                        print(f"Fehler bei einem Eintrag einer Lehrkraft von Raum {raum}")

                    r = " ".join([r.name for r in po.rooms])
                    sub = " ".join([r.name for r in po.subjects])
                    c = "(" + po.code + ")" if po.code is not None else ""

                    #clear passed school hours
                    if chtime < e:
                        #print(d, s + "-" + e, k, sub, t, r, c)

                        #add things to the list
                        cache.append(s)
                        cache.append(e)
                        cache.append(k)
                        cache.append(sub)
                        cache.append(t)

                        print(cache)

                        #call the untis2imagegen.py file
                        #untis2imagegen(raum, k, t, sub, s, e, d, c)
                print(f"Daten von Raum {raum} erhalten ...")

    except FileNotFoundError:
        print("Configfile Not Found - Please check the File!")

def main():
    #loading config file
    try:
        with open('../config.json', 'r') as config_file:
            config_data = json.load(config_file)

            #check a few things and do things
            if (config_data['config'][0]['enabled']) == "true":

                #var for the roomdatabase file e.g. roomdatabase.json
                roomdatabase = config_data['config'][0]['roomdatabase']

                # load a json file with the rooms
                # use an own file because dev stat ~yeah
                try:
                    with open(roomdatabase, 'r') as file:
                        data = json.load(file)

                        # check if active stat
                        for i in data['rooms']:
                            if (i['enabled'][0]) == "t":
                                #call the untis_get function with the room number from the roomdatabase file
                                untis_get(i['roomnumber'])
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
        print("Configfile Not Found - Please check the File!")
if __name__ == "__main__":
    main()