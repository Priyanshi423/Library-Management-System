# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:41:28 2020

@author: DELL
"""
from tkinter import Frame,Label,Canvas,Tk,Entry,Button
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as s
con=s.connect(host="localhost",user="root",passwd="1234",database="mydatabase",auth_plugin='mysql_native_password')
cur=con.cursor()
bookTable="books"

def add():
    global bookinfo1,bookinfo2,bookinfo3,bookinfo4,Canvas1,con,cur,bookTable,root
    root= Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
  
    
    #canvas
    Canvas1= Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
    #heading
    Headingframe= Frame(root,bg="#FFBB00",bd=5)
    Headingframe.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headinglabel=Label(Headingframe,text="ADD BOOKS",bg="black",fg="white",font=("Courier",15))
    headinglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    #fields
    labelframe= Frame(root,bg="black")
    labelframe.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    lb1=Label(labelframe,text="Book ID:",bg="black",fg="white")   
    lb1.place(relx=0.05,rely=0.2,relheight=0.08)
    bookinfo1= Entry(labelframe)
    bookinfo1.place(relx=0.3,rely=0.2,relwidth=0.62,relheight=0.08)
    lb2= Label(labelframe,bg="black",fg="white",text="title")
    lb2.place(relx=0.05,rely=0.35,relheight=0.08)
    bookinfo2= Entry(labelframe)
    bookinfo2.place(relx=0.3,rely=0.35,relwidth=0.62,relheight=0.08)
    lb3= Label(labelframe,bg="black",fg="white",text="author")
    lb3.place(relx=0.05,rely=0.50,relheight=0.08)
    bookinfo3= Entry(labelframe)
    bookinfo3.place(relx=0.3,rely=0.50,relwidth=0.62,relheight=0.08)
    lb4= Label(labelframe,bg="black",fg="white",text="status")
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
    bookinfo4 = Entry(labelframe)
    bookinfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
    #submit button
    Submitbtn= Button(root,text="Submit",bg='#d1ccc0',fg="black",command=bookreg)
    Submitbtn.place(relx=0.28,rely=0.9 ,relwidth=0.18,relheight=0.08)
    quitbtn= Button(root,text="Quit",bg='#f7f1e3',fg="black",command=root.destroy)
    quitbtn.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)
    root.mainloop()  
def bookreg():
    bid=bookinfo1.get()
    title=bookinfo2.get()
    author=bookinfo3.get()
    status=bookinfo4.get()
    status=status.lower()
    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(bid)
    print(title)
    print(author)
    print(status)
    root.destroy()           
             
    
               