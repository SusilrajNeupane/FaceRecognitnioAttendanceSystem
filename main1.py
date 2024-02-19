from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import tkinter

from student import Student
from train import Train
from face_recognition import Face_recognition
from attendence import Attendence
from help import Help


from time import strftime
from datetime import datetime



class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        # bg image
        img3 = Image.open(r"D:\AttendenceSystem\imagesHere\kuLibGround.jpg")
        img3 = img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=860)


        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=20,width=1530,height=44)


        # ==========   TIME ===============
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=5,y=(-5) ,width=110,height=50)
        time()






        # student button
        img4 = Image.open(r"D:\AttendenceSystem\imagesHere\student.jpg")
        img4 = img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details,cursor='hand2')
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text='Student Details' ,command=self.student_details,cursor='hand2',font=("times new roman",15,"bold"),bg='black',fg='white')
        b1_1.place(x=200,y=300,width=220,height=40)



        # detect face 
        img5 = Image.open(r"D:\AttendenceSystem\imagesHere\detect.jpg")
        img5 = img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,command=self.face_data,cursor='hand2')
        b1.place(x=500,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text='Face Detector',command=self.face_data ,cursor='hand2',font=("times new roman",15,"bold"),bg='black',fg='white')
        b1_1.place(x=500,y=300,width=220,height=40)




        # attendence face 
        img6 = Image.open(r"D:\AttendenceSystem\imagesHere\attendence.jpg")
        img6 = img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image=self.photoimg6,cursor='hand2',command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text='Attendance' ,cursor='hand2',command=self.attendance_data,font=("times new roman",15,"bold"),bg='black',fg='white')
        b1_1.place(x=800,y=300,width=220,height=40)




        # train face buttom 
        img8 = Image.open(r"D:\AttendenceSystem\imagesHere\trainface.jpg")
        img8 = img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image=self.photoimg8,command=self.train_data,cursor='hand2')
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text='Train face' ,cursor='hand2',command=self.train_data,font=("times new roman",15,"bold"),bg='black',fg='white')
        b1_1.place(x=1100,y=300,width=220,height=40)

 


        b1_1 = Button(bg_img,text='Photos' ,cursor='hand2',command=self.open_img,font=("times new roman",15,"bold"),bg='black',fg='white')
        b1_1.place(x=1300,y=620,width=220,height=40)




        b1_1 = Button(bg_img,text='Exit' ,cursor='hand2',command=self.iExit,font=("times new roman",15,"bold"),bg='red',fg='white')
        b1_1.place(x=1300,y=720,width=220,height=40)




        #  information text
        text_infoH = Label(bg_img,text="End Semester Project ",font=("time new roman",10,"bold"),borderwidth=0,fg="blue")
        text_infoH.place(x=-5,y=680)
        text_infoH = Label(bg_img,text="By:",font=("time new roman",10,"bold"),borderwidth=0,fg="blue")
        text_infoH.place(x=-5,y=700)
        text_infoH = Label(bg_img,text="Rabin Bhandari &",font=("time new roman",10,"bold"),borderwidth=0,fg="blue")
        text_infoH.place(x=-5,y=720)
        text_infoH = Label(bg_img,text="Susil Raj Neupane",font=("time new roman",10,"bold"),borderwidth=0,fg="blue")
        text_infoH.place(x=-5,y=740)



    

    def open_img(self):
        os.startfile("data")


    

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return 


    # ====================function buttons============

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)





    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)


    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)



    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendence(self.new_window)



    def info_data(self):
        self.new_window = Help(self.root)
        self.app = Attendence(self.new_window)













if __name__=="__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()