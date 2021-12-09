#from re import L
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image,ImageTk
from tkcalendar.dateentry import DateEntry
from tkinter import messagebox
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
    t6.set(item['values'][6])
    t7.set(item['values'][7])

def drive():
    tm=set.get()
    dt=d.get()
    nm=n.get()
    mob=m.get()
    mdl=modset.get()
    loc=locset.get()
    bookingnumber=mob[6:11]+nm[0:4]
    con=mysql.connector.connect(host="localhost",user="root",password="",database="carinventory")
    cur=con.cursor()
    cur.execute("insert into testdrive(name,contactnumber,date,timeslot,model,location,bookingnumber)values(%s,%s,%s,%s,%s,%s,%s)",(nm,mob,dt,tm,mdl,loc,bookingnumber))
    con.commit()
    dtshow=Label(bg="brown",fg="white",width=45,text="Your drive date is "+dt).place(x=650,y=200)
    tmshow=Label(bg="brown",fg="white",width=45,text="Your time slot is "+tm).place(x=650,y=220)
    bukshow=Label(bg="brown",fg="white",width=45,text="Your booking id is "+bookingnumber).place(x=650,y=240)
    disp=Label(bg="brown",fg="white",width=45,text="Test Drive booked successfully.\nOur Executive will contact you soon\n").place(x=650,y=260)

def can():
    
    cid=c.get()
    print(cid)
    if cid!="":
        con=mysql.connector.connect(host="localhost",user="root",password="",database="carinventory")
        cur=con.cursor()
        q="select * from testdrive where bookingnumber like '%"+cid+"%'"
        cur.execute(q,cid)
        rows=cur.fetchall()
        update(rows)
        if messagebox.askyesno("Confirm Delete?","Are you sure you want to cancel the request?"):
            q2="delete from testdrive where bookingnumber like '%"+cid+"%'"
            cur.execute(q2,cid)
            con.commit()
            disp1=Label(t,bg="brown",fg="white",width=45,text="Test Drive cancelled successfully").place(x=650,y=260)
        else:
            return True
t=Tk()
t.title("Test Drive")
t.geometry("1000x1000")

t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()
t5=StringVar()
t6=StringVar()
t7=StringVar()

#Background Design
back=ImageTk.PhotoImage(Image.open("back.jpg"))
l1=Label(t,image=back).place(x=0,y=0,relheight=1,relwidth=1)

name=Label(t,text="Name").place(x=20,y=20)
n=StringVar()
e1=Entry(textvariable=n,width=20).place(x=70,y=20)

number=Label(t,text="Contact").place(x=220,y=20)
m=StringVar()
e2=Entry(textvariable=m,width=20).place(x=280,y=20)

date=Label(t,text="Date").place(x=20,y=80)
d=StringVar()
edate=DateEntry(t,selectmode='day',locale='en_US',year=2021,date_pattern='y-mm-dd',textvariable=d,width=12, background='darkblue',foreground='white', borderwidth=2)
edate.place(x=70,y=80)

time=Label(t,text="Time").place(x=220,y=80)
opt=["10 AM","11 AM","1 PM","3 PM"]
set=StringVar()
set.set("Any")
tdrop=OptionMenu(t,set,*opt).place(x=280,y=80)

mod=Label(t,text="Model").place(x=20,y=120)
opt1=["Model A","Model B","Model C","Model X"]
modset=StringVar()
modset.set("Model X")
mdrop=OptionMenu(t,modset,*opt1).place(x=70,y=120)

locate=Label(t,text="Location").place(x=220,y=120)
opt2=["Eastfort","Pattom","Vazhuthacaud","Sreekaryam"]
locset=StringVar()
locset.set("Any Showroom")
locdrop=OptionMenu(t,locset,*opt2).place(x=280,y=120)

req=Button(t,text="Submit Request",command=drive).place(x=100,y=320)

trv=ttk.Treeview(t,column=(1,2,3,4,5,6,7),show='headings',height='6')
trv.place(x=50,y=500)
trv.heading(1, text="Name",anchor=W)
trv.heading(2, text="Contact",anchor=W)
trv.heading(3, text="Date",anchor=W)
trv.heading(4, text="Timeslot",anchor=W)
trv.heading(5, text="Model",anchor=W)
trv.heading(6, text="Location",anchor=W)
trv.heading(7, text="Booking Id",anchor=W)

trv.column(1,stretch=YES, minwidth=60, width=80)
trv.column(2,stretch=YES, minwidth=60, width=110)
trv.column(3,stretch=YES, minwidth=60, width=110)
trv.column(4,stretch=YES, minwidth=60, width=110)
trv.column(5,stretch=YES, minwidth=60, width=110)
trv.column(6,stretch=YES, minwidth=60, width=110)
trv.column(7,stretch=YES, minwidth=60, width=110)

trv.bind('<Double 1>',getrow)

buk=Label(t,text="Enter booking id").place(x=20,y=400)
c=StringVar()
ecan=Entry(textvariable=c,width=20).place(x=120,y=400)
cancelreq=Button(t,text="Cancel Request",command=can).place(x=250,y=400)

t.mainloop()