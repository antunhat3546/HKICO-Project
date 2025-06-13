import qrcode
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from deep_translator import GoogleTranslator

win = tk.Tk()

win.title("QR Code generator")

file_location = ""
languages = ["English", "Chinese", "Filipino", "Vietnamese"]

def upload():
    global file_location

    try:
        file_location = filedialog.askopenfilename(defaultextension="txt", filetypes=(
            ("Text files", "*.txt"),
            ("PDF files", "*.pdf"),
            ("Word documents", "*.docx"),
            ("All files", "*.*")
        ))

        file_label.config(text=f"File location: {file_location[:30]}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def generate():
    global file_location

    with open(file_location, "r") as file:
        data = file.read()

    if lang_var.get() == "English":
        transdata = GoogleTranslator(target="en").translate(data)
    elif lang_var.get() == "Chinese":
        transdata = GoogleTranslator(target="zh-CN").translate(data)
    elif lang_var.get() == "Filipino":
        transdata = GoogleTranslator(target="tl").translate(data)
    elif lang_var.get() == "Vietnamese":
        transdata = GoogleTranslator(target="vi").translate(data)

    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(transdata)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    img.save(f"{os.path.basename(file_location)}.png")

file_label = tk.Label(win, text="File location: None")
file_label.grid(row=0, column=0, columnspan=2, padx=2, pady=2)

ttk.Button(win, text="Upload file", command=upload).grid(row=1, column=0, columnspan=2, padx=2, pady=2)

tk.Label(win, text="Language: ").grid(row=2, column=0, padx=2, pady=2)

lang_var = tk.StringVar(value="English")
ttk.Combobox(win, textvariable=lang_var, values=languages, state="readonly").grid(row=2, column=1, padx=2, pady=2)

ttk.Button(win, text="Generate", command=generate).grid(row=3, column=0, columnspan=2, padx=2, pady=2)

win.mainloop()