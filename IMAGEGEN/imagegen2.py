from PIL import Image, ImageDraw, ImageFont
import datetime, json

try:
    with open('../config.json', 'r') as config_file:
        config_data = json.load(config_file)

        # Bildparameter
        width, height = config_data['config'][2]['width'], config_data['config'][2]['height']
        # width, height = 480, 288
        background_color = config_data['config'][2]['background_color']  # Weiß

        # Bild erstellen (Graustufenmodus 'L')
        image = Image.new('L', (width, height), color=background_color)

        # Objekt zum Zeichnen auf dem Bild erstellen
        draw = ImageDraw.Draw(image)

        # Logo laden und positionieren (auf 209x113 Pixel skalieren)
        try:
            logo = Image.open(config_data['config'][2]['TBZ_Logo_path']).convert('L')  # Logo in Graustufen laden
            logo = logo.resize((209, 113))  # Logo auf 209x113 Pixel skalieren
            image.paste(logo, (20, 20))  # Logo in der oberen linken Ecke platzieren
        except FileNotFoundError:
            print("Logo-Datei 'logo.png' nicht gefunden. Überspringe das Logo.")

        #Standard-Font in Variable übertragen:
        Config_Font = config_data['config'][2]['Standard_font']
        Config_Rect_Color = config_data['config'][2]['Config_rect_color']
        Config_Rect_Height = config_data['config'][2]['Config_rect_height']
        Config_Rect_Margin = config_data['config'][2]['Config_rect_margin']
        Config_Rect_Spacing = config_data['config'][2]['Config_rect_spacing']

except:
    print("Configfile not found - Please check the File!")
def gen_image(room, start1, end1, teach1, sub1, klasse1, abw1, start2, end2, teach2, sub2, klasse2, abw2, start3, end3,
              teach3, sub3, klasse3, abw3):
    if end1 != "0":
        classNumber = 1
        if end2 != "0":
            classNumber = 2
            if end3 != "0":
                classNumber = 3
    elif end1 == "0":
        classNumber = 0
    # Schriftart laden (Arial oder Standardschrift)
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

    if classNumber == 0:
        draw.text((140, 240), "Heute kein weiterer Unterricht", font=font_large, fill=0)
        draw.text((270, 320), "in diesem Raum", font=font_large, fill=0)

    # Nur zum Wissen, keine Funktion:
    Abweichungen = ["Normaler Unterricht, keine Abweichung", "Ausfall"]

    # Rechteckparameter
    rect_height = Config_Rect_Height
    rect_margin_top = Config_Rect_Margin
    rect_spacing = Config_Rect_Spacing
    rect_subtxt = "ERR 404"
    rect_starttxt = "0"
    rect_endtxt = "0"
    rect_teachtxt = "0"
    rect_classtxt = "0"
    special = "0"
    rect_color = Config_Rect_Color  # Schwarz
    rect_outline_color = 1  # Weiß

    currentClassPrintMax = classNumber
    currentClassPrint = 1
    # Rechtecke zeichnen
    for i in range(classNumber):
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
            case "800":
                rect_starttxt = "8:00 -"
            case "855":
                rect_starttxt = "8:55 -"
            case "1000":
                rect_starttxt = "10:00 -"
            case "1045":
                rect_starttxt = "10:45 -"
            case "1145":
                rect_starttxt = "11:45 -"
            case "1230":
                rect_starttxt = "12:30 -"
            case "1345":
                rect_starttxt = "13:45 -"
            case "1430":
                rect_starttxt = "14:30 -"
            case "1530":
                rect_starttxt = "15:30 -"
            case "1615":
                rect_starttxt = "16:15 -"
        match endRaw:
            case "855":
                rect_endtxt = "8:55"
            case "940":
                rect_endtxt = "9:40"
            case "1045":
                rect_endtxt = "10:45"
            case "1130":
                rect_endtxt = "11:30"
            case "1230":
                rect_endtxt = "12:30"
            case "1315":
                rect_endtxt = "13:15"
            case "1430":
                rect_endtxt = "14:30"
            case "1515":
                rect_endtxt = "15:15"
            case "1615":
                rect_endtxt = "16:15"
            case "1700":
                rect_endtxt = "17:00"

        rect_top = rect_margin_top + i * (rect_height + rect_spacing)
        rect_bottom = rect_top + rect_height
        draw.rectangle([20, rect_top, width - 20, rect_bottom], fill=rect_color, outline=rect_outline_color, width=5)

        # Fach in der Mitte jedes Rechtecks platzieren
        bbox = draw.textbbox((0, 0), rect_subtxt, font=font_large)
        # Bounding box des Textes berechnen
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        text_x = (width - text_width) // 2
        text_y = rect_top + (rect_height - text_height) // 2
        draw.text((text_x, text_y), rect_subtxt, font=font_large, fill=0)  # Text in Schwarz (0)
        if special == "1":
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
        if special == "1" or special == "2" or special == "4":
            line_y = text_y + text_height // 1.5
            draw.line((text_x, line_y, text_x + text_width, line_y), fill="black", width=3)

        # Klasse einfügen
        bbox = draw.textbbox((0, 0), rect_classtxt, font=font_medium)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        text_x = (width - text_width - 450) // 2
        text_y = rect_top + (rect_height - text_height) // 2
        draw.text((text_x, text_y), rect_classtxt, font=font_medium, fill=0)
        if special == "1":
            line_y = text_y + text_height // 1.5
            draw.line((text_x, line_y, text_x + text_width, line_y), fill="black", width=3)

        # Raum einfügen bei special == "3" or 4
        if special == "3" or special == "4":
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

    # Bild anzeigen und speichern
    #image.show()
    image.save('graustufenbild_demo.png')


# gen_image("2.310","1","2","SCJ","BInf","BGT 241","0","0","0","0","0","0","0","0","0","0", "0","0","0")

# if __name__ == "__main__":
#    try:
#gen_image("2.311","1","2","SCJ","IFT","BGT241")
#        gen_image("2.311","1","2","SCJ","IFT","BGT241","3","4","DIB","MAT","BGT221")
#        gen_image("2.311","1","2","SCJ","IFT","BGT241","3","4","DIB","MAT","BGT221","5","5","BEN","BInf","BGT4711")
#    except KeyboardInterrupt:
#        # Behandle Strg+C und beende den Server sauber
#        print("\nStrg+C erkannt. Server wird beendet...")

