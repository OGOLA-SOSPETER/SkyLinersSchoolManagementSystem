import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

import pyodbc

class TeacherDashboardPage:
    def __init__(self):
        self.teachermaster = tk.Tk()
        self.teachermaster.title("Teachers Login Page")

    def TeacherLogin(self):
        master_frame = Frame(self.teachermaster)
        master_frame.pack()
        self.teachermaster.geometry("650x280+210+100")
        self.teachermaster.config(padx=10, pady=50)
        label1 = tk.Label(master_frame, text="Welcome to the Teachers Login  dashboard.", font='Arial, 10')
        label1.grid(row=0, column=1, columnspan=3)

        # UserName Entry.
        UsernameLabel = tk.Label(master_frame, text="Staff Id", bg="#EDEDED", fg="#06283D")
        UsernameLabel.grid(row=2, column=1)
        self.UsernameEntry = Entry(master_frame, width=30)
        self.UsernameEntry.grid(row=3, column=1, padx=10)

        # Password Entry.
        PasswordLabel = tk.Label(master_frame, text="Password", bg="#EDEDED", fg="#06283D")
        PasswordLabel.grid(row=2, column=2)
        self.PasswordEntry = Entry(master_frame, width=30, show="*")
        self.PasswordEntry.grid(row=3, column=2, padx=10)

        # Login Button
        LoginButton = Button(master_frame, text="Login", bg="blue", fg="white", width=20, command=self.ValidateUser,justify=CENTER)
        LoginButton.grid(row=5, column=1, padx=30, pady=20)

        # Login Button
        RegisterButton = Button(master_frame, text="Register", bg="blue", fg="white", width=20, command=lambda:self.NewTeacher(),justify=CENTER)
        RegisterButton.grid(row=5, column=2, pady=20)

        ExitButton = Button(master_frame, text="Exit", bg="blue", fg="white", width=20, command=self.ExitTeacher)
        ExitButton.grid(row=6, column=1,  padx=115, pady=1)
        self.teachermaster.mainloop()
    def ValidateUser(self):
        username = self.UsernameEntry.get()
        password = self.PasswordEntry.get()

        errorcount = 0
        if username != "" and password != "":
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
            cursor = conn.cursor()

            # Fetching the password for the given username
            cursor.execute(f"select Password from TeacherLogin WHERE Username = '{username}'")
            fetched_password = cursor.fetchone()
            cursor.execute("select  Username from TeacherLogin ")
            fetched_users = cursor.fetchall()
            if fetched_password:
                if fetched_password[0] == password:
                    messagebox.showinfo("Login Success", "Login Successful")
                    self.ClearLoginFields()
                    self.teachermaster.withdraw()
                    self.TeacherDashBoard()
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
                                     "UserName Not Registered!!\nKindly Register  To login!")
                self.ClearLoginFields()
        else:
            messagebox.showerror("Empty Fields.","The userName and Password Fields Must be Filled!")
            self.ClearLoginFields()
    def TeacherDashBoard(self):
        self.teachermaster.geometry("550x250+210+100")
        self.teachermaster.deiconify()
        self.teachermaster.config(padx=100, pady=50)
        UpdateButton = Button(self.teachermaster, text="Update DataBase", width=15, command=self.UpdateRecords)
        UpdateButton.grid(row=1, column=0)

        detailsLabel = LabelFrame(self.teachermaster, text="Student Info")
        detailsLabel.grid(row=1, column=1, padx=25)

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
        self.Total_Entry = Entry(detailsLabel, width=10,state='disabled')
        self.Total_Entry.grid(row=10, column=1)

        # Average Entry and Label
        Average_label = Label(detailsLabel, text="Average")
        Average_label.grid(row=10, column=3)
        self.Average_Entry = Entry(detailsLabel, width=10,state='disabled')
        self.Average_Entry.grid(row=10, column=4)

        # Grade Entry and Label
        Grade_label = Label(detailsLabel, text="Grade",state='disabled')
        Grade_label.grid(row=10, column=5)
        self.Grade_Entry = Entry(detailsLabel, width=10)
        self.Grade_Entry.grid(row=10, column=6)
        self.teachermaster.mainloop()
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

        results = messagebox.askyesno("Add Records to DataBase",f"Do you want to add the Exam Records for {self.reg} to the database?")
        if results:
            self.UpdateDataBase()
    def UpdateDataBase(self):

        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\ExamRecords.accdb;')
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
        conn.close()
        cursor.close()

    def ClearLoginFields(self):
        self.UsernameEntry.delete(0, 'end')
        self.PasswordEntry.delete(0, 'end')
        self.UsernameEntry.focus()

    def ExitTeacher(self):
        self.teachermaster.withdraw()

    def NewTeacher(self):
        self.newmaster = tk.Tk()
        self.newmaster.geometry("550x300+200+150")
        self.newmaster.config(padx = 10, pady = 10)
        self.newmaster.title("Teacher Registration.")

        mainFrame = tk.Frame(self.newmaster)
        mainFrame.pack()

        mainLabel = Label(mainFrame,text = "New Teacher Registration.")
        mainLabel.grid(row = 0, column=0)

        usernamelabel = Label(mainFrame,text="Staff Id")
        usernamelabel.grid(row=1,column=0)
        passwordlabel = Label(mainFrame,text="Password.")
        passwordlabel.grid(row = 1,column=1)

        self.UsernameEntry = Entry(mainFrame,width=20)
        self.UsernameEntry.grid(row = 2,column=0)

        self.Passwordentry = Entry(mainFrame,width=20)
        self.Passwordentry.grid(row = 2, column=1)
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')

        registerButton = Button(mainFrame,text="Register Teacher", bg="Blue", fg="White", width=20, command=lambda:self.RegisterTeacher(connect=conn))
        registerButton.grid(row = 5,column=0,padx=35,pady=20)

        exitButton = Button(mainFrame, text="Exit ", bg="Blue", fg="White", width=20, command=self.Quit)
        exitButton.grid(row=5, column=1, padx=35, pady=20)
        self.newmaster.mainloop()
    def Quit(self):
        self.newmaster.withdraw()
        # self.welcomemaster.deiconify()

    def RegisterTeacher(self,connect):
        passw = self.Passwordentry.get()
        user = self.UsernameEntry.get()
        conn = connect
        if user != "" and passw != "":
            cursor = conn.cursor()

            # Fetching the password for the given username
            cursor.execute("SELECT EMP_NO FROM TeachersData ")
            registered_users = cursor.fetchall()

            # Fetching the password for the given username
            cursor.execute(f"SELECT Password FROM TeacherLogin WHERE Username = '{user}'")
            fetched_password = cursor.fetchone()

            if user not in registered_users:
                messagebox.showwarning("Invalid Id","The Teacher Id is Not Registered within our systems.\nKindly Contact the administrator first for Registration.")
                self.LogClear()
            else:

                if fetched_password:
                    messagebox.showerror("Invalid User", "Username already exists. Please choose a different one.")
                    self.LogClear()
                    self.newmaster.deiconify()
                else:
                    cursor.execute(f"SELECT Username FROM TeacherLogin WHERE Password = '{passw}'")
                    fetched_username = cursor.fetchone()

                    if fetched_username:
                        messagebox.showerror("Password Error! ", "Password already used. Please choose a different one.")
                        self.LogClear()
                        self.newmaster.deiconify()
                    elif len(passw) < 4:
                        messagebox.showerror("Password Error! ", "Password must be Greater than 4 digits or letters .")
                        self.LogClear()
                        self.newmaster.deiconify()

                    elif len(passw) > 6:
                        messagebox.showerror("Password Error! ", "Password must not be Greater than 6 digits or letters .")
                        self.LogClear()
                        self.teachermaster.deiconify()

                    else:
                        cursor.execute(f"INSERT INTO TeacherLogin (Username, Password) VALUES ('{user}', '{passw}')")
                        cursor.commit()
                        cursor.close()
                        messagebox.showinfo("Registration Success", "Teacher Successfully Registered!")
                        self.LogClear()
                        self.newmaster.withdraw()
                        self.teachermaster.deiconify()

        else:
            messagebox.showerror("Empty Fields Error", "Please enter both  username and  password.")
            self.newmaster.deiconify()
            self.LogClear()

    def LogClear(self):
        self.Passwordentry.delete(0,'end')
        self.UsernameEntry.delete(0,'end')
        self.UsernameEntry.focus()


    def launch_teacher_window(self):
        techr = TeacherDashboardPage()
        techr.TeacherLogin()

