from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os 
import csv
from tkinter import filedialog








class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root,text="Info Desk",font=("times new roman",35,"bold"),bg="black",fg="#fff")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # img_top = Image.open(r"D:\AttendenceSystem\imagesHere\kuAdmin.jpg")
        # img_top = img_top.resize((1530,325),Image.ANTIALIAS)
        # self.photoimg_top = ImageTk.PhotoImage(img_top)

        # f_lbl = Label(self.root,image=self.photoimg_top)
        # f_lbl.place(x=0,y=50,width=1536,height=825)

        
        #  information text
        text_infoH = Label(self.root,text="Follow these steps:",font=("time new roman",20,"bold"),fg="blue")
        text_infoH.place(x=5,y=50)
        text_infoH = Label(self.root,text="1. First register the student/staff on system through 'student details'. ",font=("time new roman",17,"bold"),borderwidth=0,fg="blue")
        text_infoH.place(x=10,y=100)
        text_infoH = Label(self.root,text="2. After registration process take photo sample.",font=("time new roman",17,"bold"),fg="blue")
        text_infoH.place(x=10,y=140)
        text_infoH = Label(self.root,text="3. Then we need to train the data set, for that visit 'Train Face'. ",font=("time new roman",17,"bold"),fg="blue")
        text_infoH.place(x=10,y=180)
        text_infoH = Label(self.root,text="4. Finally use face detector.",font=("time new roman",17,"bold"),fg="blue")
        text_infoH.place(x=10,y=180)

        # email
        text_infoH = Label(self.root,text="Email:",font=("time new roman",13,"bold"),fg="black")
        text_infoH.place(x=0,y=720)
        text_infoH = Label(self.root,text="susilrajneupane@gmail.com",font=("time new roman",10,"bold"),fg="black")
        text_infoH.place(x=5,y=740)
        text_infoH = Label(self.root,text="rabinbhandari7@gmail.com",font=("time new roman",10,"bold"),fg="black")
        text_infoH.place(x=5,y=760)



    
if __name__=="__main__":
    root=Tk()
    obj = Help(root)
    root.mainloop()






