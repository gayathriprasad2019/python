from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image,ImageTk
from tkcalendar.dateentry import DateEntry
import webbrowser
import pymysql
import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="",database="carinventory")
cur=con.cursor()

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end',values=i)

def getrow(event):
    trv.identify_row(event.y) 
    item=trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])
    
def findcar():
    opt=comb.get()
    #key=searched.get()
    global option
    if opt=="Type":
        opt1=["Hatchback","Sedan","SUV","Van"]
        global modset
        modset=StringVar()
        modset.set("Select Car Type")
        mdrop=OptionMenu(t,modset,*opt1).place(x=400,y=80)
    elif opt=="Budget":
        opt3=["Upto 50000","50000-1 LAC","1 LAC-5 LAC","5 LAC-10 LAC","Above 10 LAC"]
        global rangeset
        rangeset=StringVar()
        rangeset.set("Budget")
        rdrop=OptionMenu(t,rangeset,*opt3).place(x=400,y=80)
    elif opt=="Location":
        opt2=["Trivandrum","Ernakulam","Calicut","Kollam"]
        global locset
        locset=StringVar()
        locset.set("Location")
        locdrop=OptionMenu(t,locset,*opt2).place(x=400,y=80)
    okb=Button(t,text="Ok",bg="brown",fg="white",width=10,command=ok).place(x=400,y=120)
def ok():
    opt=comb.get()
    if opt=="Type":
        choice=modset.get()
        con=mysql.connector.connect(host="localhost",user="root",password="",database="carinventory")
        cur=con.cursor()
        cur.execute("select * from usedcars where type like '%"+choice+"%'")
        rows=cur.fetchall()
        update(rows)
    elif opt=="Budget":
        choice=rangeset.get()
        con=mysql.connector.connect(host="localhost",user="root",password="",database="carinventory")
        cur=con.cursor()
        cur.execute("select * from usedcars where pricerange like '%"+choice+"%'")
        rows=cur.fetchall()
        update(rows)
    if opt=="Location":
        choice=locset.get()
        con=mysql.connector.connect(host="localhost",user="root",password="",database="carinventory")
        cur=con.cursor()
        cur.execute("select * from usedcars where location like '%"+choice+"%'")
        rows=cur.fetchall()
        update(rows)


t=Tk()
t.title("Used Cars")
t.geometry("800x800")

t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()
t5=StringVar()
bck_usd=ImageTk.PhotoImage(Image.open("back.jpg"))
l1=Label(t,image=bck_usd).place(x=0,y=0,relheight=1,relwidth=1)

cap=Label(t,text="IT'S A GOOD TIME TO BUY A USED CAR",bg="brown",fg="white",font=("Chaparral Pro",15,"bold")).place(x=20,y=30)
src=Label(t,text="Search by option",bg="white",fg="brown").place(x=20,y=80)
#searched=StringVar()
#esearch=Entry(t,textvariable=searched).place(x=130,y=80)
comb=ttk.Combobox(t,values=["Type","Budget","Location"])
comb.current(0)
comb.place(x=180,y=80)
sbutton=Button(t,text="Search",bg="white",fg="brown",command=findcar).place(x=40,y=120)

trv=ttk.Treeview(t,column=(1,2,3,4,5),show='headings',height='6')
trv.place(x=50,y=300)
trv.heading(1, text="Vehicle Id",anchor=W)
trv.heading(2, text="Type",anchor=W)
trv.heading(3, text="Price",anchor=W)
trv.heading(4, text="Price Range",anchor=W)
trv.heading(5, text="Location",anchor=W)



trv.column(1,stretch=YES, minwidth=60, width=80)
trv.column(2,stretch=YES, minwidth=60, width=110)
trv.column(3,stretch=YES, minwidth=60, width=110)
trv.column(4,stretch=YES, minwidth=60, width=110)
trv.column(5,stretch=YES, minwidth=60, width=110)



trv.bind('<Double 1>',getrow)
t.mainloop()