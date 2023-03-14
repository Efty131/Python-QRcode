from pyzbar.pyzbar import decode
from PIL import Image

# Load image containing the QR code
filename = input("Enter the filename of the image: ")
img = Image.open(filename)

# Decode the QR code
data = decode(img)

# Print the QR code data
if len(data) > 0:
    print(f"QR code data found: {data[0].data.decode()}")
else:
    print("No QR code data found in the image.")
