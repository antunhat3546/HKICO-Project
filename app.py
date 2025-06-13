import tkinter as tk
from tkinter.font import Font
from PIL import Image, ImageTk

languages = ["English", "Chinese", "Filipino", "Vietnamese"]

win = tk.Tk()

win.title("QR Code displayer")

win.config(bg="white")

en_page = tk.Frame(win, bg="white")
zh_page = tk.Frame(win, bg="white")
tl_page = tk.Frame(win, bg="white")
vn_page = tk.Frame(win, bg="white")

images = []
for lang in languages:
    qrcode_image = Image.open(f"{lang}.png").resize((250, 250))
    qrcode_imagetk = ImageTk.PhotoImage(qrcode_image)
    images.append(qrcode_imagetk)

tk.Label(en_page, text="English", font=Font(family="Arial", size=35), bg="white").pack()
tk.Label(zh_page, text="Chinese", font=Font(family="Arial", size=35), bg="white").pack()
tk.Label(tl_page, text="Filipino", font=Font(family="Arial", size=35), bg="white").pack()
tk.Label(vn_page, text="Vietnamese", font=Font(family="Arial", size=35), bg="white").pack()

tk.Label(en_page, image=images[0], bg="white").pack()
tk.Label(zh_page, image=images[1], bg="white").pack()
tk.Label(tl_page, image=images[2], bg="white").pack()
tk.Label(vn_page, image=images[3], bg="white").pack()

en_page.grid(row=0, column=0)
zh_page.grid(row=0, column=1)
tl_page.grid(row=0, column=2)
vn_page.grid(row=0, column=3)

win.mainloop()