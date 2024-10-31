import socket
import struct

import numpy as np
import matplotlib.pyplot as plt

class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = None

    def start_connection(self):
        # Verbindung zum Server aufbauen
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_ip, self.server_port))
        
        # IP-Adresse des Clients herausfinden
        client_ip = self.client_socket.getsockname()[0]
        message = f"Client IP: {client_ip} Client MAC: AA:BB:CC:DD:EE:FF Client Secret: Kaesekuchen"
        
        # Sende die Länge des Strings an den Server
        message_length = len(message)
        self.client_socket.send(struct.pack("!I", message_length))
        
        # Sende den String selbst an den Server
        self.client_socket.send(message.encode('utf-8'))
        
        # Empfang einer Antwort vom Server und Ausgabe
        response = self.client_socket.recv(1024).decode('utf-8')
        print("Antwort vom Server:", response)
        
        # Empfang der Länge des uint8-Arrays
        array_length_data = self.client_socket.recv(4)
        (array_length,) = struct.unpack("!I", array_length_data)
        
        # Empfang des uint8-Arrays
        uint8_array = bytearray()
        while len(uint8_array) < array_length:
            packet = self.client_socket.recv(array_length - len(uint8_array))
            if not packet:
                break
            uint8_array.extend(packet)
        
        # Ausgabe des uint8-Arrays
        #print("Empfangenes uint8-Array:", list(uint8_array))
        ### HIER WÜRDE DAS BILD AUF E-INK DARGESTELLT WERDEN ###
        # Auf 138240 Elemente zuschneiden
        uint8_array = uint8_array[:480 * 288]  # kürzt das Array auf die gewünschte Größe
        image = np.reshape(uint8_array, (288, 480)) # ok, die Darstellung ist Böse...

        # Das Bild anzeigen mit Python
        plt.imshow(image, cmap="gray", vmin=0, vmax=255)
        plt.colorbar()  # Optional: Farbskala hinzufügen
        plt.show()
        ### HIER WÜRDE DAS BILD AUF E-INK DARGESTELLT WERDEN ###
        # Schließen der Verbindung
        self.client_socket.close()

# Beispielhafte Verwendung
if __name__ == "__main__":
    # Hier die IP-Adresse und den Port des Servers eingeben
    client = Client("127.0.0.1", 8080)
    client.start_connection()
