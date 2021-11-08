
import tkinter as tk
from tkinter import Message ,Text, Canvas
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
from tkinter import StringVar
from tkinter import OptionMenu
from tkinter import Label
from tkinter import messagebox
import smtplib
import random
import re


window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Smart Voting System REGISTRATION Page")
width= window.winfo_screenwidth() 
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
w = Canvas(window, width=width, height=height)
w.pack()
w.create_line(350, 150, 350, 800, fill="#476042", width=3)

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
#answer = messagebox.askquestion(dialog_title, dialog_text)
 
#window.geometry('1280x720')
window.configure(background='blue')

#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

#path = "profile.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
#img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
#panel = tk.Label(window, image = img)


#panel.pack(side = "left", fill = "y", expand = "no")

#cv_img = cv2.imread("img541.jpg")
#x, y, no_channels = cv_img.shape
#canvas = tk.Canvas(window, width = x, height =y)
#canvas.pack(side="left")
#photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img)) 
# Add a PhotoImage to the Canvas
#canvas.create_image(0, 0, image=photo, anchor=tk.NW)

#msg = Message(window, text='Hello, world!')

# Font is a tuple of (font_family, size_in_points, style_modifier_string)



message = tk.Label(window, text=" Voters Registration " ,bg="#000080"  ,fg="white"  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 

message.place(x=100, y=20)

lbl = tk.Label(window, text="Enter Voter ID",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
lbl.place(x=400, y=175)

txt = tk.Entry(window,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txt.place(x=700, y=190)

lbe = tk.Label(window, text="Enter Email ID",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
lbe.place(x=400, y=325)

txte = tk.Entry(window,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txte.place(x=700, y=340)


lbev = tk.Label(window, text="Enter OTP",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
lbev.place(x=400, y=400)

txtev = tk.Entry(window,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txtev.place(x=700, y=415)

lbl2 = tk.Label(window, text="Enter Voter Name",width=20  ,fg="red"  ,bg="yellow"    ,height=2 ,font=('times', 15, ' bold ')) 
lbl2.place(x=400, y=250)

txt2 = tk.Entry(window,width=20  ,bg="yellow"  ,fg="red",font=('times', 15, ' bold ')  )
txt2.place(x=700, y=265)


lbev2 = tk.Label(window, text="Enter admin OTP",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
lbev2.place(x=400, y=475)

txtev2 = tk.Entry(window,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txtev2.place(x=700, y=490)



lbl3 = tk.Label(window, text=" Current Status ",width=20  ,fg="red"  ,bg="yellow"  ,height=2 ,font=('times', 15, ' bold')) 
lbl3.place(x=50, y=200)

message = tk.Label(window, text="" ,bg="yellow"  ,fg="red"  ,width=25  ,height=6, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
message.place(x=20, y=300)

note = tk.Label(window, text="NOTE \n1. Please click on the verify Email \nbutton to get OTP\n2. Please Enter your name without\nspaces and any puctuations\nand special characters" ,bg="yellow"  ,fg="red"  ,width=25  ,height=6, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
note.place(x=20, y=500)

 
def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
def clear3():
    txte.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear4():
    txtev.delete(0, 'end')    
    res = ""
    message.configure(text= res)  
def clear5():
    txtev2.delete(0, 'end')    
    res = ""
    message.configure(text= res)  

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
def TakeImages():        
    Id=(txt.get())
    name=(txt2.get())
    mailId=(txte.get())
    x = re.findall("[a-z]{3}[0-9]{7}", Id)
    #print(len(x),name.isalpha(),otp, txtev.get(), otp1, txtev2.get())
    if(len(x)==1 and name.isalpha() and otp==txtev.get() and otp1==txtev2.get()):
        cam = cv2.VideoCapture(0)
        global Idalpha
        Idalpha=Id[:3]
        Id=Id[3:]
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.2, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                #incrementing sample number 
                sampleNum=sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                #display the frame
                cv2.imshow('frame',img)
            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum>60:
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Registered Face for ID : " + Id +"\n Name : "+ name 
        row = [Id , name, mailId, Idalpha]
        with open('VoterDetails\VoterDetails.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message.configure(text= res)
    else:
        if(len(x)!=1):
            res = "Enter correct Id with 3 alpahabets\n and 7 numbers"
            message.configure(text= res)
        if(name.isalpha() != True):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(len(txte.get())==0):
            res = "Enter Email ID"
            message.configure(text= res)
        if(len(txtev.get())==0):
            res = "Enter OTP sent to your Email ID"
            message.configure(text= res)
        if(txtev.get()==otp):
            res = "Enter correct OTP sent to \nyour Email ID"
            message.configure(text= res)
        if(len(txtev2.get())==otp1):
            res = "Enter correct OTP sent to \nadmin's Email ID"
            message.configure(text= res)
    
def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Face Evaluated"#+",".join(str(f) for f in Id)
    message.configure(text= res)

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids
def send():
    try: 
        s = smtplib.SMTP("smtp.gmail.com" , 587)  # 587 is a port number 
        s.starttls()
        s.login("245117733029@mvsrec.edu.in" , "Sunny@12345")
        global otp,otp1
        otp=random.randint(1000, 9999)
        otp1=random.randint(1000, 9999)
        otp = str(otp)
        otp1 = str(otp1)
        s.sendmail("245117733029@mvsrec.edu.in" , txte.get() , otp)
        s.sendmail("245117733029@mvsrec.edu.in" , "245117733029@mvsrec.edu.in" , otp1)
        messagebox.showinfo("Send OTP via Email", f"OTP sent to {txte.get()} and admin")
        s.quit()
    
    except:
        messagebox.showinfo("Send OTP via Email", "Please enter the valid email address OR check your internet connection")


        
sendMail = tk.Button(window, text="Email verification", command=send  ,fg="red"  ,bg="yellow"  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))

sendMail .place(x=400, y=600)
lbx = tk.Label(window, text="=>",width=2  ,height=1  ,fg="black"   ,font=('times', 20, ' bold ') ) 
lbx.place(x=605, y=600)
  
clearButton = tk.Button(window, text="Clear", command=clear  ,fg="red"  ,bg="yellow"  ,width=20  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=950, y=185)
clearButton2 = tk.Button(window, text="Clear", command=clear2  ,fg="red"  ,bg="yellow"  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton2.place(x=950, y=260)    
clearButton3 = tk.Button(window, text="Clear", command=clear3  ,fg="red"  ,bg="yellow"  ,width=20  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton3.place(x=950, y=335)
clearButton4 = tk.Button(window, text="Clear", command=clear4  ,fg="red"  ,bg="yellow"  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton4.place(x=950, y=410)  
clearButton5 = tk.Button(window, text="Clear", command=clear5  ,fg="red"  ,bg="yellow"  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton5.place(x=950, y=485)
takeImg = tk.Button(window, text="Face Registration", command=TakeImages  ,fg="red"  ,bg="yellow"  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
takeImg.place(x=650, y=600)
lby = tk.Label(window, text="=>",width=2  ,height=1  ,fg="black"   ,font=('times', 20, ' bold ') ) 
lby.place(x=855, y=600)
trainImg = tk.Button(window, text="Face Evaluation", command=TrainImages  ,fg="red"  ,bg="yellow"  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
trainImg.place(x=900, y=600)

quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="red"  ,bg="yellow"  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=1150, y=600)
 
window.mainloop()