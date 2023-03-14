import qrcode

# Get user input
data = input("Enter data for QR code: ")

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Save QR code as PNG file
filename = input("Enter filename for QR code image (without extension): ")
img.save(f"{filename}.png")
