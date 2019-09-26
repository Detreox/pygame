import tkinter as tk

HEIGHT = 500
WIDTH = 600




def btnpress(urs,pws):
    print("Button Clicked!")
    print(urs)
    print(pws)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

label = tk.LabelFrame(root, text="Username")
label.place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.05)


label = tk.LabelFrame(root, text="Passworld")
label.place(relx=0.05, rely=0.10, relwidth=0.15, relheight=0.05)

def Uname():
 urs = tk.Entry(root)
 urs.place(relx=0.20, rely=0.05, relwidth=0.15, relheight=0.05)
 urs.get()
def Upass():
 pws = tk.Entry(root)
 pws.place(relx=0.20, rely=0.10, relwidth=0.15, relheight=0.05)
 pws.get()

button = tk.Button(root, text="Log In", command=btnpress)
button.pack()

Uname()
Upass()


root.mainloop()