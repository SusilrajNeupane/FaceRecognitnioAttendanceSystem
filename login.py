from tkinter import *
from tkinter import ttk

from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime


# drtddg

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







def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()




class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0") 


        self.bg = ImageTk.PhotoImage(file="imagesHere/logBg.jpg")
        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        frame = Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)


        img1 = Image.open("imagesHere/ThisIcon2.jpg")
        img1 = img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str = Label(frame,text="Log In Here",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        # label
        username_lbl = Label(frame,text="Username",font=("times new roman",14,"bold"),fg="white",bg="black")
        username_lbl.place(x=40,y=155)

        self.txtuser = ttk.Entry(frame,font=("times new roman",14,"bold"))
        self.txtuser.place(x=40,y=180,width=270)


        password_lbl = Label(frame,text="Password",font=("times new roman",14,"bold"),fg="white",bg="black")
        password_lbl.place(x=40,y=225)

        self.txtpass = ttk.Entry(frame,font=("times new roman",14,"bold"))
        self.txtpass.place(x=40,y=250,width=270)





        # login button

        loginbtn = Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)



    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields Required")
        elif self.txtuser.get()=="susil" and self.txtpass.get()=="12345":
            messagebox.showinfo("Success","Welcome To Pannel :)")
        else:
            conn = mysql.connector.connect(host='localhost',username='root',password='Mysql@123database',database='attendencesystem')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and passwrod=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid username or passwrod")
            else:
                open_main = messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()






class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0") 


        # ===variables========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        # ============== bg image ===========
        self.bg = ImageTk.PhotoImage(file="imagesHere/logBg.jpg")
        bg_lbl = Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # ============= left image ============
        self.bg1 = ImageTk.PhotoImage(file="imagesHere/logBg.jpg")
        left_lbl = Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)


        frame = Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl = Label(frame,text="Register Here",font=("time new roman",20,"bold"),bg="white",fg="green")
        register_lbl.place(x=20,y=20)

        # =========labels and entry  ==============

        #   row 1
        fname = Label(frame,text="First Name",font=("time new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("time new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name = Label(frame,text="Last Name",font=("time new roman",15,"bold"),bg="white")
        l_name.place(x=370,y=100)

        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname,font=("time new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #   row 2
        contact = Label(frame,text="Contact No.",font=("time new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact,font=("time new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email = Label(frame,text="Email",font=("time new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email,font=("time new roman",15))
        self.txt_email.place(x=370,y=200,width=250)


        # row 3
        security_Q = Label(frame,text="Select Security Question",font=("time new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ,font=("time new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"] = ("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)



        security_A = Label(frame,text="Security Answer",font=("time new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        # row 4
        pswd = Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)


        confirm_pswd = Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        # check button
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I agree the terms and conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        # buttons
        img = Image.open('imagesHere/ThisIcon2.jpg')
        img= img.resize((200,50),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)


        img1 = Image.open('imagesHere/ThisIcon2.jpg')
        img1= img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img)
        b1 = Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b1.place(x=500,y=420,width=200)



    # ===========function declaration =============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields required.")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error","Password and confirm password must be same.")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","You should agree to terms to continue.")
        else:
            conn = mysql.connector.connect(host='localhost',username='root',password='Mysql@123database',database='attendencesystem')
            my_cursor = conn.cursor()
            query = (" select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","User already exists, please try another email.")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")






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

 
        # photos face buttom 
        # img9 = Image.open(r"D:\AttendenceSystem\imagesHere\photos.jpg")
        # img9 = img9.resize((220,220),Image.ANTIALIAS)
        # self.photoimg9 = ImageTk.PhotoImage(img9)

        # b1 = Button(bg_img,image=self.photoimg9,cursor='hand2',command=self.open_img)
        # b1.place(x=500,y=400,width=220,height=220)

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
    main()




