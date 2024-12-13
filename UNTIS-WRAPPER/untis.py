# needs a filled config.json file with the login data
# you find the file in the main folder of the server project
#by ingressy

import datetime, webuntis.objects, json, logging, os, random
from untis2imagegen import untis2imagegen
from dotenv import load_dotenv


#time things IDK
time = datetime.datetime.now()
#chtime = (time.strftime("%H%M"))
chtime = "0825"
chdate = (time.strftime("%Y-%m-%d"))
start = datetime.datetime.now()
end = start + datetime.timedelta(days=1)

def untis_get(raum):
    #try to open the config json file
    try:
        with (open('../config.json', 'r') as config_file):
            config_data = json.load(config_file)

            # login by the untis api
            s = webuntis.Session(
                server=SERVER,
                username=USERNAME,
                password=PASSWORD,
                school=SCHOOL,
                useragent=USERAGENT
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

                        #print(cache)

                #call the untis2imagegen.py file
                # var array
                # first hour
                    try:
                        starttime1 = cache[0]
                        endtime1 = cache[1]
                        klasse1 = cache[2]
                        subject1 = cache[3]
                        teacher1 = cache[4]

                        # secound hour
                        starttime2 = cache[5]
                        endtime2 = cache[6]
                        klasse2 = cache[7]
                        subject2 = cache[8]
                        teacher2 = cache[9]

                        #third hour
                        starttime3 = cache[10]
                        endtime3 = cache[11]
                        klasse3 = cache[12]
                        subject3 = cache[13]
                        teacher3 = cache[14]

                        #fourth hour
                        starttime4 = cache[15]
                        endtime4 = cache[16]
                        klasse4 = cache[17]
                        subject4 = cache[18]
                        teacher4 = cache[19]

                        #fifth hour
                        starttime5 = cache[20]
                        endtime5 = cache[21]
                        klasse5 = cache[22]
                        subject5 = cache[23]
                        teacher5 = cache[24]

                        #sixth hour
                        starttime6 = cache[25]
                        endtime6 = cache[26]
                        klasse6 = cache[27]
                        subject6 = cache[28]
                        teacher6 = cache[29]

                        #check if the display first hour is double hour
                        if cache[2] == cache[7]: #class first hour = class second hour
                            if cache[3] == cache[8]: #subject first = subject second
                                subject1 = cache[3] #subject 1 = subject 1
                                teacher1 = cache[4] #teacher 1 = teacher 1
                                klasse1 = cache[2] #klasse1 = klasse 1
                                endtime1 = cache[6] #endtime = enddate2

                                #make the third hour to the secound hour
                                starttime2 = cache[10]
                                endtime2 = cache[11]
                                klasse2 = cache[12]
                                subject2 = cache[13]
                                teacher2 = cache[14]

                                #fourth hour
                                starttime3 = cache[15]
                                endtime3 = cache[16]
                                klasse3 = cache[17]
                                subject3 = cache[18]
                                teacher3 = cache[19]

                        elif cache[7] == cache[12]:#class second hour = class third hour
                            if cache[8] == cache[13]: #subject first = subject second
                                subject2 = cache[8] #subject 1 = subject 1
                                teacher2 = cache[9] #teacher 1 = teacher 1
                                klasse2 = cache[7] #klasse1 = klasse 1
                                endtime2 = cache[11] #endtime = enddate2

                                #fourth hour
                                starttime3 = cache[15]
                                endtime3 = cache[16]
                                klasse3 = cache[17]
                                subject3 = cache[18]
                                teacher3 = cache[19]

                        elif cache[12] == cache[17]: # class third hour = class fourth hour
                            if cache[13] == cache[18]:  # subject third = subject fourth
                                subject2 = cache[13]  # subject 1 = subject 1
                                teacher2 = cache[14]  # teacher 1 = teacher 1
                                klasse2 = cache[12]  # klasse1 = klasse 1
                                endtime2 = cache[16]  # endtime = enddate2

                                #make the sixth hour to the third hour
                                starttime3 = cache[25]
                                endtime3 = cache[26]
                                klasse3 = cache[27]
                                subject3 = cache[18]
                                teacher3 = cache[29]

                        elif cache[17] == cache[22]: # class fourth hour = class fifth hour
                            if cache[18] == cache[23]:  # subject fourth = subject fifth
                                subject2 = cache[18]  # subject 1 = subject 1
                                teacher2 = cache[19]  # teacher 1 = teacher 1
                                klasse2 = cache[17]  # klasse1 = klasse 1
                                endtime2 = cache[21]  # endtime = enddate2

                                #make the sixth hour to the third hour
                                starttime3 = cache[25]
                                endtime3 = cache[26]
                                klasse3 = cache[27]
                                subject3 = cache[28]
                                teacher3 = cache[29]

                        elif cache[22] == cache[27]: # class fifth hour = class sixth hour
                            if cache[23] == cache[28]:  # subject fourth = subject fifth
                                subject3 = cache[23]  # subject 1 = subject 1
                                teacher3 = cache[24]  # teacher 1 = teacher 1
                                klasse3 = cache[22]  # klasse1 = klasse 1
                                endtime3 = cache[26]  # endtime = enddate2
                    except:
                        #print("hier stimmt was nicht")
                        starttime1 = "0"
                        starttime2 = "0"
                        starttime3 = "0"
                        endtime1 = "0"
                        endtime2 = "0"
                        endtime3 = "0"

                        klasse1 = "0"
                        klasse2 = "0"
                        klasse3 = "0"

                        subject1 = "0"
                        subject2 = "0"
                        subject3 = "0"

                        teacher1 = "0"
                        teacher2 = "0"
                        teacher3 = "0"

                    untis2imagegen(raum, klasse1, teacher1, subject1, starttime1, endtime1, c, klasse2, teacher2, subject2, starttime2, endtime2, klasse3, teacher3, subject3, starttime3, endtime3)
                    logger.info(f"Daten von Raum {raum} erhalten ...")

    except FileNotFoundError:
        c_config_file()

def c_config_file():
    # create config.json
    try:
        logger.error("Configfile created!")
        print("Configfile created!")

        config_file = {"config": [
            {"_comment": "json data for the untis wrapper", "enabled": "false", "roomdatabase": "rooms.json"},
            {"_comment": "login data for untis", "use_env": "false", "server": "", "username": "", "password": "",
             "school": "", "useragent": ""},
            {"_comment": "Config for Image-Gen.py", "width": 960, "height": 576, "background_color": 255,
             "TBZ_Logo_path": "../SNIPPETS/TBZ-sb.png", "Standard_font": "../IMAGEGEN/Arial.TTF",
             "Config_rect_color": 255, "Config_rect_height": 100, "Config_rect_margin": 140, "Config_rect_spacing": 30,
             "Custom_Text": "~UwU"}]}
        with open('../config.json', 'w') as file:
            json.dump(config_file, file, indent=4)
    except:
        logger.error("File creation not possible")
        print("File creation not possible")

def main():
    #check if log folder exist
    if not os.path.exists("log"):
        os.makedirs("log")

    # add a log file
    global logger
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename=f'log/{chtime}-{chdate}.log', encoding='utf-8', level=logging.INFO)
    logger.info("untis.py script started")

    #loading config file
    try:
        with open('../config.json', 'r') as config_file:
            config_data = json.load(config_file)

            #check a few things and do things
            if (config_data['config'][0]['enabled']) == "true":
                #check the location of the login data
                if config_data['config'][1]['use_env'] == "false":
                    #write the login data intro the .env file
                    env = open(".env", "w")
                    env.write(f"SERVER={config_data['config'][1]['server']}\n")
                    env.write(f"NAME={config_data['config'][1]['username']}\n")
                    env.write(f"PASSWORD={config_data['config'][1]['password']}\n")
                    env.write(f"SCHOOL={config_data['config'][1]['school']}\n")
                    env.write(f"USERAGENT={config_data['config'][1]['useragent']}")

                    #delete login data in config.json
                    for config in config_data["config"]:
                        if "server" in config:
                            config["server"] = None
                        if "username" in config:
                            config["username"] = None
                        if "password" in config:
                            config["password"] = None
                        if "school" in config:
                            config["school"] = None
                        if "useragent" in config:
                            config["useragent"] = None
                        if "use_env" in config:
                            config["use_env"] = "true"

                    with open('../config.json', 'w') as file:
                        json.dump(config_data, file, indent=4)

                    main()
                else:
                    global SERVER, USERNAME, PASSWORD, SCHOOL, USERAGENT

                    # load env file
                    load_dotenv()
                    SERVER = os.getenv('SERVER')
                    USERNAME = os.getenv('NAME')
                    PASSWORD = os.getenv('PASSWORD')
                    SCHOOL = os.getenv('SCHOOL')
                    USERAGENT = os.getenv('USERAGENT')
                    
                    #Easter Egg change the font ~ 1/100 probability
                    #ran = random.randint(0, 1)
                    ran = "0"
                    if ran == "1":
                        with open('../config.json', 'r') as config_file:
                            config_data = json.load(config_file)
                            for config in config_data["config"]:
                                if "Standard_font" in config:
                                    config["Standard_font"] = "../IMAGEGEN/DrolleSchriftart.ttf"
                        with open('../config.json', 'w') as file:
                            json.dump(config_data, file, indent=4)
                    else:
                        with open('../config.json', 'r') as config_file:
                            config_data = json.load(config_file)
                            for config in config_data["config"]:
                                if "Standard_font" in config:
                                    config["Standard_font"] = "../IMAGEGEN/Arial.TTF"
                        with open('../config.json', 'w') as file:
                            json.dump(config_data, file, indent=4)

                #var for the roomdatabase file e.g. roomdatabase.json
                roomdatabase = config_data['config'][0]['roomdatabase']

                # load a json file with the rooms
                # use an own file because dev state ~yeah
                try:
                    with open(roomdatabase, 'r') as file:
                        data = json.load(file)

                        # check if active state
                        for i in data['rooms']:
                            if (i['enabled'][0]) == "t":
                                #call the untis_get function with the room number from the roomdatabase file
                                logger.info("Pull timetable for Room: " + i['roomnumber'])
                                untis_get(i['roomnumber'])
                            elif (i['enabled'][0]) == "f":
                                logger.warning("Room  " + i['roomnumber'] + " is disabled")
                                # do nothing here
                            else:
                                logger.error("Reading Room Database! | " + i['roomnumber'])
                except FileNotFoundError:
                    logger.error("File Not Found - Please check the File!")
            else:
                logger.warning("untis-wrapper disabled - Please enabled in config.json")
                exit(0)
    except FileNotFoundError:
        c_config_file()
if __name__ == "__main__":
    main()