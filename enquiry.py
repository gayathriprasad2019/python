from tkinter import *
from tkcalendar import Calendar
from PIL import ImageTk,Image
from tkcalendar.dateentry import DateEntry
import pymysql
import mysql.connector

def enq():
    name1=n.get()
    number1=m.get()
    model=modset.get()
    timeframe=timset.get()
    commnt=comtext.get(1.0,"end-1c")
    con=mysql.connector.connect(host="localhost",user="root",password="",database="carinventory")
    cur=con.cursor()
    cur.execute("insert into enquiry(name,contactnumber,purchasetimeframe,model,details)values(%s,%s,%s,%s,%s)",(name1,number1,model,timeframe,commnt))
    con.commit()
    lconfirm=Label(bg="white",fg="brown",width=45,text="Thanks for enquiring.\n We will contact you soon").place(x=400,y=440)

t=Tk()
t.title("Enquiry")
t.geometry("800x800")

back_enq=ImageTk.PhotoImage(Image.open("back.jpg"))
l1=Label(t,image=back_enq).place(x=0,y=0,relheight=1,relwidth=1)

name=Label(t,bg="brown",fg="white",text="Name").place(x=20,y=20)
n=StringVar()
e1=Entry(textvariable=n,width=20).place(x=70,y=20)

number=Label(t,bg="brown",fg="white",text="Contact").place(x=220,y=20)
m=StringVar()
e2=Entry(textvariable=m,width=20).place(x=280,y=20)

mod=Label(t,bg="brown",fg="white",text="Model").place(x=20,y=80)
opt1=["Model A","Model B","Model C","Model X"]
modset=StringVar()
modset.set("Model X")
mdrop=OptionMenu(t,modset,*opt1).place(x=120,y=80)

timeframe=Label(t,bg="brown",fg="white",font="bold",text="Purchase Timeframe").place(x=220,y=80)
timopt=["2-3 weeks","1 month","3-8 months","1 year"]
timset=StringVar()
timset.set("Urgent")
timdrop=OptionMenu(t,timset,*timopt).place(x=400,y=80)

comt=Label(t,bg="brown",fg="white",font="bold",text="Details").place(x=20,y=140)
comtext=Text(t,height=20,width=30)
#comscroll=Scrollbar(t,command=comtext.yview)
#comtext.configure(yscrollcommand=comscroll.set)
comtext.tag_configure("small",font=("courier",15,"italic"),justify="left")
comtext.insert(END,'\n\n\nDetail here..\n','small')
comtext.place(x=160,y=140)
#comscroll.pack(side=RIGHT,fill=Y)

enqsubmit=Button(t,text="Submit",command=enq).place(x=350,y=480)

enqlab1=Label(t,text="EDITORIAL ENQUIRIES",bg="white",fg="brown",font=("Tekton Pro",12,"bold")).place(x=525,y=150)
enqlab2=Label(t,text="E-mail: info@autox.com",bg="white",fg="brown",font=("Tekton Pro",8,"bold")).place(x=525,y=180)
enqlab3=Label(t,text="ADVERTISING ENQUIRIES",bg="white",fg="brown",font=("Tekton Pro",12,"bold")).place(x=525,y=240)
enqlab4=Label(t,text="sdigar@autox.com",bg="white",fg="brown",font=("Tekton Pro",8,"bold")).place(x=525,y=270)
enqlab5=Label(t,text="SUBSCRIPTION ENQUIRIES",bg="white",fg="brown",font=("Tekton Pro",12,"bold")).place(x=525,y=330)
enqlab6=Label(t,text="E-mail: info@subscribeautox.com",bg="white",fg="brown",font=("Tekton Pro",8,"bold")).place(x=525,y=360)

t.mainloop()