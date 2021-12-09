from tkinter import *
from PIL import Image,ImageTk
import pymysql
import mysql.connector

def feed():
    nam1=n.get()
    cont1=m.get()
    cmt=txt.get(1.0,"end-1c")
    con=mysql.connector.connect(host="localhost",user="root",password="",database="carinventory")
    cur=con.cursor()
    cur.execute("insert into feedback(name,contactnumber,comments)values(%s,%s,%s)",(nam1,cont1,cmt))
    con.commit()
    l2=Label(text="Feedback submitted successfully").place(x=100,y=350)

t=Tk()
t.title("Feedback")
t.geometry("500x500")

#Background Design
back=ImageTk.PhotoImage(Image.open("back.jpg"))
l1=Label(t,image=back).place(x=0,y=0,relheight=1,relwidth=1)

name=Label(t,text="Name").place(x=20,y=20)
n=StringVar()
e1=Entry(textvariable=n,width=20).place(x=70,y=20)
number=Label(t,text="Contact").place(x=220,y=20)
m=StringVar()
e2=Entry(textvariable=m,width=20).place(x=280,y=20)
cmt=Label(t,text="Comments").place(x=20,y=80)
txt=Text(t,width=30,height=10)
txt.place(x=100,y=100)
btn=Button(t,text="Submit",command=feed).place(x=220,y=300)

t.mainloop()