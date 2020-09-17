    import requests
    from tkinter import*
    from tkinter import messagebox
    root=Tk()
    root.configure(background="light blue")
    root.geometry("400x600")
    Label(root,text="INDIAN RAILWAY TRAIN FAIR APP",fg="black",bg="light blue",
          font=('Helvetica',15,'bold'),relief="solid").place(x=30,y=20)
    
    Label(root,text="Train Number",font=('Helvetica',12,'bold'),
          relief="solid",width=15).place(x=40,y=70)
    tn=StringVar()
    Entry(root,textvariable=tn).place(x=200,y=71)
    
    Label(root,text="boarding code",font=('Helvetica',12,'bold'),width=15,relief="solid").place(x=40,y=110)
    bc=StringVar()
    Entry(root,textvariable=bc).place(x=200,y=112)
    
    Label(root,text="Destination code",font=('Helvetica',12,'bold'),width=15,relief="solid").place(x=40,y=150)
    dc=StringVar()
    Entry(root,textvariable=dc).place(x=200,y=153)
    
    Label(root,text="Travel Class",font=('Helvetica',12,'bold'),width=15,relief="solid").place(x=40,y=190)
    tc=StringVar(root)
    tc.set("PASSENGER CLASS")
    OptionMenu(root,tc, "AC 2", "AC 3", "SL","GN",).place(x=200,y=190)
    Label(root,text="Train Type",font=('Helvetica',12,'bold'),width=15,relief="solid").place(x=40,y=230)
    Label(root,text="Class Type",font=('Helvetica',12,'bold'),width=15,relief="solid").place(x=40,y=270)
    Label(root,text="Fare",font=('Helvetica',12,'bold'),width=15,relief="solid").place(x=40,y=300)
    
    def show():
        Tn=tn.get()
        start=bc.get()
        end=dc.get()
        response = requests.get("http://indianrailapi.com/api/v2/TrainFare/apikey/25f2c117c32d8cd157c35e29ddf2bc7b/TrainNumber/"+str(Tn)+"/From/"+str(start)+"/To/"+str(end)+"/Quota/GK")    
        data=response.json()
        if(response.status_code==200):    
            Label(root,text=str(data["TrainType"]),font=('Helvetica',12,'bold'),width=15,relief="solid").place(x=200,y=230)
            Label(root,text=str(tc.get()),font=('Helvetica',12,'bold'),relief="solid",width=15).place(x=200,y=270)
            ref={"AC 2":0, "AC 3":1, "SL":2,"GN":3}
            ref1=ref[str(tc.get())]
            fre=data["Fares"][ref1]["Fare"]
            Label(root,text="            ",font=('Helvetica',12,'bold'),relief="solid",width=15).place(x=200,y=300) 
            Label(root,text=str(fre),font=('Helvetica',12,'bold'),relief="solid",width=15).place(x=200,y=300) 
        else:
            messagebox.showinfo("showinfo", "Server error")
    
    
    Button(root,text="Check",command=show,width=10).place(x=60,y=380)  
    Button(root,text="Quit",command=root.destroy,width=10).place(x=200,y=380)    
    root.mainloop()