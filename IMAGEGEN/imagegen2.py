from PIL import Image, ImageDraw, ImageFont
import datetime, json

# Configdaten importieren und auf Grundvariablen anwenden:
try:
    with open('../config.json', 'r') as config_file:
        config_data = json.load(config_file)

        # Bildparameter
        width, height = config_data['config'][2]['width'], config_data['config'][2]['height']
        # width, height = 480, 288
        background_color = config_data['config'][2]['background_color']  # Weiß


        # Logo laden und positionieren (auf 209x113 Pixel skalieren)
        try:
            logo = Image.open(config_data['config'][2]['TBZ_Logo_path']).convert('L')  # Logo in Graustufen laden
            logo = logo.resize((209, 113))  # Logo auf 209x113 Pixel skalieren
        except FileNotFoundError:
            print("Logo-Datei 'logo.png' nicht gefunden. Überspringe das Logo.")

        #Standard-Font in Variable übertragen:
        Config_Font = config_data['config'][2]['Standard_font']

        # Rechteckdimensionen einfügen:
        Config_Rect_Color = config_data['config'][2]['Config_rect_color']
        Config_Rect_Height = config_data['config'][2]['Config_rect_height']
        Config_Rect_Margin = config_data['config'][2]['Config_rect_margin']
        Config_Rect_Spacing = config_data['config'][2]['Config_rect_spacing']

        # Standard Bottom Text aus Config abrufen
        Custom_Config_Text = config_data['config'][2]['Custom_Text']
        MaintenanceMode = config_data['config'][2]['MaintenanceMode']

except:
    print("Configfile not found - Please check the File!")


# Die Hauptfunktion:
def gen_image(room, start1, end1, teach1, sub1, klasse1, abw1, start2, end2, teach2, sub2, klasse2, abw2, start3, end3,
              teach3, sub3, klasse3, abw3,display_Bottom):
    before_rect_height = 0
    # Bild erstellen (Graustufenmodus 'L')
    image = Image.new('L', (width, height), color=background_color)
    rect_total = 0

    # Objekt zum Zeichnen auf dem Bild erstellen
    draw = ImageDraw.Draw(image)
    image.paste(logo, (20, 20))  # Logo in der oberen linken Ecke platzieren
    # Herausfinden, wie viele Stunden noch angezeigt werden müssen:
    if end1 != "0":
        classNumber = 1
        if end2 != "0":
            classNumber = 2
            if end3 != "0":
                classNumber = 3
    elif end1 == "0":
        classNumber = 0

    # Schriftart laden (Config oder Standardschrift)
    try:
        font_huge = ImageFont.truetype(Config_Font, 60)  # Riesenschrift
        font_large = ImageFont.truetype(Config_Font, 50)  # Große Schrift für Fächer
        font_medium = ImageFont.truetype(Config_Font, 35)  # Mittlere Schrift für Klassen und Lehrer
        font_small = ImageFont.truetype(Config_Font, 20)  # Kleine Schrift für "generiert um" und Zeiten
    except IOError:
        font_huge = ImageFont.load_default()
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Fall, falls es keinen Unterricht mehr in diesem Raum gibt:
    if classNumber == 0:
        draw.text((140, 240), "Heute kein weiterer Unterricht", font=font_large, fill=0)
        draw.text((270, 320), "in diesem Raum", font=font_large, fill=0)

    # Nur zum Wissen, keine Funktion:
    # Abweichungen = ["Normaler Unterricht, keine Abweichung", "Ausfall", "Vertretung", "Raumwechsel","Vertretung & Raumwechsel"]

    # Rechteckparameter aus Config
    rect_height = Config_Rect_Height
    rect_margin_top = Config_Rect_Margin
    rect_spacing = Config_Rect_Spacing
    rect_subtxt = "ERR 404"
    rect_starttxt = "0"
    rect_endtxt = "0"
    rect_teachtxt = "0"
    rect_classtxt = "0"
    classStartHour = 0
    classEndHour = 0
    # Nur Vordefinition
    special = 0
    rect_color = Config_Rect_Color  # Schwarz
    rect_outline_color = 1  # Weiß

    # For-Schleife vorbereiten:
    currentClassPrintMax = classNumber
    currentClassPrint = 1

    # Rechtecke zeichnen
    for i in range(classNumber):
        # Frag nicht, aber diese Zeile ist sehr wichtig.
        rect_height = Config_Rect_Height

        if currentClassPrint == 1:
            rect_subtxt = sub1
            startRaw = start1
            endRaw = end1
            rect_teachtxt = teach1
            rect_classtxt = klasse1
            special = abw1
        elif currentClassPrint == 2:
            rect_subtxt = sub2
            startRaw = start2
            endRaw = end2
            rect_teachtxt = teach2
            rect_classtxt = klasse2
            special = abw2
        elif currentClassPrint == 3:
            rect_subtxt = sub3
            startRaw = start3
            endRaw = end3
            rect_teachtxt = teach3
            rect_classtxt = klasse3
            special = abw3

        match startRaw:
            case "0810":
                rect_starttxt = "08:10 -"
                classStartHour = 1
            case "0855":
                rect_starttxt = "08:55 -"
                classStartHour = 2
            case "1000":
                rect_starttxt = "10:00 -"
                classStartHour = 3
            case "1045":
                rect_starttxt = "10:45 -"
                classStartHour = 4
            case "1145":
                rect_starttxt = "11:45 -"
                classStartHour = 5
            case "1230":
                rect_starttxt = "12:30 -"
                classStartHour = 6
            case "1345":
                rect_starttxt = "13:45 -"
                classStartHour = 7
            case "1430":
                rect_starttxt = "14:30 -"
                classStartHour = 8
            case "1530":
                rect_starttxt = "15:30 -"
                classStartHour = 9
            case "1615":
                rect_starttxt = "16:15 -"
                classStartHour = 10
        match endRaw:
            case "0855":
                rect_endtxt = "08:55"
                classEndHour = 1
            case "0940":
                rect_endtxt = "09:40"
                classEndHour = 2
            case "1045":
                rect_endtxt = "10:45"
                classEndHour = 3
            case "1130":
                rect_endtxt = "11:30"
                classEndHour = 4
            case "1230":
                rect_endtxt = "12:30"
                classEndHour = 5
            case "1315":
                rect_endtxt = "13:15"
                classEndHour = 6
            case "1430":
                rect_endtxt = "14:30"
                classEndHour = 7
            case "1515":
                rect_endtxt = "15:15"
                classEndHour = 8
            case "1615":
                rect_endtxt = "16:15"
                classEndHour = 9
            case "1700":
                rect_endtxt = "17:00"
                classEndHour = 10

        # Herausfinden, wie lange die anzuzeigende Stunde ist:
        classLength = classEndHour - classStartHour

        # Vorherige Größe bestimmen, um Format nicht zu bumsen:
        if i == 1:
            rect_total = rect_total + (before_rect_height - rect_height)
            rect_before = before_rect_height
        elif i == 2:
            rect_before = before_rect_height + rect_total
        else:
            rect_before = 0

        # Stunden Länger je nach insgesamter Stundenlänge oder so
        if classLength == 0:
            rect_height = rect_height - 25
            before_rect_height = rect_height
        elif classLength == 1:
            rect_height = rect_height + 0
            before_rect_height = rect_height
        elif classLength == 2:
            rect_height = rect_height + 10
            before_rect_height = rect_height
        elif classLength == 3:
            rect_height = rect_height + 25
            before_rect_height = rect_height

        # Rechtecke zeichnen:
        rect_top = rect_margin_top + i * (rect_before + rect_spacing)
        rect_bottom = rect_top + rect_height
        draw.rectangle([20, rect_top, width - 20, rect_bottom], fill=rect_color, outline=rect_outline_color, width=5)

        # Fach in der Mitte jedes Rechtecks platzieren
        bbox = draw.textbbox((0, 0), rect_subtxt, font=font_large)
        # Bounding box des Textes berechnen
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        text_x = (width - text_width) // 2
        text_y = rect_top + (rect_height - text_height) // 2
        draw.text((text_x, text_y), rect_subtxt, font=font_large, fill=0)  # Text in Schwarz (0)
        # Ausfall:
        if special == 1:
            line_y = text_y + text_height // 1.5
            draw.line((text_x, line_y, text_x + text_width, line_y), fill="black", width=5)

        # Startzeiten einfügen
        bbox = draw.textbbox((0, 0), rect_starttxt, font=font_small)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        text_x = (width - width + 100) // 2
        text_y = rect_top + (rect_height - 60) // 2
        draw.text((text_x, text_y), rect_starttxt, font=font_small, fill=0)
        # Endzeiten einfügen
        bbox = draw.textbbox((0, 0), rect_endtxt, font=font_small)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        text_x = (width - width + 100) // 2
        text_y = rect_top + (rect_height + 20) // 2
        draw.text((text_x, text_y), rect_endtxt, font=font_small, fill=0)

        # Lehrer einfügen
        bbox = draw.textbbox((0, 0), rect_teachtxt, font=font_medium)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        text_x = (width - text_width + 500) // 2
        text_y = rect_top + (rect_height - text_height) // 2
        draw.text((text_x, text_y), rect_teachtxt, font=font_medium, fill=0)
        if special == 1 or special == 2 or special == 4:
            line_y = text_y + text_height // 1.5
            draw.line((text_x, line_y, text_x + text_width, line_y), fill="black", width=3)

        # Klasse einfügen
        bbox = draw.textbbox((0, 0), rect_classtxt, font=font_medium)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        text_x = (width - text_width - 450) // 2
        text_y = rect_top + (rect_height - text_height) // 2
        draw.text((text_x, text_y), rect_classtxt, font=font_medium, fill=0)
        if special == 1:
            line_y = text_y + text_height // 1.5
            draw.line((text_x, line_y, text_x + text_width, line_y), fill="black", width=3)

        # Raum einfügen bei special == "3" or 4
        if special == 3 or special == 4:
            bbox = draw.textbbox((0, 0), room, font=font_medium)
            text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
            text_x = (width - text_width + 750) // 2
            text_y = rect_top + (rect_height - text_height) // 2
            draw.text((text_x, text_y), room, font=font_medium, fill=0)
            line_y = text_y + text_height // 1.5
            draw.line((text_x, line_y, text_x + text_width, line_y), fill="black", width=3)

        if currentClassPrint != currentClassPrintMax:
            currentClassPrint = currentClassPrint + 1

    # Mittigen Text Raum und Tag in der ersten Zeile neben dem Logo platzieren
    currentDayNum = datetime.datetime.today().weekday()
    currentDay = [" - Montag", " - Dienstag", " - Mittwoch", " - Donnerstag", " - Freitag", " - Samstag", " - Sonntag"]

    center_text = room + currentDay[currentDayNum]
    bbox = draw.textbbox((0, 0), center_text, font=font_huge)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Berechnung der Position rechts vom Logo
    logo_x, logo_y = 20, 20  # Position des Logos
    logo_width, logo_height = 209, 113  # Größe des Logos

    # Text rechts neben dem Logo platzieren (etwas Abstand dazwischen)
    text_x = logo_x + logo_width + 20  # 20 Pixel Abstand zum Logo
    text_y = logo_y + (logo_height - text_height) // 2  # Vertikal zentriert mit dem Logo

    draw.text((text_x, text_y), center_text, font=font_medium, fill=0)  # Text in Schwarz (0)

    # Aktuelle Zeit für den unteren Text
    current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M Uhr")

    # Text in der untersten Zeile
    footer_text = f"Generiert: {current_time}"
    bbox = draw.textbbox((0, 0), footer_text, font=font_small)  # Bounding box des Textes berechnen
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((width - text_width - 20, height - text_height - 20), footer_text, font=font_small,
              fill=0)  # Schwarzer Text

    # Herausfinden, ob es eine besondere Bottom Msg geben soll, sonst wird der Config Standard genutzt.
    if display_Bottom == "0":
        Custom_Msg = Custom_Config_Text
    else:
        Custom_Msg = display_Bottom
    bbox = draw.textbbox((0,0) , Custom_Msg, font=font_small, align="right")
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((10, height - text_height - 20), Custom_Msg, font=font_small,
              fill=0, align="right")

    # Überprüfen, ob der Wartungsmodus false oder true ist:
    if MaintenanceMode == True:
        # Bild speichern als graustufenbild_demo (Wartungsmodus)
        image.save('graustufenbild_demo.png')
    elif MaintenanceMode == False:
        # Bild nach Raumname in ROMMIMAGES speichern
        image.save(f"../ROOMIMAGES/{room}", 'png')


# gen_image("2.310", "0855", "1130", "SCJ","BInf","BGT 241",0,"1145","1315","SID","IFT","BGT 241",0,"1345","1615","WIB", "DEU","BGT 241",0, "TesLOL")

# if __name__ == "__main__":
#    try:
#gen_image("2.311","1","2","SCJ","IFT","BGT241")
#        gen_image("2.311","1","2","SCJ","IFT","BGT241","3","4","DIB","MAT","BGT221")
#        gen_image("2.311","1","2","SCJ","IFT","BGT241","3","4","DIB","MAT","BGT221","5","5","BEN","BInf","BGT4711")
#    except KeyboardInterrupt:
#        # Behandle Strg+C und beende den Server sauber
#        print("\nStrg+C erkannt. Server wird beendet...")

