import tkinter as tk

HEIGHT = 500
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

button = tk.Button(root, text="Log In", )
button.pack()


label = tk.LabelFrame(root, text="Username")
label.place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.05)


label = tk.LabelFrame(root, text="Passworld")
label.place(relx=0.05, rely=0.10, relwidth=0.15, relheight=0.05)

def Uname():
 entry = tk.Entry(root)
 entry.place(relx=0.20, rely=0.05, relwidth=0.15, relheight=0.05)

def Upass():
 entry = tk.Entry(root)
 entry.place(relx=0.20, rely=0.10, relwidth=0.15, relheight=0.05)

Uname()
Upass()
root.mainloop()