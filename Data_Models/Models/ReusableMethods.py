import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from tkinter.ttk import Combobox

import bcrypt
import pyodbc
import tkinter as tk
from tkinter import ttk, messagebox


def hash_password(password: str) -> bytes:
    """
    Returns a hashed password
    Args:
        password (str): password to be hashed
    """
    b = password.encode()
    hashed = bcrypt.hashpw(b, bcrypt.gensalt())
    # messagebox.showinfo('Hashed',f'HASHED Password:{hashed}')
    return hashed



def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check whether a password is valid
    Args:
        hashed_password (bytes): hashed password
        password (str): password in string
    Return:
        bool
    """
    return bcrypt.checkpw(password.encode(), hashed_password)

hash_password('Sunday')
is_valid(hash_password('Sunday'),'Sunday')

def ClearLoginFields(self):
    self.UsernameEntry.delete(0, 'end')
    self.PasswordEntry.delete(0, 'end')
    self.UsernameEntry.focus()


def StudentInfo(self, title, query):
    # This method will show all the registered teachers in a new window
    # This method will open a form for displaying all teachers
    toptitle = title
    aquery = query
    global col, i
    self.masterTeacher = tk.Tk()
    # self.master.withdraw()
    self.masterTeacher.deiconify()
    self.masterTeacher.title(f"SkyLiners High School {toptitle}")
    self.masterTeacher.geometry("1100x500+200+100")
    self.masterTeacher.resizable(width=True, height=True)
    self.masterTeacher.config(padx=100, pady=50)
    frm1 = Frame(self.masterTeacher)
    frm1.grid(row=0, column=0)

    conn = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
    cursor = conn.cursor()
    # cursor.execute('SELECT * FROM StudentData')
    # records = cursor.fetchall()

    cursor.execute(aquery)
    class_records = cursor.fetchall()
    tree = ttk.Treeview(frm1)
    tree["columns"] = tuple(range(len(class_records[0])))
    tree["show"] = "headings"
    # for i, col in enumerate(records[0]):
    for i, col in enumerate(cursor.description):
        tree.heading(i, text=col[0])

    col_width = min(max(len(str(row[i])) for row in class_records), len(col[0])) * 5
    for i, col in enumerate(class_records[0]):
        tree.column(i, width=col_width, anchor="center")

    # for i, col in enumerate(class_records[0]):
    #     # Get the maximum length of the content in the column
    #     max_length = min(len(str(cursor.description[i])) for row in class_records)
    #     # Set the column width based on the maximum content length
    #     col_width = max_length * 5
    #     # Set the column width and alignment
    #     tree.column(i, width=col_width, anchor="center")

    # col_width = lambda i: max(len(str(row[i])) for row in class_records) * 10
    # [tree.column(i, width=min(col_width(i), len(str(col)) * 10), anchor="center") for i, col in
    #  enumerate(class_records[0])]

    for record in class_records:
        tree.insert("", "end", values=list(record))
        # tree.insert("","end",values=record[0])

    tree.grid(row=0, column=0, sticky='nsew')

    ExitButton = Button(frm1, text="Exit", bg="Blue", fg="White", width=20, command=self.ExitTeacher)
    ExitButton.grid(row=1, column=0, pady=10, padx=50)

    self.masterTeacher.mainloop()


# Sending mails
def SendMail(self):
    messagebox.askquestion("Valid", "Want to send report?")
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
    subject = "EXAM REPORT FOR ", reg, "Registration Number: ", reg, "\n Mathematics: 67 "
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

#Editting Student Details
#
class EditStud:

    def RegisterStudent(self):
        self.master.withdraw()
        self.studentmaster = Toplevel(self.root)
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
        self.Reg_Entry = tk.Entry(stdframe, width=10,state='disabled')
        self.Reg_Entry.grid(row=1, column=1)
        self.Reg_Entry.bind(self.GetReg())

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

    def GetReg(self):
        connectreg = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
        cursor = connectreg.cursor()

        cursor.execute('SELECT REG_NO FROM StudentData')
        fetched_regs = cursor.fetchall()
        reg = [row[0]for row in fetched_regs][-1]
        # reg = fetched_regs[-1]
        # print(reg)
        reg1 = reg[0:3]
        reg2 = reg[3::]
        regg = int(reg2)
        regg += 1
        self.new_reg = str(reg1) + str(regg)
        # print(self.new_reg)
        self.Reg_Entry.config(state='normal')
        self.Reg_Entry.delete(0,END)
        self.Reg_Entry.insert(0,self.new_reg)
        self.Reg_Entry.config(state='disabled')
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
        self.valid = re.match(pattern, mail) is not None
        if not self.valid:
            messagebox.showerror("Invalid email!", "Input the email in the correct format!!")
            if mail == self.MotherEmail_Entry.get():
                messagebox.showerror("Mail Error","Input the Mother's Email Correctly.")
                self.MotherEmail_Entry.focus()
            elif mail == self.FatherEmail_Entry.get():
                messagebox.showerror("Mail Error","Input the Father's Email Correctly.")
                self.FatherEmail_Entry.focus()

    def validateContact(self, contact):
        if len(contact) != 10:
            messagebox.showerror("Invalid Contact!", "Contact must be only 10 digits long!!")
            if contact == self.FatherContact_Entry.get():
                messagebox.showerror("Contact Error","Input the Father's Contact Correctly.")
                self.FatherContact_Entry.focus()
            elif contact == self.MotherContact_Entry.get():
                messagebox.showerror("Contact Error","Input the Mother's Contact Correctly.")
                self.MotherContact_Entry.focus()

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



