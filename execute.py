from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image  



ws = Tk()
width= ws.winfo_screenwidth() 
height= ws.winfo_screenheight()
ws.geometry("%dx%d" % (width, height))
ws.title('Smart Voting System')

f = ("Times bold", 14)
message = tk.Label(ws, text="Smart Voting System" ,bg="#000080"  ,fg="white"  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
message.place(x=100, y=20)
lbe = tk.Label(ws, text="+",width=5  ,height=1  ,fg="black"   ,font=('times', 35, ' bold ') ) 
lbe.place(x=150, y=425)
lb2 = tk.Label(ws, text="=",width=5  ,height=1  ,fg="black"   ,font=('times', 35, ' bold ') ) 
lb2.place(x=400, y=425)

image1 = Image.open("faceRecog.jpg")
face = ImageTk.PhotoImage(image1)
label1 = tk.Label(image=face)
label1.image = face
label1.place(x=75, y=200)
image2 = Image.open("vote.jpg")
vote = ImageTk.PhotoImage(image2)
label2 = tk.Label(image=vote)
label2.image = vote
label2.place(x=75, y=500)
image3 = Image.open("election.jpg")
election = ImageTk.PhotoImage(image3)
label3 = tk.Label(image=election)
label3.image = election
label3.place(x=550, y=200)

 

def loginPage():
    import login

def registerPage():
    import registerc 
    




loginButton = tk.Button(ws, text="Poll Vote", command=loginPage  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
loginButton.place(x=950, y=250)
registerButton = tk.Button(ws, text="Register Vote", command=registerPage  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
registerButton.place(x=950, y=500)




ws.mainloop()