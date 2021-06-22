# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 23:09:10 2020

@author: DELL
"""
from tkinter import Canvas,Button,Frame,Label,Tk,Entry
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as s
con=s.connect(host="localhost",user="root",passwd="1234",database="mydatabase",auth_plugin='mysql_native_password')
cur=con.cursor(buffered=TRUE)
bookTable="books"
issuetable="issu"
allbid=[]
def issue():
    global bookinfo1,bookinfo2,Canvas3,con,cur,bookTable,root,Submit,lb1,lb2,Labelframe
    
    bid=bookinfo1.get()
    
    issueto=bookinfo2.get()
    
    Submit.destroy()
    Labelframe.destroy()
    lb1.destroy()
    bookinfo1.destroy()
    bookinfo2.destroy()
    extractid="select bid from "+bookTable
    
    
    cur.execute(extractid)
   
    for i in cur:
            allbid.append(i[0])
        
            
     
    try:       
     if int(bid) in allbid:
            checkstatus="select * FROM books WHERE bid= '%s'" % (bid,)
            
            cur.execute(checkstatus)
            f=cur.fetchall()
            #print(checkstatus)
           
            for i in f:
                check=i[3]
            if check=="avail":
                status=True
            else:
                status=False
     else:
            messagebox.showinfo("bid not available")
    except:
          messagebox.showinfo('error')
    
    #issuesql="insert into "+issuetable+"values ('"+bid+"','"+issueto+"')"
    
    #show="select *from "+issuetable
     
    #updatebook="update "+bookTable+"set status='issued' where id='"+bid+"'"
    
    try:
     if int(bid) in allbid and status==True:
            cur.execute('insert into issu(bid,issueto) values("%d","%s")' % (int(bid),issueto))
            con.commit()
            sql="UPDATE books SET  status = %s WHERE bid = %s"
            val = ("issued", int(bid))

            cur.execute(sql,val)
            con.commit()
            messagebox.showinfo("issued")
            root.destroy()
     else:
             allbid.clear()
             messagebox.showinfo("book already issued")
             root.destroy()
             return
    except:
         messagebox.showinfo("Search Error","The value entered is wrong, Try again")

    print(bid)
    print(issueto) 
    
   
    allbid.clear()

def issuebook():
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
    Headinglabel=Label(HeadingFrame1,bg="black",fg="white",text="Issue Books")
    Headinglabel.place(relx=0,rely=0,relheight=1,relwidth=1)
    Labelframe=Frame(root,bg="black")
    Labelframe.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    lb1=Label(Labelframe,text="Book id",bg="black",fg="white")
    lb1.place(relx=0.05,rely=0.5)
    bookinfo1=Entry(Labelframe)
    bookinfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    lb2=Label(Labelframe,text="Issued to",bg="black",fg="white")
    lb2.place(relx=0.05,rely=0.4)
    bookinfo2=Entry(Labelframe)
    bookinfo2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    Submit=Button(root,text="Issue",bg='#d1ccc0',fg="black",command=issue)
    Submit.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)
    quitbtn=Button(root,text="quit",bg='#d1ccc0',fg="black",command=root.destroy)
    quitbtn.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)
    root.mainloop()   
    
    
    


    
                
    
          
