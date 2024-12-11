import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk

root = tk.Tk()
root.title("SAUSIA-FTC")
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.attributes('-topmost', 1)


label = ttk.Label(root)
label['text'] = "sup"
label.pack()

def getxy(event):    
    print("Position = ({0},{1})".format(event.x, event.y))

canvas = tk.Canvas(root)
background_image = Image.open('university-of-surrey.jpg')
background_image = ImageTk.PhotoImage(background_image)
canvas.pack(fill=tk.BOTH, expand=1)
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
canvas_label = ttk.Label(root, image=canvas)
canvas_label.bind('<Button-1>', getxy)
canvas_label.pack()


try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()

