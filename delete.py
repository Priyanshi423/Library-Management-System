# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 22:44:04 2020

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
def delete():
    global bookinfo1,bookinfo2,Canvas3,con,cur,bookTable,root
    
   
    root=Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas3=Canvas(root)
    Canvas3.config(bg="#006B38")
    Canvas3.pack(expand=True,fill=BOTH)
    HeadingFrame1=Frame(root,bg="#FFBB00",bd=5)
    HeadingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    Headinglabel=Label(HeadingFrame1,bg="black",fg="white",text="delete Books")
    Headinglabel.place(relx=0,rely=0,relheight=1,relwidth=1)
    Labelframe=Frame(root,bg="black")
    Labelframe.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    lb2=Label(Labelframe,text="Book id",bg="black",fg="white")
    lb2.place(relx=0.05,rely=0.5)
    bookinfo1=Entry(Labelframe)
    bookinfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    Submit=Button(root,text="submit",bg='#d1ccc0',fg="black",command=deletebook)
    Submit.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)
    quitbtn=Button(root,text="quit",bg='#d1ccc0',fg="black",command=root.destroy)
    quitbtn.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)
    root.mainloop()        
def deletebook():
      global bookinfo1,bookinfo2,Canvas3,con,cur,bookTable,root,issuetable
      try:
          allbid1=[]
          allbid2=[]
          extractid="select bid from "+bookTable
          cur.execute(extractid)
          for i in cur:
            allbid1.append(i[0])
          extractid="select bid from "+issuetable
          cur.execute(extractid)  
          for i in cur:
            allbid2.append(i[0])
            
          bid=bookinfo1.get()
          
          if(int(bid) in allbid1 or int(bid) in allbid2):
            
          
           a = "DELETE FROM `books` WHERE bid= '%s'" % (bid,)
           cur.execute(a)
           a = "DELETE FROM `issu` WHERE bid= '%s'" % (bid,)
           cur.execute(a)
      
      #cur.execute(a)
           con.commit()
      #cur.execute(b)
           con.commit()
           
           messagebox.showinfo("success")
          else:
              print("please check bid")
      except:
      
          messagebox.showinfo("pleae check id")
      print(bid)
      
      root.destroy()  
    
    