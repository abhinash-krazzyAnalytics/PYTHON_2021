# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:17:20 2020

@author: Abhinash
"""

##################REGISTRATION FORM###########################
from tkinter import*

root=Tk()
root.geometry('500x600')
root.title("Registration form")

fn=StringVar()
ln=StringVar()
db=StringVar()
var=StringVar()

def printt():
    first=fn.get()
    last=ln.get()
    dob1=db.get()
    var1=var.get()
    print(f"Your FullName is {first}{last}")
    print(f"Your FullName is {dob1}")
    print(f"Your FullName is {var1}")


def exitt():
    exit()
label_0=Label(root, text="registration form", relief="solid",width=20, font=('arial',19,'bold'))
label_0.place(x=90, y=150)

label_1=Label(root, text="First Name",width=20, font=('bold',10))
label_1.place(x=80, y=240)
entry_1=Entry(root,textvar=fn)
entry_1.place(x=240,y=242)



label_2=Label(root, text="Last Name",width=20, font=('bold',10))
label_2.place(x=80, y=280)
entry_2=Entry(root,textvar=ln)
entry_2.place(x=240,y=282)

label_3=Label(root, text="Date of birth",width=20, font=('bold',10))
label_3.place(x=65, y=320)
entry_3=Entry(root,textvar=db)
entry_3.place(x=240,y=320)

label_4=Label(root, text="Country",width=20, font=('bold',10))
label_4.place(x=75, y=370)
list=["INDIA","USA","CANADA",'CHINA',"jAPAN"]
var=StringVar()
drop_list=OptionMenu(root,var,*list)
var.set("select country")
drop_list.config(width=15)
drop_list.place(x=230,y=370)


button_sign=Button(root,text='Signup',width=12,bg='brown',fg='white',command=printt).place(x=150,y=450)
button_out=Button(root,text='Outup',width=12,bg='brown',fg='white',command=exitt).place(x=280,y=450)
root.mainloop()

