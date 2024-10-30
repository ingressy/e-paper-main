#!/usr/bin/python
from PIL import Image, ImageDraw, ImageFont
import datetime


display_argument_demo = {
    "lehrer": "SCJ",
    "fach": "IFT",
    "zeit": "08:10-09:40",
    "klasse": "BGT221",
}

def gen_display(argument_list):
    for x,y in argument_list:
        print("INHALT: "+x +" : "+y)

def gen_image():
    # Bildparameter
    width, height = 960, 576
    #width, height = 480, 288
    background_color = 255  # Weiß

    # Bild erstellen (Graustufenmodus 'L')
    image = Image.new('L', (width, height), color=background_color)

    # Objekt zum Zeichnen auf dem Bild erstellen
    draw = ImageDraw.Draw(image)

# Logo laden und positionieren (auf 209x113 Pixel skalieren)
try:
    logo = Image.open('TBZ-sb.png').convert('L')  # Logo in Graustufen laden
    logo = logo.resize((209, 113))  # Logo auf 209x113 Pixel skalieren
    image.paste(logo, (20, 20))  # Logo in der oberen linken Ecke platzieren
except FileNotFoundError:
    print("Logo-Datei 'logo.png' nicht gefunden. Überspringe das Logo.")

    # Rechteckparameter
    rect_height = 100
    rect_margin_top = 140
    rect_spacing = 30
    rect_text = "DEMO"
    rect_color = 255  # Schwarz
    rect_outline_color = 1  # Weiß

# Schriftart laden (Arial oder Standardschrift)
try:
    font_large = ImageFont.truetype("arial.ttf", 50)  # Große Schrift für "DEMO"
    font_medium = ImageFont.truetype("arial.ttf", 60)  # Mittlere Schrift für "2.311 Montag"
    font_small = ImageFont.truetype("arial.ttf", 20)  # Kleine Schrift für "generiert um"
except IOError:
    font_large = ImageFont.load_default()
    font_medium = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Drei Rechtecke zeichnen
for i in range(3):
    rect_top = rect_margin_top + i * (rect_height + rect_spacing)
    rect_bottom = rect_top + rect_height
    draw.rectangle([20, rect_top, width - 20, rect_bottom], fill=rect_color, outline=rect_outline_color,width=5)

    # Text "DEMO" in der Mitte jedes Rechtecks platzieren
    bbox = draw.textbbox((0, 0), rect_text, font=font_large)  # Bounding box des Textes berechnen
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_x = (width - text_width) // 2
    text_y = rect_top + (rect_height - text_height) // 2
    draw.text((text_x, text_y), rect_text, font=font_large, fill=0)  # Text in Schwarz (0)

    # Mittigen Text "2.311 Montag" in der ersten Zeile neben dem Logo platzieren
    center_text = "2.311 Montag"
    bbox = draw.textbbox((0, 0), center_text, font=font_medium)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Berechnung der Position rechts vom Logo
    logo_x, logo_y = 20, 20  # Position des Logos
    logo_width, logo_height = 209, 113  # Größe des Logos

    # Text rechts neben dem Logo platzieren (etwas Abstand dazwischen)
    text_x = logo_x + logo_width + 20  # 20 Pixel Abstand zum Logo
    text_y = logo_y + (logo_height - text_height) // 2  # Vertikal zentriert mit dem Logo

    draw.text((text_x, text_y), center_text, font=font_medium, fill=0)  # Text in Schwarz (0)

    # Aktuelle Zeit für den unteren Text
    current_time = datetime.datetime.now().strftime("%d.%Y.%m %H:%M")








version = '0.1'

# Ende von generate_images.py