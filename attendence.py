from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os 
import csv
from tkinter import filedialog






myData = []

class Attendence:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #  ================ VARIABLES ============
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendence = StringVar()




        # bg image
        img3 = Image.open(r"D:\AttendenceSystem\imagesHere\library.jpg")
        img3 = img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=55,width=1540,height=660)

        title_lbl = Label(bg_img,text="ATTENDANCE MANAGEMENT ",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        

        # mian frame

        main_frame = Frame(bg_img, bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        # left frame 
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)



        left_inside_frame = Label(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=35,width=720,height=370)

        # labels and entry
        # attendance id
        attendanceId_label = Label(left_inside_frame,text='Attendance ID',font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Name
        nameLabel = Label(left_inside_frame,text='Name',font=("times new roman",12,"bold"),bg="white")
        nameLabel.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        atten_name = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        atten_name.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # roll
        rollLabel = Label(left_inside_frame,text='Roll',font=("times new roman",12,"bold"),bg="white")
        rollLabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        atten_roll = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        atten_roll.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        # Department
        depLabel = Label(left_inside_frame,text='Department',font=("times new roman",12,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        atten_dep = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        # time
        timeLabel = Label(left_inside_frame,text='Time',font=("times new roman",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        atten_time = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # date
        dateLabel = Label(left_inside_frame,text='Date',font=("times new roman",12,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        atten_date = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        atten_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # attendance 
        attendenceLabel = Label(left_inside_frame,text='Attendance Status',font=("times new roman",12,"bold"),bg="white")
        attendenceLabel.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.atten_status= ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendence,font=("times new roman",12,"bold"))
        self.atten_status["values"] = ("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        self.atten_status.current(0)


        # button frame
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=300,width=715,height=38)

        save_btn = Button(btn_frame,text="Import csv",command=self.importCsv,width=19,font=("times new roman",12,"bold"),bg='blue',fg='white')
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="Export csv",command=self.exportCsv,width=19,font=("times new roman",12,"bold"),bg='blue',fg='white')
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text="Update",width=19,font=("times new roman",12,"bold"),bg='blue',fg='white')
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg='blue',fg='white')
        reset_btn.grid(row=0,column=3)




        # right frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=660,height=580)


        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=5,y=5,width=650,height=460)


        # ======= scroll bar table=======
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)



        self.AttendanceReportTable = ttk.Treeview(table_frame,column= ("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)




        self.AttendanceReportTable.heading("id",text="Attendence ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendence",text="Attendence")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendence",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)


        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_coursor)


    # ====================  fetch data ==================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    # ====  IMPORT CSV=====

    def importCsv(self):
        global myData
        myData.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALI File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)




    # ======= EXPORT CSV ================
    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","No Data found to export.", parent=self.root )
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALI File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+ os.path.basename(fln)+" successfully.",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        

    def get_coursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendence.set(rows[6])



    def reset_data(self):

        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")














if __name__=="__main__":
    root=Tk()
    obj = Attendence(root)
    root.mainloop()