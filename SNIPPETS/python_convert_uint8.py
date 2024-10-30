from PIL import Image
import numpy as np

# Lade das BMP-Bild
image_path = 'C:\\Users\\jusch\\Documents\\Arduino\\libraries\\LilyGo-EPD47-master\\examples\\drawImages\\image_for_epaper_red.bmp'  # Pfad zu deinem BMP-Bild
image = Image.open(image_path)

# Konvertiere das Bild in ein numpy-Array
image_array = np.array(image, dtype=np.uint8)

# Überprüfen Sie die Form und den Datentyp des Arrays
print(f"Array shape: {image_array.shape}")
print(f"Array dtype: {image_array.dtype}")

# Optional: Zugriff auf die rohen Pixelwerte
print(image_array)
