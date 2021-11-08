

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
window.title("Smart Voting System LOGIN Page")
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



message = tk.Label(window, text="Poll Your Vote" ,bg="#000080"  ,fg="white"  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 

message.place(x=100, y=20)

lbl = tk.Label(window, text="Enter Voter ID",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
lbl.place(x=400, y=180)

txt = tk.Entry(window,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txt.place(x=700, y=195)

lbe = tk.Label(window, text="Enter Email ID",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
lbe.place(x=400, y=340)

txte = tk.Entry(window,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txte.place(x=700, y=355)


lbev = tk.Label(window, text="Enter OTP",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
lbev.place(x=400, y=420)

txtev = tk.Entry(window,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txtev.place(x=700, y=435)

lbl2 = tk.Label(window, text="Enter Voter Name",width=20  ,fg="red"  ,bg="yellow"    ,height=2 ,font=('times', 15, ' bold ')) 
lbl2.place(x=400, y=260)

# Dropdown menu options
options = [
    "NOTA",
    "Candidate 1",
    "Candidate 2",
    "Candidate 3",
    "Candidate 4"
]
  
# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "NOTA" )
  
# Create Dropdown menu
drop = OptionMenu( window , clicked , *options )
drop.config( bg="yellow"  ,fg="red"  ,width=30  ,height=2, activebackground = "yellow", font=('times', 15, 'bold'))
drop.pack()
drop.place(x=700, y=505)


txt2 = tk.Entry(window,width=20  ,bg="yellow"  ,fg="red",font=('times', 15, ' bold ')  )
txt2.place(x=700, y=275)

lbl3 = tk.Label(window, text=" Current Status ",width=20  ,fg="red"  ,bg="yellow"  ,height=2 ,font=('times', 15, ' bold')) 
lbl3.place(x=50, y=200)

message = tk.Label(window, text="" ,bg="yellow"  ,fg="red"  ,width=25  ,height=6, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
message.place(x=20, y=300)

note = tk.Label(window, text="NOTE \n1. Please click on the verify Email \nbutton to get OTP\n2. Please Enter your name without\nspaces and any puctuations\nand special characters" ,bg="yellow"  ,fg="red"  ,width=25  ,height=6, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
note.place(x=20, y=500)

lbl3 = tk.Label(window, text="Poll vote : ",width=20  ,fg="red"  ,bg="yellow"  ,height=2 ,font=('times', 15, ' bold')) 
lbl3.place(x=400, y=510)


 
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
        global otp
        otp=random.randint(1000, 9999)
        otp = str(otp)
        s.sendmail("245117733029@mvsrec.edu.in" , txte.get() , otp)
        messagebox.showinfo("Send OTP via Email", f"OTP sent to {txte.get()}")
        s.quit()
    
    except:
        messagebox.showinfo("Send OTP via Email", "Please enter the valid email address OR check an internet connection")

def TrackImages():
    Vote=(clicked.get())
    Id=(txt.get())
    name=(txt2.get())
    x = re.findall("[a-z]{3}[0-9]{7}", Id)
    global Idalpha,IdwithoutAlpha
    Idalpha=Id[:3]
    Id=Id[3:]
    IdwithoutAlpha=Id
    if(len(x)==1 and name.isalpha() and len(txte.get())>0 and len(txtev.get())>0):

        recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
        recognizer.read("trainingImageLabel/Trainner.yml")
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath)  
        df=pd.read_csv("VoterDetails\\VoterDetails.csv")
        global MailFromDetails, IdalphaFromDetails
        MailFromDetails=df.loc[df['Id'] == int(IdwithoutAlpha)]['mail'].values
        IdalphaFromDetails=df.loc[df['Id'] == int(IdwithoutAlpha)]['code'].values

        cam = cv2.VideoCapture(0)
        df['Vote']=Vote
        font = cv2.FONT_HERSHEY_SIMPLEX        
        col_names =  ['Id','Name','email','Vote','Date','Time','code']
        votings = pd.DataFrame(columns = col_names)  
        aa=''
        Id=0
        #messagebox.showinfo("error",f"Invalid credentials {txte.get()} {MailFromDetails[0]} {type(txte.get())} {type(MailFromDetails)}")

        while True:
            _ret, im =cam.read()
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray, 1.2,5)    
            for(x,y,w,h) in faces:
                cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
                if(conf < 50):
                    ts = time.time()  
                    global bb,date,timeStamp    
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa=df.loc[df['Id'] == Id]['Name'].values
                    bb=df.loc[df['Id'] == Id]['Vote'].values
                    tt=aa
                else:
                    Id='Unknown'                
                    tt=str(Id)  
                if(conf > 75):
                    noOfFile=len(os.listdir("ImagesUnknown"))+1
                    cv2.imwrite("./ImagesUnknown/Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
                cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
            
            cv2.imshow('im',im) 
            if (cv2.waitKey(1)==ord('q') ):
                break
        if aa[0]==txt2.get() and Id==int(IdwithoutAlpha) and otp==txtev.get() and MailFromDetails[0]==txte.get() and IdalphaFromDetails[0]==Idalpha:  
            votings.loc[len(votings)] = [IdwithoutAlpha,txt2.get(),txte.get(),bb,date,timeStamp,Idalpha]
            votings= votings.drop_duplicates(subset=['Id'],keep='first')           
            ts = time.time()      
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            Hour,Minute,Second=timeStamp.split(":")
            fileName="Votes\\Votes.csv"
            df=pd.read_csv(fileName)
            flag=1
            CheckVote=df['Id'].values.tolist()
            for i in CheckVote:
                if i==int(IdwithoutAlpha):
                    flag=0
            if flag==1:
                vv=[IdwithoutAlpha,txt2.get(),txte.get(),bb,date,timeStamp,Idalpha]
                with open(fileName,'a+') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(vv)
                csvFile.close()
                #votings.to_csv(fileName,index=False)
                cam.release()
                cv2.destroyAllWindows()
                res=votings
                messagebox.showinfo("sucess",f" Thank You for using your valuable vote")
            else:
                messagebox.showinfo("failure",f" You have already voted")
        else:

            messagebox.showinfo("error",f"Invalid credentials")
            #{aa[0]} {txt2.get()} {Id} {int(IdwithoutAlpha)} {otp} {txtev.get()} {MailFromDetails[0]} {txte.get()} {Idalpha} {IdalphaFromDetails[0]}
            #{aa[0]} {txt2.get()} {Id} {int(IdwithoutAlpha)} {otp} {txtev.get()} {MailFromDetails[0]} {txte.get()} {Idalpha} {IdalphaFromDetails[0]} 
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
        
sendMail = tk.Button(window, text="Email verification", command=send  ,fg="red"  ,bg="yellow"  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))

sendMail .place(x=400, y=600)

  
clearButton = tk.Button(window, text="Clear", command=clear  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=950, y=180)
clearButton2 = tk.Button(window, text="Clear", command=clear2  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton2.place(x=950, y=260)   
clearButton3 = tk.Button(window, text="Clear", command=clear3  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton3.place(x=950, y=340)
clearButton4 = tk.Button(window, text="Clear", command=clear4  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton4.place(x=950, y=420)  

lby = tk.Label(window, text="=>",width=2  ,height=1  ,fg="black"   ,font=('times', 25, ' bold ') ) 
lby.place(x=625, y=600)

trackImg = tk.Button(window, text="Face verification", command=TrackImages  ,fg="red"  ,bg="yellow"  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
trackImg.place(x=700, y=600)
quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="red"  ,bg="yellow"  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=1000, y=600)
 
window.mainloop()