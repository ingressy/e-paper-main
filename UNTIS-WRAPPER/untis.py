# needs a filled config.json file with the login data
# you find the file in the main folder of the server project
#by ingressy

import datetime, webuntis.objects, json, logging, os, random
from untis2imagegen import untis2imagegen
from dotenv import load_dotenv


#time things IDK
time = datetime.datetime.now()
chtime = (time.strftime("%H%M"))
#chtime = "0825"
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
                global cache
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
                        cache.append(c)

                        print(cache)

                #call the untis2imagegen.py file
                # var array
                # first hour
                    try:
                        starttime1 = cache[0]
                        endtime1 = cache[1]

                        klasse1 = x_klasse(2, "klasse1")
                        #klasse1 = cache[2]

                        subject1 = cache[3]
                        teacher1 = cache[4]
                        if cache[5] == "(cancelled)":
                            abw1 = 1

                        # secound hour
                        starttime2 = cache[6]
                        endtime2 = cache[7]

                        klasse2 = x_klasse(8, "klasse2")
                        #klasse2 = cache[8]

                        subject2 = cache[9]
                        teacher2 = cache[10]
                        if cache[11] == "(cancelled)":
                            abw1 = 1

                        #third hour
                        starttime3 = cache[12]
                        endtime3 = cache[13]

                        klasse3 = x_klasse(14, "klasse3")
                        #klasse3 = cache[14]

                        subject3 = cache[15]
                        teacher3 = cache[16]
                        if cache[17] == "(cancelled)":
                            abw1 = 1

                        #fourth hour
                        starttime4 = cache[18]
                        endtime4 = cache[19]
                        klasse4 = cache[20]
                        subject4 = cache[21]
                        teacher4 = cache[22]
                        abw4 = cache[23]

                        #fifth hour
                        starttime5 = cache[24]
                        endtime5 = cache[25]
                        klasse5 = cache[26]
                        subject5 = cache[27]
                        teacher5 = cache[28]
                        abw5 = cache[29]

                        #sixth hour
                        starttime6 = cache[30]
                        endtime6 = cache[31]
                        klasse6 = cache[32]
                        subject6 = cache[33]
                        teacher6 = cache[34]
                        abw6 = cache[35]

                        #check if the display first hour is double hour
                        if cache[2] == cache[8]: #class first hour = class second hour
                            if cache[3] == cache[9]: #subject first = subject second
                                subject1 = cache[3] #subject 1 = subject 1
                                teacher1 = cache[4]

                                klasse1 = x_klasse(2, "klasse1")
                                #klasse1 = cache[2] #klasse1 = klasse 1

                                endtime1 = cache[7] #endtime = enddate2
                                if cache[11] == "(cancelled)":
                                    abw1 = 1

                                #make the third hour to the secound hour
                                starttime2 = cache[12]
                                endtime2 = cache[13]

                                klasse2 = x_klasse(14, "klasse2")
                                #klasse2 = cache[12]

                                subject2 = cache[15]
                                teacher2 = cache[16]
                                if cache[17] == "(cancelled)":
                                    abw2 = 1

                                #fourth hour
                                #starttime3 = cache[15]
                                #endtime3 = cache[16]
                                #klasse3 = cache[17]
                                #subject3 = cache[18]
                                #teacher3 = cache[19]

                        if cache[8] == cache[14]:#class second hour = class third hour
                            if cache[9] == cache[15]: #subject first = subject second
                                subject2 = cache[9] #subject 1 = subject 1
                                teacher2 = cache[10] #teacher 1 = teacher 1

                                klasse2 = x_klasse(8, "klasse2")
                                #klasse2 = cache[7] #klasse1 = klasse 1

                                endtime2 = cache[13] #endtime = enddate2
                                if cache[11] == "(cancelled)":
                                    abw2 = 1

                                #fourth hour
                                starttime3 = cache[18]
                                endtime3 = cache[19]

                                klasse3 = x_klasse(20, "klasse3")
                                #klasse3 = cache[17]

                                subject3 = cache[21]
                                teacher3 = cache[22]
                                if cache[23] == "(cancelled)":
                                    abw3 = 1

                        if cache[14] == cache[20]: # class third hour = class fourth hour
                            if cache[15] == cache[21]:  # subject third = subject fourth
                                subject2 = cache[15]  # subject 1 = subject 1
                                teacher2 = cache[16]  # teacher 1 = teacher 1
                                if cache[17] == "(cancelled)":
                                    abw2 = 1

                                klasse2 = x_klasse(14, "klasse2")
                                #klasse2 = cache[12]  # klasse1 = klasse 1

                                endtime2 = cache[19]  # endtime = enddate2

                                #make the sixth hour to the third hour
                                starttime3 = cache[30]
                                endtime3 = cache[31]
                                klasse3 = cache[32]
                                subject3 = cache[33]
                                teacher3 = cache[34]
                                if cache[35] == "(cancelled)":
                                    abw3 = 1


                        if cache[20] == cache[26]: # class fourth hour = class fifth hour
                            if cache[21] == cache[27]:  # subject fourth = subject fifth
                                subject2 = cache[21]  # subject 1 = subject 1
                                teacher2 = cache[22]  # teacher 1 = teacher 1
                                if cache[23] == "(cancelled)":
                                    abw2 = 1

                                klasse2 = x_klasse(20, "klasse2")
                                #klasse2 = cache[17]  # klasse1 = klasse 1

                                endtime2 = cache[25]  # endtime = enddate2

                                #make the sixth hour to the third hour
                                starttime3 = cache[30]
                                endtime3 = cache[31]

                                klasse3 = x_klasse(32, "klasse3")
                                #klasse3 = cache[32]

                                subject3 = cache[33]
                                teacher3 = cache[34]
                                if cache[35] == "(cancelled)":
                                    abw3 = 1


                        if cache[26] == cache[32]: # class fifth hour = class sixth hour
                            if cache[27] == cache[33]:  # subject fourth = subject fifth
                                subject3 = cache[27]  # subject 1 = subject 1
                                teacher3 = cache[28]  # teacher 1 = teacher 1
                                if cache[29] == "(cancelled)":
                                    abw3 = 1

                                klasse3 = x_klasse(26, "klasse3")
                                #klasse3 = cache[22]  # klasse1 = klasse 1

                                endtime3 = cache[31]  # endtime = enddate2

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

                        abw1 = "0"
                        abw2 = "0"
                        abw3 = "0"

                    untis2imagegen(raum, klasse1, teacher1, subject1, starttime1, endtime1, abw1, klasse2, teacher2, subject2, starttime2, endtime2, abw2, klasse3, teacher3, subject3, starttime3, endtime3, abw3)
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

def x_klasse(cache_number, display_klasse):

    klasse = cache[cache_number]
    count = sum(1 for i in klasse)
    number = [zeichen for zeichen in klasse if zeichen.isdigit()]

    klasse_number = str(''.join(number))[:2] + "X"
    if count >= 28:
        klasse_number = str(''.join(number))[:1] + "XX"
        klasse_prefix = klasse[:3]
        return klasse_prefix + ' ' + klasse_number
    elif count >= 8:
        klasse_prefix = klasse[:3]
        return klasse_prefix + ' ' + klasse_number
    else:
        return cache[cache_number]

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
                    env.write(f"USERAGENT={config_data['config'][1]['useragent']}\n")
                    env.write(f"DCWEBHOOK={config_data['config'][1]['Discord_Webhook']}")

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
                        if "Discord_Webhook" in config:
                            config['Discord_Webhook'] = None
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