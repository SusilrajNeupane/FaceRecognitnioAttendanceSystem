from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os 
import csv
from tkinter import filedialog








class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="black",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"D:\AttendenceSystem\imagesHere\kuAdmin.jpg")
        img_top = img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1536,height=825)


        #  frame
        main_frame = Frame(f_lbl, bd=2,bg="yellow")
        main_frame.place(x=10,y=55,width=1500,height=600)









    
if __name__=="__main__":
    root=Tk()
    obj = Developer(root)
    root.mainloop()












