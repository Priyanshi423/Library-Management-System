# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 14:11:36 2020

@author: DELL
"""
"""import mysql.connector
import numpy as np
from tkinter import *
from PIL import ImageTk,Image,ImageChops 
import pymysql#PIL -> Pillow
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks  import *
from Issuebook import *"""

"""db=mysql.connector.connect(host="localhost",user="user",passwwd="gfg")
obj=dataBase.cursor()
obj.execute("CREATE DATABASE GEEKSFORGEEKS")"""

"""from mysql.connector import connection

  
# Connecting from the server 
conn = connection.MySQLConnection(user = 'roott', 
                               host = 'localhost', 
                             passwd="1234") 
  
cur=conn.cursor()
roott=Tk()
roott.title("library management system")
roott.minsize(width=400,height=400)
roott.geometry("600x500")
image=Image.open("lib.jpg")
w,h=image.size
n=0.25
neww=int(w*n)

same=True
if(same):
    newh=int(h*n)
else:
    newh=int(h/n)
backgroundimage=image.resize((neww,newh),Image.ANTIALIAS)   
img=ImageTk.PhotoImage(backgroundimage)
canvas1=Canvas(roott)
canvas1.create_image(300,400,image=img)
canvas1.config(bg="white",width=neww,height=newh)
canvas1.pack(expand=True,fill=BOTH) 
roott.mainloop()
    
# creating database 
#cursorObject.execute("CREATE DATABASE geeks4geeks") """
"""img=Image.open("ff.jpeg")
"""
"""s=img.rotate(-40)
s.save("hy.png")
s=Image.open("hy.png")
s=np.array(img)

img_array=255-s
img=Image.fromarray(img_array)"""

"""img=img.crop((10,10,10,10))
img.show()"""
import sys
#import mysql.connector as s
import mysql.connector
sys.path.append("C:/Users/DELL/Desktop/PROJECTS/library management system")
from addbook import *
from delete import *
from viebook import *
from issue import *
from returnb import *

db=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="mydatabase",auth_plugin='mysql_native_password')





cur=db.cursor()

from tkinter import Canvas,Button,Frame,Label,Tk,Entry
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.title("Library Management")
root.minsize(width=400,height=400)
#roott.geometry("600x500")

from PIL import Image,ImageTk 
n=0.25
Image1=Image.open("C:/Users/DELL/Desktop/PROJECTS/library management system/lib.jpg")
width,height=Image1.size
same=True
newwidth=int(width*n)
if same:
    newheight=  int(height*n)
else:
   newheight=int(height/n)
Image1=Image1.resize((newwidth,newheight),Image.ANTIALIAS)

Canvas2=Canvas(root)
image1=ImageTk.PhotoImage(Image1)


Canvas2.create_image(630,600,image=image1)  
Canvas2.config(bg="red",width=newwidth,height=newheight)
Canvas2.pack(expand=True,fill=BOTH)
#heading
Heading1=Frame(root,bg="#FFBB00",bd=5)
            
Heading1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headinglabel=Label(Heading1,text="Welcome to Data Flair library",bg="black",fg="white",font=("Courier",15))
headinglabel.place(relx=0,rely=0,relwidth=1,relheight=1) 
#buttons 

btn1=Button(root,text="Add Book Details",bg="black",fg="white",command=add)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1) 
btn2=Button(root,text="Delete Book",bg="black",fg="white",command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)  
btn3=Button(root,text="View book list",bg="black",fg="white",command=Viewbook)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)            
btn4=Button(root,text="Issue Book to Student",bg="black",fg="white",command=issuebook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1) 
btn5=Button(root,text="Return",bg="black",fg="white",command=returnbook)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)                        
root.mainloop()
