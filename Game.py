import random
import time
from tkinter import *


def throw():
    x = random.choice(['1.png', '2.png', '3.png', '4.png', '5.png', '6.png'])
    return x


def img(event):
    global cube1, cube2
    for i in range(6):
        cube1 = PhotoImage(file=(throw()))
        cube2 = PhotoImage(file=(throw()))
        label1['image'] = cube1
        label2['image'] = cube2
        root.update()
        time.sleep(0.15)


root = Tk()
root.geometry('400x200')
root.title('Game of Dice (сделай бросок)')
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file='icon.png'))
font = PhotoImage(file='holst.png')
Label(root, image=font).pack()
label1 = Label(root)
label1.place(relx=0.3, rely=0.5, anchor=CENTER)
label2 = Label(root)
label2.place(relx=0.7, rely=0.5, anchor=CENTER)
root.bind('<1>', img)
img('event')

root.mainloop()
