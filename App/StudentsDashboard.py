import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pyodbc
from datetime import date

class StudentsDashboardPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Dashboard")
        self.master = tk.Tk()


    def StudentDashBoard(self):
        self.root.geometry("700x400+210+100")
        self.root.deiconify()
        self.root.config(padx=80)
        # self.root.config(bg="#06283D")

        label1 = tk.Label(self.root, text="Welcome to the student dashboard.")
        label1.grid(row=0, column=0, columnspan=3)

        label2 = tk.Label(self.root, text="Kindly LOGIN.")
        label2.grid(row=1, column=0, columnspan=2)

        root_frame = tk.LabelFrame(self.root, text="Login Details.",fg="#06283D")
        root_frame.grid(row=3, column=1, padx=130, pady=20,sticky=tk.W+tk.E)

        # UserName Entry.
        UsernameLabel = tk.Label(root_frame, text="UserName", bg="#EDEDED", fg="#06283D")
        UsernameLabel.grid(row=0, column=0)
        self.UsernameEntry = Entry(root_frame, width=30)
        self.UsernameEntry.grid(row=0, column=1, padx=10)

        # Password Entry.
        PasswordLabel = tk.Label(root_frame, text="Password", bg="#EDEDED", fg="#06283D")
        PasswordLabel.grid(row=1, column=0)
        self.PasswordEntry = Entry(root_frame, width=30, show="*")
        self.PasswordEntry.grid(row=1, column=1, padx=10)

        # Login Button
        LoginButton = Button(root_frame, text="Login", bg="#06283D", fg="white", command=self.ValidateUser,justify=CENTER)
        LoginButton.grid(row=4, column=1,sticky=tk.W+tk.E,columnspan=1,padx=25)

        # RegisterLabel = tk.Label(self.root, text="If Not Registered, kindly proceed to register here.")
        # RegisterLabel.grid(row=5, column=0, columnspan=2)
        #
        # RegisterButton = Button(self.root, text="Register", bg="#06283D", fg="white", command=self.RegisterStudent)
        # RegisterButton.grid(row=6, column=0, columnspan=2, pady=10)

        self.root.mainloop()

    def ValidateUser(self):
        username = self.UsernameEntry.get()
        password = self.PasswordEntry.get()

        errorcount = 0
        if username != "" and password != "":
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\SchoolUsers.accdb;')
            cursor = conn.cursor()

            # Fetching the password for the given username
            cursor.execute(f"select Password from StudentLogin WHERE Username = '{username}'")
            fetched_password = cursor.fetchone()
            cursor.execute("select  Username from StudentLogin ")
            fetched_users = cursor.fetchall()
            if fetched_password:
                if fetched_password[0] == password:
                    messagebox.showinfo("Login Success", "Login Successful")
                    self.ClearLoginFields()
                    self.root.withdraw()
                    self.Records()
                else:
                    errorcount += 1
                    if errorcount >= 3:
                        messagebox.showwarning("Access Failure!",
                                               "You have exceeded the attempts.\nTry again after 30 minutes.")
                    else:
                        messagebox.showerror("Login Error", "Invalid Password")
                        self.ClearLoginFields()

            else:
                # messagebox.showerror("Login Error", "Username Not Found")
                messagebox.showerror("Username Not Found!",
                                     "UserName Not Registered!!\nKindly Contact the Administrator!")
                self.ClearLoginFields()
        else:
            messagebox.showerror("Empty Fields.","The userName and Password Fields Must be Filled!")
            self.ClearLoginFields()
    def ClearLoginFields(self):
        self.UsernameEntry.delete(0, 'end')
        self.PasswordEntry.delete(0, 'end')
        self.UsernameEntry.focus()
    def Records(self):
        self.master.title("SkyLiners High School Student Exam Records")
        self.master.geometry("1000x600+250+100")

        frame = tk.Frame(self.master, borderwidth=3)
        frame.pack()


        # Registration Number Entry and Label
        dateLabel = Label(frame,text="Date: ")
        dateLabel.grid(row=0,column=2,padx=25)

        Date = StringVar()
        today = date.today()
        d1 = today.strftime("%d/%m/%y")
        Date.set(d1)

        dateEntry = Entry(frame,textvariable=Date,width=13,font="ariel 13 ")
        dateEntry.grid(row=0,column=3,padx=25)




        detailsLabel = LabelFrame(frame,text="Student Info")
        detailsLabel.grid(row=1,column=1,padx=25)
        Reg_label = Label(detailsLabel, text="Reg_Number")
        Reg_label.grid(row=3, column=0)
        self.Reg_Entry = Entry(detailsLabel, width=10)
        self.Reg_Entry.grid(row=3, column=1)

        # Mathematics Entry and Label
        Maths_label = Label(detailsLabel, text="Maths")
        Maths_label.grid(row=4, column=0)
        self.Maths_Entry = Entry(detailsLabel, width=10)
        self.Maths_Entry.grid(row=4, column=1)


        # English Entry and Label
        English_label = Label(detailsLabel, text="English")
        English_label.grid(row=4, column=4)
        self.English_Entry = Entry(detailsLabel, width=10)
        self.English_Entry.grid(row=4, column=5)


        # Kiswahili Entry and Label
        Kiswahili_label = Label(detailsLabel, text="Kiswahili")
        Kiswahili_label.grid(row=5, column=0)
        self.Kiswahili_Entry = Entry(detailsLabel, width=10)
        self.Kiswahili_Entry.grid(row=5, column=1)


        # Biology Entry and Label
        Biology_label = Label(detailsLabel, text="Biology")
        Biology_label.grid(row=5, column=4)
        self.Biology_Entry = Entry(detailsLabel, width=10)
        self.Biology_Entry.grid(row=5, column=5)


        # Chemistry Entry and Label
        Chemistry_label = Label(detailsLabel, text="Chemistry")
        Chemistry_label.grid(row=6, column=0)
        self.Chemistry_Entry = Entry(detailsLabel, width=10)
        self.Chemistry_Entry.grid(row=6, column=1)


        # Physics Entry and Label
        Physics_label = Label(detailsLabel, text="Physics")
        Physics_label.grid(row=6, column=4)
        self.Physics_Entry = Entry(detailsLabel, width=10)
        self.Physics_Entry.grid(row=6, column=5)


        # Geography Entry and Label
        Geography_label = Label(detailsLabel, text="Geography")
        Geography_label.grid(row=7, column=0)
        self.Geography_Entry = Entry(detailsLabel, width=10)
        self.Geography_Entry.grid(row=7, column=1)


        # History Entry and Label
        History_label = Label(detailsLabel, text="History")
        History_label.grid(row=7, column=4)
        self.History_Entry = Entry(detailsLabel, width=10)
        self.History_Entry.grid(row=7, column=5)


        # CRE Entry and Label
        CRE_label = Label(detailsLabel, text="CRE")
        CRE_label.grid(row=8, column=0)
        self.CRE_Entry = Entry(detailsLabel, width=10)
        self.CRE_Entry.grid(row=8, column=1)


        # Computer Entry and Label
        Computer_label = Label(detailsLabel, text="Computer")
        Computer_label.grid(row=8, column=4)
        self.Computer_Entry = Entry(detailsLabel, width=10)
        self.Computer_Entry.grid(row=8, column=5)

        # Total Entry and Label
        Total_label = Label(detailsLabel, text="Total")
        Total_label.grid(row=10, column=0)
        self.Total_Entry = Entry(detailsLabel, width=10)
        self.Total_Entry.grid(row=10, column=1)

        # Average Entry and Label
        Average_label = Label(detailsLabel, text="Average")
        Average_label.grid(row=10, column=3)
        self.Average_Entry = Entry(detailsLabel, width=10)
        self.Average_Entry.grid(row=10, column=4)

        # Grade Entry and Label
        Grade_label = Label(detailsLabel, text="Grade")
        Grade_label.grid(row=10, column=5)
        self.Grade_Entry = Entry(detailsLabel, width=10)
        self.Grade_Entry.grid(row=10, column=6)

        buttonsFrame = Frame(frame)
        buttonsFrame.grid(row=1, column=2, padx=25)

        DisplayButton = Button(buttonsFrame, text="DisplayRecords",width=15, command=self.DisplayScores)
        DisplayButton.grid(row=1, column=0)

        UpdateButton = Button(buttonsFrame, text="Update DataBase",width=15, command=self.UpdateRecords)
        UpdateButton.grid(row=2, column=0)

        ClearButton = Button(buttonsFrame,text="Clear",width=15, command=self.ClearFields)
        ClearButton.grid(row=3,column=0)

        ExitButton = Button(buttonsFrame, text="Exit",width=15, command=self.Close)
        ExitButton.grid(row=4, column=0)


        self.master.mainloop()

    def DisplayScores(self):
        try:
            self.reg = self.Reg_Entry.get()
            # establish database connection
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\ExamRecords.accdb;')
            cursor = conn.cursor()

            # retrieve subject scores for given registration number
            cursor.execute(
                f"SELECT MATHS, ENGLISH, KISWAHILI, BIOLOGY, CHEMISTRY, PHYSICS, GEOGRAPHY, HISTORY, CRE, COMPUTER_STUDIES, TOTAL, AVERAGE, GRADE FROM ExamRecords WHERE REG_NO='{self.reg}'")
            row = cursor.fetchone()

            # display scores in entry boxes
            if row:

                self.Reg_Entry.delete(0, 'end')
                self.Reg_Entry.insert(0, self.reg)

                self.Maths_Entry.delete(0, 'end')
                self.Maths_Entry.insert(0, row[0])

                self.English_Entry.delete(0, 'end')
                self.English_Entry.insert(0, row[1])

                self.Kiswahili_Entry.delete(0, 'end')
                self.Kiswahili_Entry.insert(0, row[2])

                self.Biology_Entry.delete(0, 'end')
                self.Biology_Entry.insert(0, row[3])

                self.History_Entry.delete(0, 'end')
                self.History_Entry.insert(0, row[7])

                self.Chemistry_Entry.delete(0, 'end')
                self.Chemistry_Entry.insert(0, row[4])

                self.Physics_Entry.delete(0, 'end')
                self.Physics_Entry.insert(0, row[5])

                self.Geography_Entry.delete(0, 'end')
                self.Geography_Entry.insert(0, row[6])

                self.CRE_Entry.delete(0, 'end')
                self.CRE_Entry.insert(0, row[8])

                self.Computer_Entry.delete(0, 'end')
                self.Computer_Entry.insert(0, row[9])

                self.Total_Entry.delete(0, 'end')
                self.Total_Entry.insert(0, row[10])

                self.Average_Entry.delete(0, 'end')
                self.Average_Entry.insert(0, row[11])

                self.Grade_Entry.delete(0, 'end')
                self.Grade_Entry.insert(0, row[12])
            else:
                messagebox.showerror("Error", f"No record found for registration number {self.reg}")

            # close database connection
            conn.close()

        except pyodbc.Error as e:
            messagebox.showerror("Error", str(e))

    def ClearFields(self):
        response = messagebox.askyesno("Clear Fields.", f"Do you want to clear the Entries for  {self.reg} ?")
        if response:
            self.Reg_Entry.selection_clear()
            self.Reg_Entry.delete(0, 'end')
            self.Maths_Entry.delete(0, 'end')
            self.English_Entry.delete(0, 'end')
            self.Kiswahili_Entry.delete(0, 'end')
            self.Biology_Entry.delete(0, 'end')
            self.History_Entry.delete(0, 'end')
            self.Chemistry_Entry.delete(0, 'end')
            self.Physics_Entry.delete(0, 'end')
            self.Geography_Entry.delete(0, 'end')
            self.CRE_Entry.delete(0, 'end')
            self.Computer_Entry.delete(0, 'end')
            self.Total_Entry.delete(0, 'end')
            self.Average_Entry.delete(0, 'end')
            self.Grade_Entry.delete(0, 'end')
        else:
           pass

    def Close(self):
        self.master.withdraw()
        self.root.deiconify()
        # exit()

    def UpdateRecords(self):
        self.reg = self.Reg_Entry.get()
        self.math = int(self.Maths_Entry.get())
        self.eng = int(self.English_Entry.get())
        self.kis = int(self.Kiswahili_Entry.get())
        self.bio = int(self.Biology_Entry.get())
        self.chem = int(self.Chemistry_Entry.get())
        self.phy = int(self.Physics_Entry.get())
        self.geo = int(self.Geography_Entry.get())
        self.hist = int(self.History_Entry.get())
        self.cr = int(self.CRE_Entry.get())
        self.comp = int(self.Computer_Entry.get())
        self.tot = int(self.Total_Entry.get())
        self.av = float(self.Average_Entry.get())
        self.grd = self.Grade_Entry.get()

        self.tot = self.math + self.eng + self.kis + self.chem + self.bio + self.phy + self.geo + self.hist + self.cr + self.comp
        self.av = (self.math + self.eng + self.kis + self.chem + self.bio + self.phy + self.geo + self.hist + self.cr + self.comp)/10

        if 80 <= self.av <= 100:
            self.Grade = ' A '
            self.comment = "Excellent Performance"

        elif 60 <= self.av <= 79:
            self.Grade = ' B '
            self.comment = " A Good Performance "

        elif 50 <= self.av <= 59:
            self.Grade = ' C '
            self.comment = "Put in more effort"

        elif 40 <= self.av <= 49:
            self.Grade = ' D '
            self.comment = " Poor "

        else:
            self.Grade = ' E '
            self.comment = "Below Average. You Fail"
        # conn = pyodbc.connect(
        #     r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\ExamRecords.accdb;')
        # cursor = conn.cursor()
        #
        # # Fetching the password for the given username
        # cursor.execute(f"select * from ExamRecords WHERE REG_NO = '{self.reg}'")
        # fetched_data = cursor.fetchall()
        # # messagebox.showinfo("Data", f"{self.reg}, {self.math}, {self.eng}")
        #
        # if self.reg in fetched_data and self.math != "" and self.eng !="" and self.kis != "" and self.bio != "":
        #     update_query = f"UPDATE ExamRecords SET MATHS = '{self.math}', ENGLISH = '{self.eng}', KISWAHILI = '{self.kis}', BIOLOGY = '{self.bio}', CHEMISTRY = '{self.chem}', TOTAL ='{self.tot}', AVERAGE = '{self.av}' WHERE REG_NO = '{self.reg}'"
        #
        #     results = cursor.execute(update_query)
        #
        #     if results:
        #         messagebox.showinfo("Update Success.","Records updated successfully.")
        #     else:
        #         messagebox.showerror("Update Failure", "Update Failed.")
        #
        # else:
        #     messagebox.showerror("Null Fields", "Fields cannot be empty!!")

        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\ExamRecords.accdb;')
        cursor = conn.cursor()

        # Fetching the password for the given username
        cursor.execute(f"select * from ExamRecords WHERE REG_NO = '{self.reg}'")
        fetched_data = cursor.fetchone()

        if fetched_data:
            reg, math, eng, kis, bio, hist, chem, phy, geog, cre, comp, tot, av, grd = fetched_data
            if self.math and self.eng and self.kis and self.bio:
                # f"UPDATE ExamRecords SET MATHS = '{self.math}', ENGLISH = '{self.eng}', KISWAHILI = '{self.kis}', BIOLOGY = '{self.bio}', CHEMISTRY = '{self.chem}', TOTAL ='{self.tot}', AVERAGE = '{self.av}' WHERE REG_NO = '{self.reg}'"
                response = messagebox.askyesno("Update Records.", f"Do you want to update the records for {self.reg} ?")
                if response:
                    results = cursor.execute(
                        "UPDATE ExamRecords SET MATHS = ?, ENGLISH = ?, KISWAHILI = ?, BIOLOGY = ?, CHEMISTRY = ?, PHYSICS = ?, GEOGRAPHY = ?, HISTORY = ?, CRE = ?, COMPUTER_STUDIES = ?, TOTAL = ?, AVERAGE = ?, GRADE = ? WHERE REG_NO = ?",
                        self.math, self.eng, self.kis, self.bio, self.chem, self.phy, self.geo, self.hist, self.cr,
                        self.comp, self.tot, self.av, self.Grade, self.reg)

                    if results:
                        messagebox.showinfo("Update Success.", "Records updated successfully.")
                    else:
                        messagebox.showerror("Update Failure", "Update Failed.")
                else:
                    messagebox.showwarning("Cancel Update.","Update Cancelled.")
            else:
                messagebox.showerror("Null Fields", "Fields cannot be empty!!")
        else:
            messagebox.showerror("Invalid Registration Number", "No data found for the given Registration Number!")
        conn.commit()













stud = StudentsDashboardPage()

stud.StudentDashBoard()

