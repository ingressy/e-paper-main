import socket
import numpy as np
from PIL import Image


def image_to_array(image_path):
    """Öffnet ein Graustufenbild und gibt die Pixelwerte als eindimensionales Array zurück."""
    # Bild öffnen
    with Image.open(image_path) as img:
        # Bild in Graustufen konvertieren, falls es nicht schon in diesem Modus ist
        gray_image = img.convert('L')
        
        # Pixelwerte als numpy-Array extrahieren
        pixel_array = np.array(gray_image)

        # In ein eindimensionales Array konvertieren
        pixel_array_flattened = pixel_array.flatten()  # Alternativ: pixel_array.ravel()

    return pixel_array_flattened

def reduce_pixel_count(pixel_array):
    """Reduziert die Pixelanzahl um die Hälfte."""
    # Neues Array erstellen, das die Hälfte der Pixelanzahl hat
    reduced_array = pixel_array[::2]  # Nur jeden zweiten Pixel nehmen
    return reduced_array


## DEMO-ARRAY
# Anzahl der Werte
num_values = 276480
random_values = np.random.randint(0, 256, size=num_values, dtype=np.uint8)


# ESP32 IP und Port
ESP32_IP = '192.168.0.233'  # IP-Adresse des ESP32
ESP32_PORT = 12345

# Zu sendende Daten (Zahlenwerte zwischen 0 und 255)
#####
#data_to_send = [170, 204, 240, 255]  # Beispiel-Array mit Werten zwischen 0 und 255
#data_to_send = random_values
data_to_send = reduce_pixel_count(image_to_array("graustufenbild_demo.png"))
print(data_to_send)
print(len(data_to_send))
print(len(reduce_pixel_count(data_to_send)))


#####
# TCP-Verbindung zum ESP32 herstellen
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ESP32_IP, ESP32_PORT))

# Sende die Daten als ganze Bytes
for value in data_to_send:
    client_socket.send(bytes([value]))  # Sende den Zahlenwert als einzelnes Byte

# Schließe die Verbindung
client_socket.close()