# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 11:15:27 2020

@author: DELL
"""
from tkinter import Canvas,Button,Frame,Label,Tk,Entry
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as s
con=s.connect(host="localhost",user="root",passwd="1234",database="mydatabase",auth_plugin='mysql_native_password')
cur=con.cursor()
bookTable="books"
issuetable="issu"
allbid=[]
def returnbook():
    global bookinfo1,bookinfo2,Canvas3,con,cur,bookTable,root,Submit,lb1,lb2,Labelframe
    
   
    root=Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas3=Canvas(root)
    Canvas3.config(bg="#006B38")
    Canvas3.pack(expand=True,fill=BOTH)
    HeadingFrame1=Frame(root,bg="#FFBB00",bd=5)
    HeadingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    Headinglabel=Label(HeadingFrame1,bg="black",fg="white",text="Return Books")
    Headinglabel.place(relx=0,rely=0,relheight=1,relwidth=1)
    Labelframe=Frame(root,bg="black")
    Labelframe.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    lb1=Label(Labelframe,text="Book id",bg="black",fg="white")
    lb1.place(relx=0.05,rely=0.5)
    bookinfo1=Entry(Labelframe)
    bookinfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    Submit=Button(root,text="Return",bg='#d1ccc0',fg="black",command=returnb)
    Submit.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)
    quitbtn=Button(root,text="quit",bg='#d1ccc0',fg="black",command=root.destroy)
    quitbtn.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)
    root.mainloop() 
def returnb():
     global Submit,Labelframe,lb1,bookinfo1,quitbtn,root,Canvas2,status,bookTable,issuetable,con,cur
     bid=bookinfo1.get()
     ex="select * from issu"
     try:
        cur.execute(ex)
        f=cur.fetchall()
        for i in f:
             allbid.append(i[0])
        print(allbid)     
        if int(bid) in allbid:
             checkavail="select * FROM books WHERE bid= '%s'" % (bid,)
             cur.execute(checkavail)
             f=cur.fetchall()
             for i in f:
                 check=i[3]
             print(check)    
             if check=='issued':
                 status=True
             else:
                 status=False
        else:
             messagebox.showinfo("bid is not present")
     except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
         
         
     issuesql="DELETE FROM issu WHERE bid= '%s'" % (bid,)
      
     try:
      if int(bid) in allbid and status==True:
         cur.execute(issuesql)
         con.commit()
         sql="UPDATE books SET  status = %s WHERE bid = %s"
         val = ("avail", int(bid))

         cur.execute(sql,val)
        
         con.commit()
         messagebox.showinfo('Success',"Book Returned Successfully")
      else:
          allbid.clear()
          messagebox.showinfo('Message',"Please check the book ID")
          root.destroy()
          return
     except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
     allbid.clear()
     root.destroy()
     
     
     
