import ViewEditStudent
import re
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
import pyodbc
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter.ttk import Combobox
from tkinter import messagebox
import random
# from ViewEditStudent import viewstud

class AdminDashboardPage:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Administrator")
        self.master = tk.Tk()

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
        self.Passwordentry = tk.Entry(self.root, width=30, show="*")
        self.Passwordentry.grid(row=3, column=1)

        # Login Button
        LoginButton = tk.Button(self.root, text="Login", bg="blue", fg="white", width=20, command=self.ValidateUser)
        LoginButton.grid(row=4, column=0, columnspan=2, pady=10)

        RegisterLabel = tk.Label(self.root, text="If Not Registered, kindly proceed to register here.")
        RegisterLabel.grid(row=5, column=0, columnspan=2)

        RegisterButton = tk.Button(self.root, text="Register", bg="blue", fg="white", width=20, command=self.NewAdmin)
        RegisterButton.grid(row=6, column=0, pady=10)

        ExitButton = tk.Button(self.root, text="Exit ", bg="blue", fg="white", width=20, command=self.Exit)
        ExitButton.grid(row=6, column=1, pady=10)

        self.root.mainloop()
    def Exit(self):
        exit()
        self.master.deiconify()
    def ValidateUser(self):
        self.username = self.UsernameEntry.get()
        password = self.Passwordentry.get()

        if self.username != "" and password != "":
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
            cursor = conn.cursor()

            # Fetching the password for the given username
            cursor.execute('select Password from Admins WHERE Username = ?', self.username)
            fetched_password = cursor.fetchone()
            # Fetching the username for the given password
            cursor.execute('select Username from Admins WHERE Password = ?', fetched_password)
            fetched_username = cursor.fetchone()

            if fetched_password and fetched_username:
                if fetched_password[0] == password and fetched_username[0] == self.username:
                    messagebox.showinfo("Login Success", "Login Successful")
                    self.LogClear()
                    self.root.withdraw()
                    self.AdminDashboard()

                elif fetched_username[0] != self.username:
                    messagebox.showerror("Login Error", "Invalid UserName")
                    self.LogClear()
                elif password != fetched_password[0]:
                    messagebox.showerror("Login Error", "Invalid Password")
                    self.LogClear()

            else:
                messagebox.showerror("Login Error", "Username Not Found")
                self.LogClear()


        else:
            messagebox.showerror("Login Error", "Username and Password Required")
            self.LogClear()

        return self.username
    def AdminDashboard(self):
        self.master.geometry("600x400+200+100")
        self.master.config(padx=50,pady=50)

        self.master.title("Administrator Dashboard")

        # Welcome Label
        WelcomeLabel = tk.Label(self.master, text="Welcome, Administrator, " + self.username)
        WelcomeLabel.grid(row=0, column=0, columnspan=4)
        self.viewst = ViewEditStudent.ViewStudentDetails()
        # View Students Button
        ViewStudentsButton = tk.Button(self.master, text="View Students", bg="blue",width = 20, fg="white", command=self.viewst.ViewStudent)
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
        ViewReportsButton = tk.Button(self.master, text="View Reports", bg="blue",width = 20, fg="white", command=self.ViewReports)
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
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM StudentData WHERE REG_NO = '{reg}'")
        record = cursor.fetchall()

        conn1 = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\ExamRecords.accdb;')
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


    def RegisterStudent(self):
        self.master.withdraw()
        self.studentmaster = tk.Tk()
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
        self.Fee_Due_Entry.bind('<KeyRelease>',lambda event: self.calculate_fee_balance())

        # Fees Entry and Label
        Fee_Paid_label = tk.Label(stdframe, text="Fees Paid")
        Fee_Paid_label.grid(row=4, column=0)
        self.Fee_Paid_Entry = tk.Entry(stdframe, width=10)
        self.Fee_Paid_Entry.grid(row=4, column=1)
        self.Fee_Paid_Entry.bind('<KeyRelease>',lambda event: self.calculate_fee_balance())


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

        RegisterButton = Button(self.studentmaster, text="Register Student", command=self.ValidateEntries,width=20)
        RegisterButton.grid(row=5, column=0)

        ExitButton = Button(self.studentmaster, text="Exit", command=self.ExitAdmin,width=20)
        ExitButton.grid(row=5, column=1,padx=20)

        self.studentmaster.mainloop()
    def ValidateEntries(self):
        self.validateContact(self.FatherContact_Entry.get())
        self.validateContact(self.MotherContact_Entry.get())
        self.valid_email(self.FatherEmail_Entry.get())
        self.valid_email(self.MotherEmail_Entry.get())
        if self.valid:
            self.InsertStudent()

    def InsertStudent(self):
        reg = self.Reg_Entry.get()
        name = self.Name_Entry.get()
        feeD = self.Fee_Due_Entry.get()
        feeP = self.Fee_Paid_Entry.get()
        stream = self.Stream_Entry.get()
        form = self.Form_Entry.get()
        fathId = self.Father_id_Entry.get()
        fathNm = self.FatherName_Entry.get()
        fathCnt = self.FatherContact_Entry.get()
        fathEm = self.FatherEmail_Entry.get()
        mothId = self.Mother_id_Entry.get()
        mothNm = self.MotherName_Entry.get()
        mothCnt = self.MotherContact_Entry.get()
        mothEm = self.MotherEmail_Entry.get()
        county = self.stdCountyEntry.get()

        # Validate the input fields
        if not all((reg, name, feeD, feeP, stream, form, fathId, fathNm, fathCnt, fathEm, mothId, mothNm, mothCnt,
                    mothEm, county)):
            messagebox.showerror("Empty Fields", "Kindly Fill All the Fields!!!")
            return


        # Establish a connection to the StudentData Access database
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
        # Create a cursor object
        cursor = conn.cursor()

        cursor.execute("SELECT REG_NO FROM StudentData")
        fetched_reg = [row[0] for row in cursor.fetchall()]

        # Check if the registration number already exists
        if reg in fetched_reg:
            messagebox.showerror("Duplicate Records!", "Registration Number " + reg + " already exists!!")
            return

        # Insert the new record
        cursor.execute(
            f"INSERT INTO StudentData (REG_NO, NAME, STREAM, FORM, FEES_DUE, FEES_PAID, FEES_BALANCE, FATHER_ID, FATHER_NAME, FATHER_CONTACT, FATHER_EMAIL, MOTHER_ID, MOTHER_NAME, MOTHER_CONTACT, MOTHER_EMAIL, COUNTY)  VALUES ('{reg}', '{name}', '{stream}', '{form}', '{feeD}', '{feeP}', '{self.fee_balance}', '{fathId}', '{fathNm}', '{fathCnt}', '{fathEm}', '{mothId}', '{mothNm}', '{mothCnt}', '{mothEm}', '{county}')")

        # Commit the changes
        conn.commit()
        conn.close()
        messagebox.showinfo("Success.", "Record Added Successfully!")
        self.master.deiconify()

    def valid_email(self, mail):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'
        valid = re.match(pattern, mail) is not None
        if not valid:
            messagebox.showerror("Invalid email!", "Input the email in the correct format!!")
            if mail == self.MotherEmail_Entry.get():
                messagebox.showerror("Mail Error","Input the Mother's Email Correctly.")
                self.MotherEmail_Entry.focus()
            elif mail == self.FatherEmail_Entry.get():
                messagebox.showerror("Mail Error","Input the Father's Email Correctly.")
                self.FatherEmail_Entry.focus()

        else:
            self.valid = messagebox.showinfo("Valid","No Errors")

    def validateContact(self, contact):
        if len(contact) != 10:
            messagebox.showerror("Invalid Contact!", "Contact must be only 10 digits long!!")
            if contact == self.FatherContact_Entry.get():
                messagebox.showerror("Contact Error","Input the Father's Contact Correctly.")
                self.FatherContact_Entry.focus()
            elif contact == self.MotherContact_Entry.get():
                messagebox.showerror("Contact Error","Input the Mother's Contact Correctly.")
                self.MotherContact_Entry.focus()
        else:
            self.valid = messagebox.showinfo("Valid","No Errors")
    # def InsertStudent(self):
    #     reg = self.Reg_Entry.get()
    #     name = self.Name_Entry.get()
    #     feeD = self.Fee_Due_Entry.get()
    #     feeP = self.Fee_Paid_Entry.get()
    #     stream = self.Stream_Entry.get()
    #     form = self.Form_Entry.get()
    #     fathId = self.Father_id_Entry.get()
    #     fathNm = self.FatherName_Entry.get()
    #     fathCnt = self.FatherContact_Entry.get()
    #     fathEm = self.FatherEmail_Entry.get()
    #     mothId = self.Mother_id_Entry.get()
    #     mothNm = self.MotherName_Entry.get()
    #     mothCnt = self.MotherContact_Entry.get()
    #     mothEm = self.MotherEmail_Entry.get()
    #     county = self.stdCountyEntry.get()
    #
    #     # Establish a connection to the StudentData Access database
    #     conn = pyodbc.connect(
    #         r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
    #     # Create a cursor object
    #     cursor = conn.cursor()
    #
    #     cursor.execute("SELECT REG_NO FROM StudentData")
    #     fetched_reg = [row[0] for row in cursor.fetchall()]
    #     #
    #     # # Establish a connection to the StudentData Access database
    #     # conn = pyodbc.connect(
    #     #     r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\StreamData.accdb;')
    #     # # Create a cursor object
    #     # cursor = conn.cursor()
    #
    #     # cursor.execute("SELECT Stream FROM StreamData")
    #     # fetched_stream = cursor.fetchall()
    #     # random_stream = random.choice(fetched_stream)
    #     # stream = random_stream
    #
    #     # Check if the registration number already exists
    #     if reg not in fetched_reg:
    #         if reg != "" and name != "" and stream != "" and form != "" and feeD != "" and feeP != "" and fathId != "" and fathNm != "" and fathEm != "" and fathCnt != "" and mothId != "" and mothNm != "" and mothCnt != "" and mothEm != "":
    #             # Insert the new record
    #             self.validateContact(self.FatherContact_Entry.get())
    #             self.validateContact(self.MotherContact_Entry.get())
    #             self.valid_email(self.MotherEmail_Entry.get())
    #             self.valid_email(self.FatherEmail_Entry.get())
    #
    #             cursor.execute(
    #                 f"INSERT INTO StudentData (REG_NO,  NAME, STREAM, FORM, FEES_DUE, FEES_PAID, FEES_BALANCE, FATHER_ID, FATHER_NAME, FATHER_CONTACT, FATHER_EMAIL, MOTHER_ID, MOTHER_NAME, MOTHER_CONTACT, MOTHER_EMAIL, COUNTY )  VALUES ('{reg}', '{name}', '{stream}', '{form}', '{feeD}', '{feeP}', '{self.fee_balance}', '{fathId}', '{fathNm}', '{fathCnt}', '{fathEm}', '{mothId}', '{mothNm}', '{mothCnt}', '{mothEm}', '{county}')")
    #             # Commit the changes
    #             conn.commit()
    #             conn.close()
    #             messagebox.showinfo("Success.", "Record Added Successfully!")
    #             self.welcomemaster.deiconify()
    #         else:
    #             messagebox.showerror("Empty Fields","Kindly Fill All the Fields!!!")
    #     else:
    #         if reg == "" and name == "":
    #             messagebox.showerror("Empty Entry", "Empty Entries!\n Kindly Fill All Fields.")
    #         else:
    #             messagebox.showerror("Duplicate Records!", "Registration Number " + reg + " already exists!!")
    # def valid_email(self,mail):
    #     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'
    #     valid = re.match(pattern,mail) is not None
    #     if not valid:
    #         messagebox.showerror("Invalid email!","Input the email in the correct format!!")
    #         self.viewmaster.deiconify()
    #         if mail == self.MotherEmail_Entry.get():
    #             self.MotherEmail_Entry.focus()
    #         elif mail == self.FatherEmail_Entry.get():
    #             self.FatherEmail_Entry.focus()
    # def validateContact(self,contact):
    #     if len(contact) != 10:
    #         messagebox.showerror("Invalid Contact!","Contact must be only 10 digits long!!")
    #         self.viewmaster.deiconify()
    #         if contact == self.FatherContact_Entry.get():
    #             self.FatherContact_Entry.focus()
    #         elif contact == self.MotherContact_Entry.get():
    #             self.MotherContact_Entry.focus()
    def calculate_fee_balance(self):
        fee_due = float(self.Fee_Due_Entry.get())
        fee_paid = float(self.Fee_Paid_Entry.get())
        self.fee_balance = fee_due - fee_paid
        self.Fee_Balance_Entry.config(state="normal")
        self.Fee_Balance_Entry.delete(0, tk.END)
        self.Fee_Balance_Entry.insert(0, str(self.fee_balance))
        self.Fee_Balance_Entry.config(state='disabled')
        # except ValueError:
        #     messagebox.showwarning("Invalid Input!","Input Values Only!!")

    def ViewTeachers(self):
        # This method will show all the registered teachers in a new window
        # This method will open a form for displaying all teachers
        global col, i
        self.masterTeacher = tk.Tk()
        self.master.withdraw()
        self.masterTeacher.deiconify()
        self.masterTeacher.title("SkyLiners High School  Teachers Data.")
        self.masterTeacher.geometry("1100x500+200+100")
        self.masterTeacher.resizable(width=True,height=True)
        self.masterTeacher.config(padx=60, pady=50)
        frm1 = Frame(self.masterTeacher)
        frm1.grid(row=0, column=0)

        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM TeachersData')
        records = cursor.fetchall()

        tree = ttk.Treeview(frm1)
        tree["columns"] = tuple(range(len(records[0])))
        tree["show"] = "headings"
        # for i, col in enumerate(records[0]):
        for i, col in enumerate(cursor.description):
            tree.heading(i,text=col[0])

        col_width = max(max(len(str(row[i])) for row in records), len(col[0])) * 5
        for i, col in enumerate(records[0]):
            tree.column(i,width=col_width,anchor="center")


        for record in records:
            tree.insert("","end",values=list(record))
            # tree.insert("","end",values=record[0])

        tree.grid(row=0,column=0)
        ExitButton = Button(frm1, text="Exit", bg="Blue", fg="White", width=20, command=self.ExitTeacher)
        ExitButton.grid(row=1, column=0, pady=10,padx=50)


        self.masterTeacher.mainloop()


    def AddTeacher(self):
        # This method will open a form for adding a new teacher
        self.masterTeacher = tk.Tk()
        self.master.withdraw()
        self.masterTeacher.deiconify()
        self.masterTeacher.title("SkyLiners High School New Teachers Registration.")
        self.masterTeacher.geometry("750x500+200+100")
        self.masterTeacher.config(padx=60, pady=50)

        frm1 = Frame(self.masterTeacher)
        frm1.grid(row=0,column=0)
        frm2 = Frame(self.masterTeacher)
        frm2.grid(row=0, column=1)
        lbl = Label(frm1, text ="Proceed to register.\nEnsure you fill out all the fields.!!")
        lbl.grid(row = 0,column=1)
        # Registration Number Entry and Label
        TIdReg_label = Label(frm1, text="Employment ID:")
        TIdReg_label.grid(row=1, column=0)
        self.TIdReg_Entry = tk.Entry(frm1, width=20)
        self.TIdReg_Entry.grid(row=2, column=0)

        # Age Entry and Label
        TAge_label = Label(frm1, text="Teacher's Age")
        TAge_label.grid(row=1, column=1)
        self.TAge_Entry = tk.Spinbox(frm1, from_= 25, to= 59, width=20)
        self.TAge_Entry.grid(row=2, column=1)

        # Name Entry and Label
        TName_label = Label(frm1, text="Teacher's Name")
        TName_label.grid(row=3, column=0)
        self.TName_Entry = tk.Entry(frm1, width=20)
        self.TName_Entry.grid(row=4, column=0)

        # Stream Entry and Label
        TStream_label = tk.Label(frm1, text="Stream Handled:")
        TStream_label.grid(row=3, column=1)
        self.TStream_Entry = Combobox(frm1, width=20, values=['North', 'South', 'East', 'West'])
        self.TStream_Entry.grid(row=4, column=1)

        # Form_Taught Entry and Label
        TForm_label = tk.Label(frm1, text="Form Handled:")
        TForm_label.grid(row=5, column=0)
        self.TForm_Entry = Combobox(frm1, width=20, values=['1', ' 2', ' 3', ' 4'])
        self.TForm_Entry.grid(row=6, column=0)

        trCounty_label = tk.Label(frm1, text="County Code")
        trCounty_label.grid(row=5, column=1)
        self.trCountyEntry = Combobox(frm1, width=20, values=[f"{i}" for i in range(1, 48, 1)])
        self.trCountyEntry.grid(row=6, column=1)
        self.trCountyEntry.set("Select County")

        # Subjects Entry and Label
        subjects = ['MATHS', 'ENGLISH', 'KISWAHILI', 'BIOLOGY', 'CHEMISTRY', 'PHYSICS', 'GEOGRAPHY', 'HISTORY', 'CRE', 'COMPUTER_STUDIES']
        Tsubj_label = Label(frm2, text="Subject List:")
        Tsubj_label.grid(row=0, column=0)
        self.Tsubj_Entry = Listbox(frm2, width=20,selectmode=MULTIPLE)
        for item in subjects:
            self.Tsubj_Entry.insert(END,item)
        self.Tsubj_Entry.grid(row=1, column=0)

        RegisterButton = Button(frm1, text="Register", bg="Blue",fg="White",  width = 20, command= self.RegisterTeacher)
        RegisterButton.grid(row=8, column=0,  pady=10)

        ExitButton = Button(frm1, text="Exit", bg="Blue",fg="White", width = 20, command=self.ExitTeacher)
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
        tsubject = [self.Tsubj_Entry.get(idx) for idx in self.Tsubj_Entry.curselection()]
        # tsubject = self.Tsubj_Entry.get()
        value_str = ','.join(tsubject)
        tcounty = self.trCountyEntry.get()

        connection = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
        dataAccess = connection.cursor()

        dataAccess.execute("SELECT EMP_NO from TeachersData")
        fetched_Ids = dataAccess.fetchall()

        if tId not in fetched_Ids:
            if tId != "" and tName != "" and tsubject != "":
                # Insert the new record
                dataAccess.execute(f"INSERT INTO TeachersData (EMP_NO,  NAME, AGE, COUNTY, STREAM_T, FORM_T, SUBJECT_T)  VALUES ('{tId}', '{tName}', {tage}, {tcounty}, '{tstream}', {tform}, '{value_str}')")
                # Commit the changes
                dataAccess.commit()
                dataAccess.close()
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
    def ViewReports(self):
        # This method will show all the Student Reports in a new window
        # This method will open a form for displaying all Student Reports
        global col, i
        self.masterTeacher = tk.Tk()
        self.master.withdraw()
        self.masterTeacher.deiconify()
        self.masterTeacher.title("SkyLiners High School  Student Exam Reports.")
        self.masterTeacher.geometry("1200x500+100+100")
        self.masterTeacher.resizable(width=True, height=True)
        self.masterTeacher.config(padx=60, pady=50)
        frm1 = Frame(self.masterTeacher)
        frm1.grid(row=0, column=0)

        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM ExamRecords')
        records = cursor.fetchall()

        tree = ttk.Treeview(frm1)
        tree["columns"] = tuple(range(len(records[0])))
        tree["show"] = "headings"
        # for i, col in enumerate(records[0]):
        for i, col in enumerate(cursor.description):
            tree.heading(i, text=col[0])

        col_width = max(max(len(str(row[i])) for row in records), len(col[0])) * 15
        for i, col in enumerate(records[0]):
            tree.column(i, width=col_width, anchor="center")

        for record in records:
            tree.insert("", "end", values=list(record))
            # tree.insert("","end",values=record[0])

        tree.grid(row=0, column=0)
        ExitButton = Button(frm1, text="Exit", bg="Blue", fg="White", width=20, command=self.ExitTeacher)
        ExitButton.grid(row=1, column=0, pady=10, padx=50)

        self.masterTeacher.mainloop()

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

        self.UsernameEntry = Entry(mainFrame,width=20)
        self.UsernameEntry.grid(row = 2,column=0)

        self.Passwordentry = Entry(mainFrame,width=20)
        self.Passwordentry.grid(row = 2, column=1)
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')

        registerButton = Button(mainFrame,text="Register Admin", bg="Blue", fg="White", width=20, command=lambda:self.RegisterAdmin(connect=conn))
        registerButton.grid(row = 5,column=0,padx=35,pady=20)

        exitButton = Button(mainFrame, text="Exit ", bg="Blue", fg="White", width=20, command=self.Quit)
        exitButton.grid(row=5, column=1, padx=35, pady=20)
    def Quit(self):
        self.adminmaster.withdraw()
        # self.welcomemaster.deiconify()


    def RegisterAdmin(self,connect):
        passw = self.Passwordentry.get()
        user = self.UsernameEntry.get()
        conn = connect
        if user != "" and passw != "":
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
                elif len(passw) < 4:
                    messagebox.showerror("Password Error! ", "Password must be Greater than 4 digits or letters .")
                    self.LogClear()
                    self.adminmaster.deiconify()

                elif len(passw) > 6:
                    messagebox.showerror("Password Error! ", "Password must not be Greater than 6 digits or letters .")
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
        self.Passwordentry.delete(0,'end')
        self.UsernameEntry.delete(0,'end')
        self.UsernameEntry.focus()

    def launch_admin_window(self):
        admin = AdminDashboardPage()
        admin.AdminLogin()
# admin = AdminDashboardPage()
# # admin.AdminLogin()
