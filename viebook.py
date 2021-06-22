# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:32:07 2020

@author: DELL
"""

from tkinter import Canvas,Button,Frame,Label,Tk
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as s

con=s.connect(host="localhost",user="root",passwd="1234",database="mydatabase",auth_plugin='mysql_native_password')
cur=con.cursor()
bookTable="books"
def Viewbook():
    global con,cur,bookTable
    root=Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas3=Canvas(root)
    Canvas3.config(bg="#12a4d9")
    Canvas3.pack(expand=True,fill=BOTH)
    HeadingFrame1=Frame(root,bg="#FFBB00",bd=5)
    HeadingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    Headinglabel=Label(HeadingFrame1,bg="black",fg="white",text="View Books")
    Headinglabel.place(relx=0,rely=0,relheight=1,relwidth=1)
    Labelframe=Frame(root,bg="black")
    Labelframe.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    Label(Labelframe,text="%-10s%-40s%-30s%-20s"%('BID','Title','Author','status'),bg="black",fg="white").place(relx=0.07,rely=0.1)
    Label(Labelframe,text= "----------------------------------------------------------------------------",bg="black",fg="white").place(relx=0.05,rely=0.2)
    
    getBooks = "select * from books "
    y=0.25
    try:
     cur.execute(getBooks)
    
     f=cur.fetchall()
   
     for i in f:
            Label(Labelframe, text="%-10s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    #cur.close()    
    except:
     messagebox.showinfo("Failed to fetch files from database")
    
   
    quitbtn= Button(root,text="Quit",bg='#f7f1e3',fg="black",command=root.destroy)
    quitbtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    root.mainloop()     
      
  
 
         
                                 
    
    
    