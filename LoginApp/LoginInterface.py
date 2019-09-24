import tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

button = tk.Button(root, text="Log In", )
button.pack()

label = tk.LabelFrame(root, text="Username")
label.place(relx=0.8, rely=0, relwidth=0.25, relheight=0.25)

root.mainloop()