from PIL import Image
import numpy as np


def bmp_to_byte_array(image_path):
    # Open the BMP image
    image = Image.open(image_path)
    
    # Ensure the image is in grayscale mode ('L')
    if image.mode != 'L':
        image = image.convert('L')
    
    # Get the pixel data as a flat list of pixel values
    pixel_values = list(image.getdata())
    
    # Convert the pixel values to a byte array
    byte_array = bytearray(pixel_values)
    

    
    return byte_array


def bmp_to_uint8_array(image_path):
    # Open the image in grayscale mode
    image = Image.open(image_path).convert('L')
    
    # Convert image to a NumPy array with dtype uint8
    pixel_array = np.array(image, dtype=np.uint8)
    
    return pixel_array

# Load the JPG image
image_path = 'C://Users//jusch//Documents//Arduino//libraries//LilyGo-EPD47-master//examples//drawImages//rickandmorty.png'
image = Image.open(image_path)

# Set the resolution of your T5 E-Paper display (replace with actual resolution)
display_width = 600
display_height = 448

# Resize the image to match the display resolution
image_resized = image.resize((display_width, display_height))

# Convert the image to black and white (1-bit mode)
image_bw = image_resized.convert('L')  # '1' means 1-bit pixels, black and white

# Save the processed image (optional)
image_bw.save('C://Users//jusch//Documents//Arduino//libraries//LilyGo-EPD47-master//examples//drawImages//image_for_epaper.bmp')

#print(bmp_to_byte_array('C://Users//jusch//Documents//Arduino//libraries//LilyGo-EPD47-master//examples//drawImages//image_for_epaper.bmp'))

image_path = 'C://Users//jusch//Documents//Arduino//libraries//LilyGo-EPD47-master//examples//drawImages//image_for_epaper.bmp'

uint8_array = bmp_to_uint8_array(image_path)

# Optionally save the uint8 array to a binary file
uint8_array.tofile('C://Users//jusch//Documents//Arduino//libraries//LilyGo-EPD47-master//examples//drawImages//image_uint8_data.bin')

# Print out the first 10 values for verification
print(uint8_array.flatten()[:100]) 


# Optionally, you could convert the image into a raw format for your e-paper display driver
#image_bw.save('image_for_epaper.raw')

# To display the image on the E-Paper, you would load it using the display's library.
