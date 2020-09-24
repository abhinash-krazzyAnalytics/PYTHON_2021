# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:02:04 2020

@author: Abhinash
"""

#Basic Program

import PyPDF2
import pyttsx3

book=open(r'C:\Users\Abhinash\Downloads\childrensrhymes.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
print(pages)

pn=int(input("Enter page number to read :"))
try:
   speaker=pyttsx3.init()
   speaker.setProperty('rate', 150) 
   # Set volume 0-1 
   speaker.setProperty('volume', 0.7) 
   page=pdfreader.getPage(pn)
   text=page.extractText()
   speaker.say(text)
   speaker.runAndWait()
except:
    print("Page number enter is not present in book")
    print(pages)
    
#Tkinter Application
    

import PyPDF2
import pyttsx3

# import all components 
# from the tkinter library 
from tkinter import *
# import filedialog module 
from tkinter import filedialog 



# Function for opening the 
# file explorer window 
def browseFiles(): 
    global filename
    filename = filedialog.askopenfilename(initialdir = "/", 
										title = "Select a File", 
								filetypes =(("Text files","*.txt*"),("all files", "*.*")))
														 
												 
													
    label_file_explorer.configure(text="File Opened: "+filename)
    
def audio():
    goto=pn.get()
    book=open(filename,'rb')
    pdfreader=PyPDF2.PdfFileReader(book)
    pages=pdfreader.numPages
    print(pages)
    speaker=pyttsx3.init()
    speaker.setProperty('rate', 150) 
    # Set volume 0-1 
    speaker.setProperty('volume', 0.7) 
    page=pdfreader.getPage(int(goto))
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()

																								
# Create the root window 
window = Tk() 

#Window Title
window.title("PDF_TO_AUDIO")

# Set window title 
window.title('File Explorer') 

# Set window size 
window.geometry("400x300") 

#Set window background color 
window.config(background = "light yellow") 

Label(window,text="PDF TO AUDIO PLAYER",font=('Helvetica',15,'bold'),
               bg='light yellow',relief='solid').pack()
Label(window,text="GO TO PAGE NO",font=8).place(x=50,y=100)

# Create a File Explorer label 
label_file_explorer = Label(window, 
							text = "File Explorer using Tkinter", 
							 fg = "blue") 

	
button_explore = Button(window, 
						text = "Browse Files", 
						command = browseFiles) 
Button(window,text="audio",command=audio,width=15).place(x=50,y=140)

pn=StringVar()
Entry(window,textvariable=pn).place(x=200,y=100) 

Button(window, text = "Exit",width=15, 
		command = window.destroy).place(x=200,y=140) 

# Grid method is chosen for placing 
# the widgets at respective positions 
# in a table like structure by 
# specifying rows and columns 
label_file_explorer.pack()

button_explore.pack()

# Let the window wait for any events 
window.mainloop() 

