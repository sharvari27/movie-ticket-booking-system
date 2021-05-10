from tkinter import*
from tkinter import Tk,StringVar,ttk
import random
import time;
import datetime

root = Tk()
root.geometry("1350x750+0+0")
root.title("movie management")
root.configure(background='white')

Tops=Frame(root,width=1350,height=100,bd=14 , relief="raise")
Tops.pack(side=TOP)

f1=Frame(root,width=900,height=650,bd=8,relief="raise")
f1.pack(side=LEFT)
f2=Frame(root,width=440,height=650,bd=8,relief="raise")
f2.pack(side=RIGHT)

frametopRight=Frame(f2,width=440,height=650,bd=12,relief="raise")
frametopRight.pack(side=TOP)
framebottomRight=Frame(f2,width=440,height=50,bd=16,relief="raise")
framebottomRight.pack(side=BOTTOM)

f1a=Frame(f1,width = 900,height=330,bd=8,relief="raise")
f1a.pack(side=TOP)
f2a=Frame(f1,width=900,height=320,bd=6,relief="raise")
f2a.pack(side=BOTTOM)

topLeft1 = Frame(f1a,width=300,height=250,bd=16,relief="raise")
topLeft1.pack(side=LEFT)
topLeft2 = Frame(f1a,width=300,height=250,bd=16,relief="raise")
topLeft2.pack(side=RIGHT)
topLeft3 = Frame(f1a,width=300,height=250,bd=16,relief="raise")
topLeft3.pack(side=RIGHT)

bottomLeft1= Frame(f2a,width=350,height=350,bd=14,relief="raise")
bottomLeft1.pack(side=LEFT)

bottomLeft2=Frame(f2a,width=350,height=350,bd=14,relief="raise")
bottomLeft2.pack(side=RIGHT)

Tops.configure(background='white')
f1.configure(background='white')
f2.configure(background='white')
lb1Title=Label(Tops,font=('arial',50,'bold'),text="           Movie Information System      ",bd=15,width=41,anchor='w')
lb1Title.grid(row=0,column=0)

#date and time
Date1=StringVar()
Time1=StringVar()
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=StringVar()
var5=IntVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
Tax=StringVar()
SubTotal=StringVar()
Total=StringVar()

var1.set("0")
var4.set("0")
var6.set("0")
var7.set("0")
var8.set("0")

lb1Receipt=Label(frametopRight,font=('arial',14,'bold'),text=" Information ",bd=10,width=18,justify='center')
lb1Receipt.grid(row=0,column=0)


lb1Price1=Label(framebottomRight,font=('arial',14,'bold'),text="Price" ,  width=8,relief='sunken',justify='center')
lb1Price1.grid(row=6,column=1)
lb1Price2=Label(framebottomRight,font=('arial',14,'bold'),  width=8,relief='sunken',textvariable=Total,justify='center')
lb1Price2.grid(row=6,column=2)

lb1Time1=Label(framebottomRight,font=('arial',14,'bold'),text="Time" ,  width=8,relief='sunken',justify='center')
lb1Time1.grid(row=3,column=0)
lb1Time2=Label(framebottomRight,font=('arial',14,'bold'),  width=8,relief='sunken',textvariable=Time1,justify='center')
lb1Time2.grid(row=4,column=0)


lb1Date1=Label(framebottomRight,font=('arial',14,'bold'),text="Date" ,  width=8,relief='sunken',justify='center')
lb1Date1.grid(row=3,column=2)
lb1Date2=Label(framebottomRight,font=('arial',14,'bold'),  width=8,relief='sunken',textvariable=Date1,justify='center')
lb1Date2.grid(row=4,column=2)
#-----------------------------------------------------------------------------------------------------------------------------------

def Reset():
    var1.set("0")
    var5.set("0")
    var7.set("0") 
    var6.set("0")
    var8.set("0")
    Total.set("0")
    Tax.set("0")

def Movie_Cost():
    if (var1.get()==150):
        st="rs",str(15)
        Tax.set(st)
        T="rs",str(var5.get()*150+var5.get()*15)
        Total.set(T)
    elif var1.get()==200 :
        st="rs",str(20)
        Tax.set(st)
        T="rs",str(var5.get()*200+var5.get()*20)
        Total.set(T)  
    elif var1.get()==300:
        st="rs",str(30)
        Tax.set(st)
        T="rs",str(var5.get()*300+var5.get()*30)
        Total.set(T)
    else:
        st="rs 0"
        Tax.set(st)
        T="rs 0"
        Total.set(T)
       
        
        
#date and time
Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime('%H:%M:%S'))

lb1Class=Label(topLeft1,font=('arial',18,'bold'),text='Seats in Class',bd=8,width=15)
lb1Class.grid(row=0,column=0,sticky=W)

chkGold=Radiobutton(topLeft1,font=('arial',14,'bold'),text='Gold',variable=var1,value=150)
chkGold.grid(row=1,column=0,sticky=W)
chkDiamond=Radiobutton(topLeft1,font=('arial',14,'bold'),text='Diamond',variable=var1,value=200)
chkDiamond.grid(row=2,column=0,sticky=W)
chkPlatinum=Radiobutton(topLeft1,font=('arial',14,'bold'),text='Platinum',variable=var1,value=300)
chkPlatinum.grid(row=3,column=0,sticky=W)


lb1Genre=Label(topLeft3,font=('arial',16,'bold'),text='Select a GENRE',bd=8)
lb1Genre.grid(row=0,column=0,sticky=W)
cboGenre=ttk.Combobox(topLeft3,textvariable=var4,state='readonly',font=('arial',12,'bold'),width=15)
cboGenre['value']=('','National','Comedy','Romantic','Thriller','Horror','sci-fi','animation') 
cboGenre.current(0)
cboGenre.grid(row=0,column=1,sticky=W)

lb1Class=Label(topLeft2,font=('arial',14,'bold'),text='Tickets',bd=8)
lb1Class.grid(row=0,column=0,sticky=W)

lb1Number=Label(topLeft2,font=('arial',14,'bold'),text='No of Tickets',bd=8)
lb1Number.grid(row=1,column=0,sticky=W)
entSingle=Entry(topLeft2,font=('arial',14,'bold'),textvariable=var5,bd=2,width=15)
entSingle.grid(row=1,column=1,sticky=W)

lb1Ticket1=Label(framebottomRight,font=('arial',14,'bold'),text=" Ticket", width=8,relief='sunken',justify='center')
lb1Ticket1.grid(row=0,column=1)
lb1Ticket2=Label(framebottomRight,textvariable=var5,font=('arial',14,'bold'), width=8,relief='sunken',justify='center')
lb1Ticket2.grid(row=1,column=1)

lb1Cinema=Label(bottomLeft2,font=('arial',16,'bold'),text='Select a cinema near you',bd=8)
lb1Cinema.grid(row=1,column=0,sticky=W)
cboCinema=ttk.Combobox(bottomLeft2,textvariable=var6,state='readonly',font=('arial',12,'bold'),width=15)
cboCinema['value']=('','ashok anil','Big cinemas','Xbox','Sarvoday','poplo') 
cboCinema.current(0)

cboCinema.grid(row=1,column=1,sticky=W)
lb1Cinema1=Label(framebottomRight,font=('arial',14,'bold'),text=" Cinema",  width=8,relief='sunken',justify='center')
lb1Cinema1.grid(row=0,column=0)
lb1Cinema2=Label(framebottomRight ,textvariable=var6,font=('arial',14,'bold'),  width=8,relief='sunken',justify='center')
lb1Cinema2.grid(row=1,column=0)


lb1Movie=Label(bottomLeft2,font=('arial',16,'bold'),text='Select a Movie',bd=8)
lb1Movie.grid(row=0,column=0,sticky=W)
cboMovie=ttk.Combobox(bottomLeft2,textvariable=var7,state='readonly',font=('arial',12,'bold'),width=15)
cboMovie['value']=('','Jai ho','Indian','Army','Border','Hera Pheri','IT','who Killed Jessica','Prem Ratan','raw','WAR','URI','Finding Nemo') 
cboMovie.current(0)
cboMovie.grid(row=0,column=1,sticky=W)
lb1Movie1=Label(framebottomRight,font=('arial',14,'bold'),text="Movie " ,  width=8,relief='sunken',justify='center')
lb1Movie1.grid(row=0,column=2)
lb1Movie2=Label(framebottomRight,textvariable=var7,font=('arial',14,'bold'),  width=8,relief='sunken',justify='center')
lb1Movie2.grid(row=1,column=2)

lblSpace = Label(bottomLeft2,font=('arial',14,'bold'),text="         \n      ",bd=16,anchor='w')
lblSpace.grid(row=1,column=3)
#----------------------------------------------------------------------------------Total and Subtotal----------------------------------------------------------------------

lb1StateTax=Label(bottomLeft1,font=('arial',14,'bold'),text='Statetax',bd=8,anchor='w')
lb1StateTax.grid(row=3,column=2)
txtStateTax=Entry(bottomLeft1,font=('arial',14,'bold'),textvariable=Tax,bd=10,insertwidth=4,
                  justify='right')
txtStateTax.grid(row=3,column=3)

lblSpace = Label(bottomLeft1,font=('arial',14,'bold'),text="              ",bd=16,anchor='w')
lblSpace.grid(row=4,column=2)

lb1TotalCost=Label(bottomLeft1,font=('arial',14,'bold'),text='Total Cost',bd=8,anchor='w')
lb1TotalCost.grid(row=5,column=2)
txtTotalCost=Entry(bottomLeft1,font=('arial',14,'bold'),textvariable=Total,bd=10,insertwidth=4,justify='right')
txtTotalCost.grid(row=5,column=3)

lblSpace = Label(bottomLeft1,font=('arial',14,'bold'),text="             ",bd=16,anchor='w')
lblSpace.grid(row=8,column=2)

lblSpace = Label(bottomLeft1,font=('arial',14,'bold'),text="               ",bd=16,anchor='w')
lblSpace.grid(row=8,columnspan=4)

#------------------------------------------------------------------------------------------
lblSp= Label(framebottomRight,font=('arial',14,'bold'),width=25,height=1,relief='sunken',justify='center')
lblSp.grid(row=7,columnspan=4)

lblSp= Label(framebottomRight,font=('arial',14,'bold'),width=25,height=1,relief='sunken',justify='center')
lblSp.grid(row=5,columnspan=4)

lblSp= Label(framebottomRight,font=('arial',14,'bold'),width=25,height=1,relief='sunken',justify='center')
lblSp.grid(row=2,columnspan=4)


btnTotal=Button(framebottomRight,text='Total',padx=2,pady=2,bd=2,fg="black",
                font=('arial',12,'bold'),width=6,height=1,command=Movie_Cost).grid(row=8,column=0)

btnClear=Button(framebottomRight,text='Clear',padx=2,pady=2,bd=2,fg="black",
                font=('arial',12,'bold'),width=6,height=1,command=Reset).grid(row=8,column=1)

'''btnReset=Button(framebottomRight,text='Reset',padx=2,pady=2,bd=2,fg="black",
                font=('arial',12,'bold'),width=6,height=1).grid(row=7,column=2)'''

btnExit=Button(framebottomRight,text='Exit',padx=2,pady=2,bd=2,fg="black",
                font=('arial',12,'bold'),width=6,height=1,command=quit).grid(row=8,column=2)


root.mainloop()














































































