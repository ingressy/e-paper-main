import socket
from PIL import Image
import numpy as np

# Funktion, um eine .bmp-Datei zu laden und in ein uint8_t-Array zu konvertieren
def bmp_to_uint8_array(file_path):
    # Bild öffnen und in Graustufen konvertieren (1 Kanal, 8 Bit pro Pixel)
    img = Image.open(file_path).convert('L')
    
    # Bilddaten in ein numpy-Array umwandeln (dtype uint8)
    img_array = np.array(img, dtype=np.uint8)
    
    # Flach das Bild (um es einfacher zu senden)
    flattened_array = img_array.flatten()
    
    return flattened_array

# Funktion, um den uint8_t-Array über den Socket zu senden
def send_image_data(file_path, server_ip, server_port):
    # Konvertiere das Bild in einen uint8_t-Array
    img_data = bmp_to_uint8_array(file_path)
    
    # TCP-Socket erstellen
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Verbindung zum Server herstellen
        s.connect((server_ip, server_port))
        
        # Die Bilddaten als Bytes senden
        s.sendall(img_data.tobytes())  # .tobytes() konvertiert den numpy-Array in Bytes
        
        print(f"Bilddaten von {file_path} gesendet, Größe: {len(img_data)} Bytes")
        print(img_data.tobytes())

if __name__ == "__main__":
    # Beispiel für das Senden eines BMP-Bildes
    bmp_file = "image_for_epaper.bmp"  # Pfad zur BMP-Datei
    SERVER_IP = "192.168.0.233"  # IP-Adresse des Arduino-Servers
    SERVER_PORT = 12345          # Port des Servers
    
    send_image_data(bmp_file, SERVER_IP, SERVER_PORT)
