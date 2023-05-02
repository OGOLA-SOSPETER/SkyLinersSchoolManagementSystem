import sys
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pyodbc
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter.ttk import Combobox
from tkinter import messagebox
import random

class AdminDashboardPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Administrator")
        self.master = tk.Tk()
        self.studentmaster = tk.Tk()


    def AdminLogin(self):
        self.root.geometry("600x300+200+100")
        self.root.config(padx=150,pady=20)



        label1 = tk.Label(self.root, text="Welcome to the Administrator dashboard.")
        label1.grid(row=0, column=0, columnspan=2)

        label2 = tk.Label(self.root, text="Kindly LOGIN.")
        label2.grid(row=1, column=0, columnspan=2)

        # UserName Entry.
        UsernameLabel = tk.Label(self.root, text="UserName")
        UsernameLabel.grid(row=2, column=0)
        self.UsernameEntry = tk.Entry(self.root, width=30)
        self.UsernameEntry.grid(row=2, column=1)

        # Password Entry.
        PasswordLabel = tk.Label(self.root, text="Password")
        PasswordLabel.grid(row=3, column=0)
        self.PasswordEntry = tk.Entry(self.root, width=30, show="*")
        self.PasswordEntry.grid(row=3, column=1)

        # Login Button
        LoginButton = tk.Button(self.root, text="Login", bg="blue", fg="white", command=self.ValidateUser)
        LoginButton.grid(row=4, column=0, columnspan=2, pady=10)

        RegisterLabel = tk.Label(self.root, text="If Not Registered, kindly proceed to register here.")
        RegisterLabel.grid(row=5, column=0, columnspan=2)

        RegisterButton = tk.Button(self.root, text="Register", bg="black", fg="white", command=self.NewAdmin)
        RegisterButton.grid(row=6, column=0, columnspan=2, pady=10)

        self.root.mainloop()
    def ValidateUser(self):
        self.username = self.UsernameEntry.get()
        password = self.PasswordEntry.get()

        if self.username != "" and password != "":
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\SchoolUsers.accdb;')
            cursor = conn.cursor()

            # Fetching the password for the given username
            cursor.execute('select Password from Admins WHERE Username = ?', self.username)
            fetched_password = cursor.fetchone()

            if fetched_password:
                if fetched_password[0] == password:
                    messagebox.showinfo("Login Success", "Login Successful")
                    self.root.withdraw()
                    self.AdminDashboard()

                else:
                    messagebox.showerror("Login Error", "Invalid Password")
            else:
                messagebox.showerror("Login Error", "Username Not Found")

        else:
            messagebox.showerror("Login Error", "Username and Password Required")
        return self.username
    def AdminDashboard(self):
        self.master.geometry("600x400+200+100")
        self.master.config(padx=50,pady=50)

        self.master.title("Administrator Dashboard")

        # Welcome Label
        WelcomeLabel = tk.Label(self.master, text="Welcome, Administrator, " + self.username)
        WelcomeLabel.grid(row=0, column=0, columnspan=4)

        # View Students Button
        ViewStudentsButton = tk.Button(self.master, text="View Students", bg="blue",width = 20, fg="white", command=self.ViewStudents)
        ViewStudentsButton.grid(row=1, column=0, padx=10,pady=10)

        # Add Student Button
        RegisterStudentButton = tk.Button(self.master, text="Add Student", bg="green",width = 20, fg="white", command=self.RegisterStudent)
        RegisterStudentButton.grid(row=1, column=1, padx=10, pady=10)

        # View Teachers Button
        ViewTeachersButton = tk.Button(self.master, text="View Teachers", bg="blue",width = 20, fg="white", command=self.ViewTeachers)
        ViewTeachersButton.grid(row=1, column=2, padx=10, pady=10)

        # Add Teacher Button
        AddTeacherButton = tk.Button(self.master, text="Add Teacher", bg="green",width = 20, fg="white", command=self.AddTeacher)
        AddTeacherButton.grid(row=2, column=0,  padx=10,pady=10)

        # View Classes Button
        ViewReportsButton = tk.Button(self.master, text="View Reports", bg="blue",width = 20, fg="white", command=self.ViewClasses)
        ViewReportsButton.grid(row=2, column=1, padx=10, pady=10)

        # Add Class Button
        ViewParentsButton = tk.Button(self.master, text="Parents Information", bg="green",width = 20, fg="white", command=self.AddClass)
        ViewParentsButton.grid(row=2, column=2, padx=10, pady=10)


        #Send Mail
        SendMailButton = tk.Button(self.master, text="Send Mail", bg="green", fg="white", command=self.SendMail)
        SendMailButton.grid(row=3, column=1, pady=10)

        # Send Mail
        HomeButton = tk.Button(self.master, text="Exit",width = 20, command=self.Home)
        HomeButton.grid(row=3, column=2, pady=10)


    def Home(self):
        self.master.withdraw()
        self.root.deiconify()
    def SendMail(self):
        messagebox.askquestion("Valid","Want to send report?")
        # Get the registration number from the entry field
        reg = self.Reg_Entry.get()

        # Connect to the database and retrieve the student's record and exam results
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\StudentData.accdb;')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM StudentData WHERE REG_NO = '{reg}'")
        record = cursor.fetchall()

        conn1 = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\ExamRecords.accdb;')
        cursor = conn1.cursor()
        cursor.execute(f"SELECT MATHS FROM ExamRecords WHERE REG_NO = '{reg}'")
        data = cursor.fetchone()

        # Set up the email sender and recipient
        sender = 'ogolasospeter62@gmail.com'
        recipient = 'captainsos483@gmail.com'
        subject = "EXAM REPORT FOR ", reg,  "Registration Number: ", reg, "\n Mathematics: 67 "
        body = 'Kindly Receive the exam Report.'

        # Set up the email message
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Send the email using Gmail's SMTP server
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'ogolasospeter62@gmail.com'
        smtp_password = 'uovfyacgvntlemes'
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender, recipient, message.as_string())

        # Show a success message
        messagebox.showinfo('Success', 'Email sent successfully')

    # except Exception as e:
    #     # Show an error message
    #     messagebox.showerror('Error', str(e))

    def ViewStudents(self):
        # This method will show all the registered students in a new window
        pass

    def RegisterStudent(self):
        self.master.withdraw()
        self.studentmaster.deiconify()
        self.studentmaster.title("SkyLiners High School New Student Registration.")
        self.studentmaster.geometry("900x600+200+100")
        self.studentmaster.config(padx=50,pady=5)
        self.studentmaster.resizable(True,True)

        lbl = Label(self.studentmaster, text="Input all student Details and the Parent Details.")
        lbl.grid(row=0, column=0)
        Reg_label = tk.Label(self.studentmaster, text="Student Details.")
        Reg_label.grid(row=1, column=0)
        stdframe = Frame(self.studentmaster,borderwidth=2,relief= GROOVE, width=500,height=350,padx=50,pady=10)
        stdframe.grid(row=2,column=0,sticky=W+E)

        # Registration Number Entry and Label
        Reg_label = tk.Label(stdframe, text="Reg_Number")
        Reg_label.grid(row=1, column=0)
        self.Reg_Entry = tk.Entry(stdframe, width=10)
        self.Reg_Entry.grid(row=1, column=1)

        # Name Entry and Label
        Name_label = tk.Label(stdframe, text="Name")
        Name_label.grid(row=2, column=0)
        self.Name_Entry = tk.Entry(stdframe, width=10)
        self.Name_Entry.grid(row=2, column=1)

        # Fees Entry and Label
        Fee_Due_label = tk.Label(stdframe, text="Fees Due")
        Fee_Due_label.grid(row=3, column=0)
        self.Fee_Due_Entry = tk.Entry(stdframe, width=10)
        self.Fee_Due_Entry.grid(row=3, column=1)

        # Fees Entry and Label
        Fee_Paid_label = tk.Label(stdframe, text="Fees Paid")
        Fee_Paid_label.grid(row=4, column=0)
        self.Fee_Paid_Entry = tk.Entry(stdframe, width=10)
        self.Fee_Paid_Entry.grid(row=4, column=1)

        # fb = IntVar(self.Fee_Due_Entry.get()) - IntVar(self.Fee_Paid_Entry.get())
        # fb_strvar = tk.StringVar(value=str(fb))
        # Fee Balance Entry and Label
        Fee_Balance_label = tk.Label(stdframe, text="Fee Balance", state="disabled")
        Fee_Balance_label.grid(row=1, column=3,pady = 2)
        self.Fee_Balance_Entry = tk.Entry(stdframe, width=10, state="disabled")
        self.Fee_Balance_Entry.grid(row=1, column=4)

        # Stream Entry and Label
        Stream_label = tk.Label(stdframe, text="Stream")
        Stream_label.grid(row=2, column=3,padx=10,pady = 2)
        self.Stream_Entry = Combobox(stdframe, width=8, values=['North', ' South', ' East', 'West'])
        self.Stream_Entry.grid(row=2, column=4)

        # Form Entry and Label
        Form_label = tk.Label(stdframe, text="Form")
        Form_label.grid(row=3, column=3,padx=10,pady = 2)
        self.Form_Entry = Combobox(stdframe, width=8, values=['1', ' 2', ' 3', ' 4'])
        self.Form_Entry.grid(row=3, column=4)

        #County Label
        stdCounty_label = tk.Label(stdframe, text="County")
        stdCounty_label.grid(row=4, column=3,padx=10,pady = 2)
        self.stdCountyEntry = Combobox(stdframe, width=8,values=['HomaBay', 'Mombasa', 'Malindi', 'Kisumu','Kisii','Nyamira','Migori','Kitale','Nairobi','Turkana','Eldoret','Lamu','Kilifi'])
        self.stdCountyEntry.grid(row=4, column=4)
        self.stdCountyEntry.set("Select County")


        prntlbl = Label(self.studentmaster,text="Parents' Details.")
        prntlbl.grid(row=3,column=0)

        parntframe = Frame(self.studentmaster,borderwidth=2,relief= GROOVE, width=500,height=350,padx=50,pady=10)
        parntframe.grid(row=4, column=0)

        #Father's Details.
        # ID Number Entry and Label
        fthLabel = Label(parntframe,text="Father's Details",font="Montserrat 12 ", justify=CENTER)
        fthLabel.grid(row=0,column=0)
        Fatherid_label = tk.Label(parntframe, text="ID. NO.")
        Fatherid_label.grid(row=1, column=0)
        self.Father_id_Entry = tk.Entry(parntframe, width=20)
        self.Father_id_Entry.grid(row=1, column=1)

        # Name Entry and Label
        FatherName_label = tk.Label(parntframe, text="Name: ")
        FatherName_label.grid(row=2, column=0)
        self.FatherName_Entry = tk.Entry(parntframe, width=20)
        self.FatherName_Entry.grid(row=2, column=1)

        # Stream Entry and Label
        FatherContact_label = tk.Label(parntframe, text="Contact: ")
        FatherContact_label.grid(row=3, column=0)
        self.FatherContact_Entry = tk.Entry(parntframe, width=20)
        self.FatherContact_Entry.grid(row=3, column=1)

        # Form Entry and Label
        FatherEmail_label = tk.Label(parntframe, text="Email: ")
        FatherEmail_label.grid(row=4, column=0)
        self.FatherEmail_Entry = tk.Entry(parntframe, width=20)
        self.FatherEmail_Entry.grid(row=4, column=1)

        #Mother's Details.
        # ID Number Entry and Label
        mthLabel = Label(parntframe, text="Mother's Details", font="Montserrat 12 ", justify=CENTER)
        mthLabel.grid(row=5, column=0)
        mother_id_label = tk.Label(parntframe, text="ID. NO.")
        mother_id_label.grid(row=6, column=0)
        self.Mother_id_Entry = tk.Entry(parntframe, width=20)
        self.Mother_id_Entry.grid(row=6, column=1)

        # Name Entry and Label
        MotherName_label = tk.Label(parntframe, text="Name: ")
        MotherName_label.grid(row=7, column=0)
        self.MotherName_Entry = tk.Entry(parntframe, width=20)
        self.MotherName_Entry.grid(row=7, column=1)

        # Stream Entry and Label
        MotherContact_label = tk.Label(parntframe, text="Contact: ")
        MotherContact_label.grid(row=8, column=0)
        self.MotherContact_Entry = tk.Entry(parntframe, width=20)
        self.MotherContact_Entry.grid(row=8, column=1)

        # Form Entry and Label
        MotherEmail_label = tk.Label(parntframe, text="Email: ")
        MotherEmail_label.grid(row=9, column=0)
        self.MotherEmail_Entry = tk.Entry(parntframe, width=20)
        self.MotherEmail_Entry.grid(row=9, column=1)

        RegisterButton = Button(self.studentmaster, text="Register Student", command=self.InsertStudent,width=20)
        RegisterButton.grid(row=5, column=0)

        ExitButton = Button(self.studentmaster, text="Exit", command=self.ExitAdmin,width=20)
        ExitButton.grid(row=5, column=1,padx=20)

        self.studentmaster.mainloop()

    def InsertStudent(self):
        reg = self.Reg_Entry.get()
        name = self.Name_Entry.get()
        feeD = self.Fee_Due_Entry.get()
        feeP = self.Fee_Paid_Entry.get()
        fd = self.Fee_Due_Entry.get()
        fp = self.Fee_Paid_Entry.get()
        stream = StringVar(self.Stream_Entry)
        form = StringVar(self.Form_Entry)
        fathId = self.Father_id_Entry.get()
        fathNm = self.FatherName_Entry.get()
        fathCnt = self.FatherContact_Entry.get()
        fathEm = self.FatherEmail_Entry.get()
        mothId = self.Mother_id_Entry.get()
        mothNm = self.MotherName_Entry.get()
        mothCnt = self.MotherContact_Entry.get()
        mothEm = self.MotherEmail_Entry.get()
        county = StringVar(self.stdCountyEntry)
        feeB = 0

        # Establish a connection to the StudentData Access database
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\StudentData.accdb;')
        # Create a cursor object
        cursor = conn.cursor()

        cursor.execute("SELECT REG_NO FROM StudentData")
        fetched_reg = [row[0] for row in cursor.fetchall()]
        #
        # # Establish a connection to the StudentData Access database
        # conn = pyodbc.connect(
        #     r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\StreamData.accdb;')
        # # Create a cursor object
        # cursor = conn.cursor()

        # cursor.execute("SELECT Stream FROM StreamData")
        # fetched_stream = cursor.fetchall()
        # random_stream = random.choice(fetched_stream)
        # stream = random_stream

        # Check if the registration number already exists
        if reg not in fetched_reg:
            if reg != "" and name != "" and stream != "" and form != "" and feeD != "" and feeP != "" and fathId != "" and fathNm != "" and fathEm != "" and fathCnt != "" and mothId != "" and mothNm != "" and mothCnt != "" and mothEm != "":
                # Insert the new record
                cursor.execute(
                    f"INSERT INTO StudentData (REG_NO,  NAME, STREAM, FORM, FEES_DUE, FEES_PAID, FEES_BALANCE, FATHER_ID, FATHER_NAME, FATHER_CONTACT, FATHER_EMAIL, MOTHER_ID, MOTHER_NAME, MOTHER_CONTACT, MOTHER_EMAIL, COUNTY )  VALUES ('{reg}', '{name}', '{stream}', '{form}', '{feeD}', '{feeP}', '{feeB}', '{fathId}', '{fathNm}', '{fathCnt}', '{fathEm}', '{mothId}', '{mothNm}', '{mothCnt}', '{mothEm}', '{county}')")
                # Commit the changes
                conn.commit()
                conn.close()
                messagebox.showinfo("Success.", "Record Added Successfully!")
                self.master.deiconify()
            else:
                messagebox.showerror("Empty Fields","Kindly Fill All the Fields!!!")
        else:
            if reg == "" and name == "":
                messagebox.showerror("Empty Entry", "Empty Entries!\n Kindly Fill All Fields.")
            else:
                messagebox.showerror("Duplicate Records!", "Registration Number " + reg + " already exists!!")

    def ViewTeachers(self):
        # This method will show all the registered teachers in a new window
        pass

    def AddTeacher(self):
        # This method will open a form for adding a new teacher
        self.masterTeacher = tk.Tk()
        self.master.withdraw()
        self.masterTeacher.deiconify()
        self.masterTeacher.title("SkyLiners High School New Teachers Registration.")
        self.masterTeacher.geometry("650x450+200+100")
        self.masterTeacher.config(padx=60, pady=50)


        lbl = Label(self.masterTeacher, text ="Proceed to register.\nEnsure you fill out all the fields.!!")
        lbl.grid(row = 0,column=1)
        # Registration Number Entry and Label
        TIdReg_label = Label(self.masterTeacher, text="Employment ID:")
        TIdReg_label.grid(row=1, column=0)
        self.TIdReg_Entry = tk.Entry(self.masterTeacher, width=20)
        self.TIdReg_Entry.grid(row=2, column=0)

        # Age Entry and Label
        TAge_label = Label(self.masterTeacher, text="Teacher's Name")
        TAge_label.grid(row=1, column=1)
        self.TAge_Entry = tk.Spinbox(self.masterTeacher, from_= 12, to= 19, width=20)
        self.TAge_Entry.grid(row=2, column=1)

        # Name Entry and Label
        TName_label = Label(self.masterTeacher, text="Teacher's Name")
        TName_label.grid(row=1, column=2)
        self.TName_Entry = tk.Entry(self.masterTeacher, width=20)
        self.TName_Entry.grid(row=2, column=2)

        # Stream Entry and Label
        TStream_label = tk.Label(self.masterTeacher, text="Stream Handled:")
        TStream_label.grid(row=3, column=0)
        self.TStream_Entry = Combobox(self.masterTeacher, width=20, values=['North', 'South', 'East', 'West'])
        self.TStream_Entry.grid(row=4, column=0)

        # Form_Taught Entry and Label
        TForm_label = tk.Label(self.masterTeacher, text="Form Handled:")
        TForm_label.grid(row=3, column=1)
        self.TForm_Entry = Combobox(self.masterTeacher, width=20, values=['1', ' 2', ' 3', ' 4'])
        self.TForm_Entry.grid(row=4, column=1)

        # Subjects Entry and Label
        Tsubj1_label = Label(self.masterTeacher, text="Subject1:")
        Tsubj1_label.grid(row=3, column=2)
        self.Tsubj1_Entry = Entry(self.masterTeacher, width=20)
        self.Tsubj1_Entry.grid(row=4, column=2)

        # Subjects Entry and Label
        Tsubj2_label = Label(self.masterTeacher, text="Subject2:")
        Tsubj2_label.grid(row=5, column=0)
        self.Tsubj2_Entry = Entry(self.masterTeacher, width=20)
        self.Tsubj2_Entry.grid(row=6, column=0)

        # Subjects Entry and Label
        Tsubj3_label = Label(self.masterTeacher, text="Subject3:")
        Tsubj3_label.grid(row=5, column=1)
        self.Tsubj3_Entry = Entry(self.masterTeacher, width=20)
        self.Tsubj3_Entry.grid(row=6, column=1)

        trCounty_label = tk.Label(self.masterTeacher, text="County Code")
        trCounty_label.grid(row=5, column=2)
        self.trCountyEntry = Combobox(self.masterTeacher, width=20, values=[f"{i}" for i in range(1, 48, 1)])
        self.trCountyEntry.grid(row=6, column=2)
        self.trCountyEntry.set("Select County")

        RegisterButton = Button(self.masterTeacher, text="Register", bg="Blue",fg="White",  width = 20, command= self.RegisterTeacher)
        RegisterButton.grid(row=8, column=0,  pady=10)

        ExitButton = Button(self.masterTeacher, text="Exit", bg="Blue",fg="White", width = 20, command=self.ExitTeacher)
        ExitButton.grid(row=8, column=1,  pady=10)

        for Widget in self.masterTeacher.winfo_children():
            Widget.grid_configure(padx=10,pady=5)
        self.masterTeacher.mainloop()
    def RegisterTeacher(self):
        tId = self.TIdReg_Entry.get()
        tName = self.TName_Entry.get()
        tage = self.TAge_Entry.get()
        tstream = self.TStream_Entry.get()
        tform = self.TForm_Entry.get()
        tsubject1 = self.Tsubj1_Entry.get()
        tsubject2 = self.Tsubj2_Entry.get()
        tsubject3 = self.Tsubj3_Entry.get()
        tcounty = self.trCountyEntry.get()

        connection = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\TeachersData.accdb;')
        dataAccess = connection.cursor()

        dataAccess.execute("SELECT EMP_NO from TeachersData")
        fetched_Ids = dataAccess.fetchall()

        if tId not in fetched_Ids:
            if tId != "" and tName != "" and tsubject1 != "" and tsubject2 and tsubject3 != "" != "":
                # Insert the new record
                dataAccess.execute(f"INSERT INTO TeachersData (EMP_NO,  NAME, AGE, COUNTY, STREAM_T, FORM_T, SUBJECT1_T, SUBJECT2_T, SUBJECT3_T)  VALUES ('{tId}', '{tName}', {tage}, {tcounty}, '{tstream}', {tform}, '{tsubject1}', '{tsubject2}', '{tsubject3}')")
                # Commit the changes
                dataAccess.commit()
                # dataAccess.close()
                # connection.close()
                messagebox.showinfo("Success.", "Teacher Registered  Successfully!")
                self.master.deiconify()
            else:
                messagebox.showerror("Empty Fields", "Kindly Fill All the Fields!!!")
        else:
            if tId == "" and tName == "":
                messagebox.showerror("Empty Entry", "Empty Entries!\n Kindly Fill All Fields.")
            else:
                messagebox.showerror("Duplicate Records!", "Employee Number " + tId + " already exists!!")

    def ExitTeacher(self):
        self.masterTeacher.withdraw()
        self.master.deiconify()
    def ViewClasses(self):
        # This method will show all the classes in a new window
        pass

    def AddClass(self):
        # This method will open a form for adding a new class
        pass

    def ExitAdmin(self):
        self.studentmaster.withdraw()
        self.master.deiconify()

    def NewAdmin(self):
        self.adminmaster = tk.Tk()
        self.adminmaster.geometry("550x300+200+150")
        self.adminmaster.config(padx = 10,pady = 10)
        self.adminmaster.title("Administrator Registration.")

        mainFrame = tk.Frame(self.adminmaster)
        mainFrame.pack()

        mainLabel = Label(mainFrame,text = "New Administrator Registration.")
        mainLabel.grid(row = 0, column=0)

        usernamelabel = Label(mainFrame,text="UserName")
        usernamelabel.grid(row=1,column=0)
        passwordlabel = Label(mainFrame,text="Password.")
        passwordlabel.grid(row = 1,column=1)

        self.usernameentry = Entry(mainFrame,width=20)
        self.usernameentry.grid(row = 2,column=0)

        self.passwordentry = Entry(mainFrame,width=20)
        self.passwordentry.grid(row = 2, column=1)

        registerButton = Button(mainFrame,text="Register Admin", width=20, command=self.RegisterAdmin)
        registerButton.grid(row = 5,column=0,padx=35,pady=20)

    def RegisterAdmin(self):
        passw = self.passwordentry.get()
        user = self.usernameentry.get()

        if user != "" and passw != "":
            conn = pyodbc.connect(
                r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\SchoolUsers.accdb;')
            cursor = conn.cursor()

            # Fetching the password for the given username
            cursor.execute(f"SELECT Password FROM Admins WHERE Username = '{user}'")
            fetched_password = cursor.fetchone()

            if fetched_password:
                messagebox.showerror("Invalid User", "Username already exists. Please choose a different one.")
                self.LogClear()
                self.adminmaster.deiconify()
            else:
                cursor.execute(f"SELECT Username FROM Admins WHERE Password = '{passw}'")
                fetched_username = cursor.fetchone()

                if fetched_username:
                    messagebox.showerror("Password Error! ", "Password already used. Please choose a different one.")
                    self.LogClear()
                    self.adminmaster.deiconify()

                else:
                    cursor.execute(f"INSERT INTO Admins (Username, Password) VALUES ('{user}', '{passw}')")
                    cursor.commit()
                    cursor.close()
                    messagebox.showinfo("Registration Success", "New Admin Successfully Registered!")
                    self.LogClear()
                    self.adminmaster.withdraw()
                    self.root.deiconify()

        else:
            messagebox.showerror("Empty Fields Error", "Please enter both a username and a password.")
            self.adminmaster.deiconify()
            self.LogClear()

    def LogClear(self):
        self.passwordentry.delete(0,'end')
        self.usernameentry.delete(0,'end')
        self.UsernameEntry.focus()

    # def RegisterAdmin(self):
    #     passw = self.passwordentry.get()
    #     user = self.usernameentry.get()
    #
    #     if user != "" and passw != "":
    #         conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\SchoolUsers.accdb;')
    #         cursor = conn.cursor()
    #
    #         # Fetching the password for the given username
    #         cursor.execute('select   Username from Admins')
    #         fetched_users = cursor.fetchall()
    #
    #         cursor.execute('select Password from Admins')
    #         fetched_passwords = cursor.fetchall()
    #
    #         if user not in fetched_users:
    #             if passw not in fetched_passwords:
    #                 cursor.execute(f"INSERT INTO Admins (Username, Password) VALUES ('{user}', '{passw}')")
    #                 cursor.commit()
    #                 cursor.close()
    #                 messagebox.showinfo("Registration Success", "New Admin Successfully Registered!")
    #                 self.adminmaster.withdraw()
    #                 self.root.deiconify()
    #
    #             else:
    #                 messagebox.showerror("Password Error! ", "Password already used😂🤣🤣")
    #         else:
    #             messagebox.showerror("Invalid User", "Username Already Exists.")
    #
    #     else:
    #         messagebox.showerror("Empty Fields Error", "Input Field Values!.")
    #

        #


admin = AdminDashboardPage()
admin.AdminLogin()
# admin.AdminDashboard()

#
# def RegisterStudent(self):
#     self.subroot = tk.Tk()
#     self.subroot.deiconify()
#     self.subroot.geometry("1000x600+200+100")
#     self.subroot.title("Student Registration.")
#
#     mainFrame = tk.Frame(self.subroot)
#     mainFrame.pack()
#
#     stdLabel = tk.LabelFrame(mainFrame, text="Student Details.")
#     stdLabel.grid(row=1, column=0, padx=50, pady=100, columnspan=7)
#     stdLabel.winfo_geometry()
#
#     Label(stdLabel, text="Reg. No.").grid(row=1, column=0)
#     Label(stdLabel, text="Name.").grid(row=2, column=0)
#     Label(stdLabel, text="Age.").grid(row=3, column=0)
#     Label(stdLabel, text="Stream.").grid(row=1, column=3)
#     Label(stdLabel, text="Form.").grid(row=2, column=3)
#     Label(stdLabel, text="County.").grid(row=3, column=3)
#
#     stdRegEntry = Entry(stdLabel, width=25)
#     stdRegEntry.grid(row=1, column=1)
#     StdReg = StringVar(stdRegEntry)
#
#     stdNameEntry = Entry(stdLabel, width=25)
#     stdNameEntry.grid(row=2, column=1)
#     StdName = StringVar(stdNameEntry)
#
#     stdAgeEntry = Entry(stdLabel, width=25)
#     stdAgeEntry.grid(row=3, column=1)
#     StdAge = IntVar(stdAgeEntry)
#
#     stdStreamEntry = Entry(stdLabel, width=25)
#     stdStreamEntry.grid(row=1, column=4)
#     StdStream = IntVar(stdStreamEntry)

    # stdFormEntry = Entry(stdLabel, width=25)
    # stdFormEntry.grid(row=2, column=4)
    # StdForm = IntVar(stdFormEntry)
    #
    #



    # self.subroot.mainloop()

