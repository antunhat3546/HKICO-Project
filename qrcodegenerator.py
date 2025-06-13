import qrcode
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

file_location = "https://drive.google.com/file/d/1uHW3YXJHXoXxogZNrF9eXmoh_BeiksBt/view?usp=share_link"

# img = qrcode.make("https://translate.google.com/?sl=en&tl=es&text=example&op=docs")
# img.save("sampleqr4.png")

qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(file_location)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("file_download_qr.png")

win = tk.Tk()

win.title("QR Code generator")

qrcode_image = Image.open("file_download_qr.png")
qrcode_imagetk = ImageTk.PhotoImage(qrcode_image)

image_label = tk.Label(image=qrcode_imagetk)
image_label.pack()

win.mainloop()