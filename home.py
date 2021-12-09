from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import webbrowser
import sys
import os
import pymysql
import mysql.connector

def review(url):
    webbrowser.open_new_tab(url)
def broch(url1):
    webbrowser.open_new_tab(url1)
def feedback():
    os.system("feedback.py")
def choose(i):
    if i==4:
        os.system("modelx.py")
    elif i==2:
        Label(tab2,text="Opening Model B",font=("Lucida Calligraphy",11,"bold"),bg="brown2",fg="white").place(x=250,y=600)
    elif i==3:
        Label(tab2,text="Opening Model C",font=("Lucida Calligraphy",11,"bold"),bg="brown2",fg="white").place(x=250,y=600)
    elif i==1:
        Label(tab2,text="Opening Model A",font=("Lucida Calligraphy",11,"bold"),bg="brown2",fg="white").place(x=250,y=600)
def loan():
    lname=n.get()
    lcont=m.get()
    lmod=modset1.get()
    lfin=finset.get()
    lcmt=comtext1.get(1.0,"end-1c")
    
    con=mysql.connector.connect(host="localhost",user="root",password="",database="carinventory")
    cur=con.cursor()
    cur.execute("insert into loans(name,contact,model,finance,comments)values(%s,%s,%s,%s,%s)",(lname,lcont,lmod,lfin,lcmt))
    con.commit()
    
    ls=Label(tab3,bg="brown",fg="white",width=45,text="Requirements submitted successfully.\nOur Executive will contact you soon\n").place(x=650,y=240)
def usedcar():
    os.system("usedcars.py")
def appointbook():
    testapp=Button(tab4,text="Test Drive",bg="white",fg="firebrick",command=lambda:os.system("testdrive.py")).place(x=220,y=200)
    roomvisit=Button(tab4,text="Service Booking",bg="white",fg="firebrick",command=lambda:os.system("service.py")).place(x=300,y=200)
def enquire():
    os.system("enquiry.py")

t=Tk()
t.geometry("1400x1360")
t.title("Car Shoppy")

#Tab Design
tc=ttk.Notebook(t)
tab1=Frame(tc)
tab2=Frame(tc)
tab3=Frame(tc,bg="grey",width=1400,height=1360)
tab4=Frame(tc)
tab5=Frame(tc)
tab6=Frame(tc)
tc.add(tab1,text="Home")
tc.add(tab2,text="Models")
tc.add(tab3,text="Loans")
#tc.add(tab4,text="Service")
#tc.add(tab5,text="e-Appointment")
tc.add(tab4,text="Contact Us")
tc.pack(expand=1,fill="both")
#Background Design
back=ImageTk.PhotoImage(Image.open("back.jpg"))
l1=Label(tab1,image=back).place(x=0,y=0,relheight=1,relwidth=1)
#Heading Design
head=Label(tab1,text="Drive in Style",font=("Lucida Calligraphy",30,"bold"),pady=5,width=50,height=2,justify="left",fg="white",bg="brown")
head.place(x=0,y=26)
#Review Design
link=Label(tc,text="Customer Reviews",bg="brown",font=("Courier",15,"bold"),fg="white",cursor="hand2")
link.place(x=1160,y=58)
link.bind("<Button-1>",lambda e: review("https://www.autox.com/reviews/car-reviews/"))
#Brochure Design
bro=Label(tc,text="Brochure",bg="brown",font=("Courier",15,"bold"),fg="white",cursor="hand2")
bro.place(x=1160,y=98)
bro.bind("<Button-1>",lambda e: broch("https://www.nissan.in/vehicles/brochures.html"))
#Feedback Design
feed=Label(tc,text="Feedback",bg="brown",font=("Courier",15,"bold"),fg="white",cursor="hand2")
feed.place(x=1160,y=138)
feed.bind("<Button-1>",lambda e: feedback())

text2=Text(tab1,height=50,width=65,background="pink",foreground="firebrick")
scroll=Scrollbar(t,command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure("big",font=("lucida calligraphy",15,"bold","italic"),foreground="firebrick",justify="center")
text2.insert(END,'\n\n\nLatest Models\n\n Trending now..\n\nHit variants\n','big')
text2.place(x=0,y=180)
scroll.pack(side=RIGHT,fill=Y)
#Design Model1
text1=Text(tab1,height=20,width=50,background="black",foreground="black")
img1=Image.open("model2.jpg")
img1=img1.resize((500,320),Image.ANTIALIAS)
car_img1=ImageTk.PhotoImage(img1)
text1.image_create(END,image=car_img1)
text1.place(x=500,y=180)
#Design Model2
text3=Text(tab1,height=20,width=55,background="black",foreground="black")
img2=Image.open("model1.jpg")
img2=img2.resize((450,320),Image.ANTIALIAS)
car_img2=ImageTk.PhotoImage(img2)
text3.image_create(END,image=car_img2)
text3.place(x=900,y=180)
#Design Model3
text5=Text(tab1,height=20,width=50,background="black",foreground="black")
img3=Image.open("model3.jpg")
img3=img3.resize((452,220),Image.ANTIALIAS)
car_img3=ImageTk.PhotoImage(img3)
text5.image_create(END,image=car_img3)
text5.place(x=500,y=480)
#Design Model4
text7=Text(tab1,height=20,width=55,background="black",foreground="black")
img4=Image.open("model4.jpg")
img4=img4.resize((490,220),Image.ANTIALIAS)
car_img4=ImageTk.PhotoImage(img4)
text7.image_create(END,image=car_img4)
text7.place(x=900,y=480)

#Models Design
#Background Design
back_mod=ImageTk.PhotoImage(Image.open("bck.jpg"))
l_mod=Label(tab2,image=back).place(x=0,y=0,relheight=1,relwidth=1)
ind=IntVar()
ch=Label(tab2,text="Choose to drive",bg="brown",fg="white",font=("Tekton Pro",20,"bold")).place(x=25,y=150)
choice1=Button(tab2,text="Model A",width=20,bg="brown",fg="white",font=("Tekton Pro",20,"bold"),command=lambda:choose(1))
choice1.place(x=280,y=220)
choice2=Button(tab2,text="Model B",width=20,bg="brown",fg="white",font=("Tekton Pro",20,"bold"),command=lambda:choose(2))
choice2.place(x=280,y=300)
choice3=Button(tab2,text="Model C",width=20,bg="brown",fg="white",font=("Tekton Pro",20,"bold"),command=lambda:choose(3))
choice3.place(x=280,y=380)
choice4=Button(tab2,text="Model X",width=20,bg="brown",fg="white",font=("Tekton Pro",20,"bold"),command=lambda:choose(4))
choice4.place(x=280,y=460)

#Loans Design
back_loan=ImageTk.PhotoImage(Image.open("bck.jpg"))
l_loan=Label(tab3,image=back).place(x=0,y=0,relheight=1,relwidth=1)
head_loan=Label(tab3,text="Get the best finance option for your dream car",font=("Chaparral Pro",15,"bold"),pady=2,padx=2,height=2,fg="white",bg="brown")
head_loan.place(x=20,y=36)

name_loan=Label(tab3,font="bold",text="Name").place(x=20,y=120)
n=StringVar()
enam=Entry(tab3,textvariable=n,width=20).place(x=100,y=120)

number=Label(tab3,font="bold",text="Contact").place(x=370,y=120)
m=StringVar()
econt=Entry(tab3,textvariable=m,width=20).place(x=450,y=120)

mod=Label(tab3,font="bold",text="Model").place(x=20,y=200)
opt1=["Model A","Model B","Model C","Model X"]
modset1=StringVar()
modset1.set("Model X")
mdrop=OptionMenu(tab3,modset1,*opt1).place(x=100,y=200)

fin=Label(tab3,font="bold",text="Prefered Finance").place(x=20,y=300)
finopt=["HDFC","SBI","IndusInd","Sundaram Finance"]
finset=StringVar()
finset.set("Any")
findrop=OptionMenu(tab3,finset,*finopt).place(x=200,y=300)

comt1=Label(tab3,font="bold",text="Comments").place(x=20,y=400)
comtext1=Text(tab3,height=10,width=50)
comscroll1=Scrollbar(tab3,command=comtext1.yview)
comtext1.configure(yscrollcommand=comscroll1.set)
comtext1.tag_configure("small",font=("courier",15,"italic"),justify="left")
comtext1.insert(END,'\n\n\nAdd any requirements here..\n','small')
comtext1.place(x=200,y=400)
comscroll1.pack(side=RIGHT,fill=Y)

loansubmit=Button(tab3,text="Submit",command=loan).place(x=550,y=600)

#Contact Design
back_contact=ImageTk.PhotoImage(Image.open("back.jpg"))
l_contact=Label(tab4,image=back_contact).place(x=0,y=0,relheight=1,relwidth=1)
#Service Design
serv=Label(tab4,text="Used Cars",bg="brown",font=("Courier",15,"bold"),fg="white",cursor="hand2")
serv.place(x=60,y=60)
serv.bind("<Button-1>",lambda e: usedcar())
#Appointment Design
appoint=Label(tab4,text="e-Appointment",bg="brown",font=("Courier",15,"bold"),fg="white",cursor="hand2")
appoint.place(x=260,y=60)
appoint.bind("<Button-1>",lambda e: appointbook())
#Enquiry Design
enq=Label(tab4,text="Enquiry",bg="brown",font=("Courier",15,"bold"),fg="white",cursor="hand2")
enq.place(x=470,y=60)
enq.bind("<Button-1>",lambda e: enquire())
t.mainloop()