from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import scrolledtext
import sys
import os
import webbrowser

def specdisplay():
     os.system("specifications.py")
def gallery(g_url):
    webbrowser.open_new_tab(g_url)
def review(url):
    webbrowser.open_new_tab(url)
def tdrive():
     os.system("testdrive.py")

t=Tk()
t.title("Model X")
t.geometry("1010x500")

back=ImageTk.PhotoImage(Image.open("back.jpg"))
l1=Label(t,image=back).place(x=0,y=0,relheight=1,relwidth=1)

i=Image.open("model2.jpg")
i=i.resize((650,400),Image.ANTIALIAS)
img=ImageTk.PhotoImage(i)
text1=Text(t,height=20,width=80,background="brown",foreground="white")
text1.image_create(END,image=img)
text1.place(x=50,y=20)

spec=Label(t,text="Specifications",bg="brown",font=("Courier",15,"bold"),fg="white",cursor="hand2")
spec.place(x=805,y=100)
spec.bind("<Button-1>",lambda e: specdisplay())

gall=Label(t,text="Gallery",bg="brown",font=("Courier",15,"bold"),fg="white",cursor="hand2")
gall.place(x=805,y=150)
gall.bind("<Button-1>",lambda e: gallery("https://www.autocarindia.com/auto-images/2021-skoda-fabia-image-gallery-420712"))

link=Label(t,text="Customer Reviews",bg="brown",font=("Courier",15,"bold"),fg="white",cursor="hand2")
link.place(x=805,y=200)
link.bind("<Button-1>",lambda e: review("https://www.autox.com/reviews/car-reviews/"))

drive=Label(t,text="Test Drive",bg="brown",font=("Courier",15,"bold"),fg="white",cursor="hand2")
drive.place(x=805,y=250)
drive.bind("<Button-1>",lambda e: tdrive())

t.mainloop()
