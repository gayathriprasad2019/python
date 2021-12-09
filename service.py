from tkinter import *
from tkcalendar import Calendar
from PIL import ImageTk,Image
from tkcalendar.dateentry import DateEntry
from tkinter import ttk
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

def servbook():
    vnumb=ent.get()
    model=modset.get()
    date1=d.get()
    owner=n.get()
    cont=m.get()
    #bookingnumber=cont[6:11]+owner[0:4]
    con=mysql.connector.connect(host="localhost",user="root",password="",database="carinventory")
    cur=con.cursor()
    cur.execute("insert into service(veh_num,model,date,owner_name,contactnumber)values(%s,%s,%s,%s,%s)",(vnumb,model,date1,owner,cont))
    con.commit()
    confirm=Label(bg="brown",fg="white",width=45,text="Booking confirmed for vehicle service\nvehicle number: "+vnumb).place(x=450,y=100)
def change():
    #repeat=Label(bg="brown",fg="white",width=45,text="Please enter vehicle number").place(x=450,y=100)
    #cid=c.get()
    vnumb=p1.get()
    model=p2.get()
    date1=p3.get()
    owner=p4.get()
    cont=p5.get()
    con=mysql.connector.connect(host="localhost",user="root",password="",database="carinventory")
    cur=con.cursor()
    q="select * from service where veh_num like '%"+vnumb+"%'"
    cur.execute(q,vnumb)
    rows=cur.fetchall()
    update(rows)
    
    if messagebox.askyesno("Confirm Update?","Are you sure you want to edit the request?"):
    
        con=mysql.connector.connect(host="localhost",user="root",password="",database="carinventory")
        cur=con.cursor()
        q="update service set veh_num=%s,model=%s,date=%s,owner_name=%s,contactnumber=%s where veh_num like '%"+vnumb+"%'"
        cur.execute(q,(vnumb,model,date1,owner,cont))
        con.commit()
        disp1=Label(t,bg="brown",fg="white",width=45,text="Booking details changed successfully").place(x=650,y=260)
    else:
        return True
def can():
    cid=p1.get()
    print(p1)
    con=mysql.connector.connect(host="localhost",user="root",password="",database="carinventory")
    cur=con.cursor()
    q="select * from service where veh_num like '%"+cid+"%'"
    cur.execute(q,cid)
    rows=cur.fetchall()
    update(rows)

    if messagebox.askyesno("Confirm Delete?","Are you sure you want to cancel the request?"):
        q2="delete from service where veh_num like '%"+cid+"%'"
        cur.execute(q2,cid)
        con.commit()
        disp1=Label(t,bg="brown",fg="white",width=45,text="Service booking cancelled successfully").place(x=650,y=260)
    else:
        return True
t=Tk()
t.title("Book Service")
t.geometry("1050x1000")

t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()
t5=StringVar()
t6=StringVar()
t7=StringVar()

back=ImageTk.PhotoImage(Image.open("back.jpg"))
l1=Label(t,image=back).place(x=0,y=0,relheight=1,relwidth=1)

mod=Label(t,text="Model").place(x=20,y=20)
opt1=["Model A","Model B","Model C","Model X"]
modset=StringVar()
modset.set("Model X")
mdrop=OptionMenu(t,modset,*opt1).place(x=120,y=20)

date=Label(t,text="Date").place(x=220,y=20)
d=StringVar()
edate=DateEntry(t,selectmode='day',locale='en_US',year=2021,date_pattern='y-mm-dd',textvariable=d,width=12, background='darkblue',foreground='white', borderwidth=2)
edate.place(x=300,y=20)

vnum=Label(t,text="Vehicle Number").place(x=20,y=60)
ent=StringVar()
eveh=Entry(t,textvariable=ent).place(x=120,y=60)

name=Label(t,text="Owner Name").place(x=20,y=100)
n=StringVar()
e1=Entry(textvariable=n,width=20).place(x=120,y=100)

number=Label(t,text="Contact").place(x=20,y=140)
m=IntVar()
e2=Entry(textvariable=m,width=20).place(x=120,y=140)

book=Button(t,text="Book",command=servbook).place(x=100,y=200)

#buk1=Label(t,text="Enter vehicle number").place(x=20,y=250)
p1=StringVar()
p2=StringVar()
p3=StringVar()
p4=StringVar()
p5=StringVar()
lbl1=Label(t,text="Vehicle Number").place(x=20,y=250)
ent1=Entry(t,textvariable=p1).place(x=120,y=250)
lbl2=Label(t,text="Model").place(x=20,y=290)
ent2=Entry(t,textvariable=p2).place(x=120,y=290)
lbl3=Label(t,text="Date").place(x=20,y=330)
ent3=Entry(t,textvariable=p3).place(x=120,y=330)
lbl4=Label(t,text="Owner Name").place(x=400,y=250)
ent4=Entry(t,textvariable=p4).place(x=500,y=250)
lbl5=Label(t,text="Contact Number").place(x=400,y=290)
ent5=Entry(t,textvariable=p5).place(x=500,y=290)

#c=StringVar()
#ecan=Entry(textvariable=c,width=20).place(x=160,y=250)
editreq=Button(t,text="Edit Details",command=change).place(x=20,y=360)
cancelreq=Button(t,text="Cancel Booking",command=can).place(x=120,y=360)

trv=ttk.Treeview(t,column=(1,2,3,4,5),show='headings',height='6')
trv.place(x=50,y=500)
trv.heading(1, text="Vehicle Number",anchor=W)
trv.heading(2, text="Model",anchor=W)
trv.heading(3, text="Date",anchor=W)
trv.heading(4, text="Owner Name",anchor=W)
trv.heading(5, text="Contact Number",anchor=W)


trv.column(1,stretch=YES, minwidth=60, width=80)
trv.column(2,stretch=YES, minwidth=60, width=110)
trv.column(3,stretch=YES, minwidth=60, width=110)
trv.column(4,stretch=YES, minwidth=60, width=110)
trv.column(5,stretch=YES, minwidth=60, width=110)


trv.bind('<Double 1>',getrow)

t.mainloop()