import socket
import numpy as np
from PIL import Image

# IP-Adresse des ESP32 und Portnummer
ESP32_IP = "192.168.0.233"  # IP-Adresse des ESP32 (über den seriellen Monitor einsehbar)
PORT = 12345

# Erstelle einen Socket und verbinde mit dem ESP32
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ESP32_IP, PORT))

# Beispiel-uint8-Array
image_path = 'C:\\Users\\jusch\\Documents\\Arduino\\libraries\\LilyGo-EPD47-master\\examples\\drawImages\\image_for_epaper.bmp'  # Pfad zu deinem BMP-Bild
image = Image.open(image_path)

# Konvertiere das Bild in ein numpy-Array
image_array = np.array(image, dtype=np.uint8)

# Sende das Array byteweise an den ESP32
client_socket.send(image_array.tobytes())

# Verbindung schließen
client_socket.close()
print("Daten gesendet.")