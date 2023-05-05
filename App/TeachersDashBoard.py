import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

from App import ViewEditStudent
from App import StudentsDashboard
from App.AdminDashboard import AdminDashboardPage

import pyodbc

class TeacherDashboardPage(StudentsDashboard.StudentsDashboardPage):
    # def __init__(self):
    #     super().__init__()

    def TeacherLogin(self):
        self.teachermaster = tk.Tk()
        self.teachermaster.title("Administrator")
        self.teachermaster.geometry("600x300+200+100")
        self.teachermaster.config(padx=150,pady=20)

        label1 = tk.Label(self.teachermaster, text="Welcome to the Teachers Login  dashboard.")
        label1.grid(row=0, column=0, columnspan=2)

        label2 = tk.Label(self.teachermaster, text="Kindly LOGIN.")
        label2.grid(row=1, column=0, columnspan=2)

        # UserName Entry.
        UsernameLabel = tk.Label(self.teachermaster, text="UserName")
        UsernameLabel.grid(row=2, column=0)
        self.UsernameEntry = tk.Entry(self.teachermaster, width=30)
        self.UsernameEntry.grid(row=2, column=1)

        # Password Entry.
        PasswordLabel = tk.Label(self.teachermaster, text="Password")
        PasswordLabel.grid(row=3, column=0)
        self.PasswordEntry = tk.Entry(self.teachermaster, width=30, show="*")
        self.PasswordEntry.grid(row=3, column=1)

        # Login Button
        LoginButton = tk.Button(self.teachermaster, text="Login", bg="blue", fg="white", width=20, command=self.ValidateUser)
        LoginButton.grid(row=4, column=0, columnspan=2, pady=10)

        RegisterLabel = tk.Label(self.teachermaster, text="If Not Registered, kindly proceed to register here.")
        RegisterLabel.grid(row=5, column=0, columnspan=2)

        RegisterButton = tk.Button(self.teachermaster, text="Register", bg="blue", fg="white", width=20, command=lambda:self.NewTeacher())
        RegisterButton.grid(row=6, column=0, pady=10)

        ExitButton = tk.Button(self.teachermaster, text="Exit ", bg="blue", fg="white", width=20, command=self.ExitTeacher)
        ExitButton.grid(row=6, column=1, pady=10)

        self.teachermaster.mainloop()
    #
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
        self.dashmaster = tk.Tk()
        self.dashmaster.title(" Teachers  Main DashBoard")
        self.dashmaster.geometry("800x500+210+100")
        self.dashmaster.deiconify()
        self.dashmaster.config(padx=100, pady=50)


        eventsframe = Frame(self.dashmaster)
        eventsframe.grid(row=0, column=1)

        UpdateButton = Button(eventsframe, text="Manage Student Info",bg='blue',fg='white', width=20, command=self.ViewRecords)
        UpdateButton.grid(row=1, column=0,pady =5,padx=10)

        DisplayRecordsButton = Button(eventsframe, text="Manage Exam Records",bg='blue',fg='white', width=20, command=self.Records)
        DisplayRecordsButton.grid(row=1, column=1,pady =5,padx=10)

        EditRecordsButton = Button(eventsframe, text="Edit Records", bg='blue', fg='white', width=20,command=self.UpdateRecords)
        EditRecordsButton.grid(row=2, column=0,pady =5,padx=10)


        ExitButton = Button(eventsframe, text="Exit", width=20,bg='blue',fg='white', command=self.Home)
        ExitButton.grid(row=2, column=1,pady =5,padx=10)


        self.dashmaster.mainloop()
    def ExamInfo(self):
        teacherframe = Frame(self.dashmaster)
        teacherframe.grid(row=0, column=0)
        detailsLabel = LabelFrame(teacherframe, text="Student Info")
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
        self.Maths_Entry.bind('<KeyRelease>', lambda event: self.GetTotalAverage())

        # English Entry and Label
        English_label = Label(detailsLabel, text="English")
        English_label.grid(row=4, column=4)
        self.English_Entry = Entry(detailsLabel, width=10)
        self.English_Entry.grid(row=4, column=5)
        self.English_Entry.bind('<KeyRelease>', lambda event: self.GetTotalAverage())

        # Kiswahili Entry and Label
        Kiswahili_label = Label(detailsLabel, text="Kiswahili")
        Kiswahili_label.grid(row=5, column=0)
        self.Kiswahili_Entry = Entry(detailsLabel, width=10)
        self.Kiswahili_Entry.grid(row=5, column=1)
        self.Kiswahili_Entry.bind('<KeyRelease>', lambda event: self.GetTotalAverage())

        # Biology Entry and Label
        Biology_label = Label(detailsLabel, text="Biology")
        Biology_label.grid(row=5, column=4)
        self.Biology_Entry = Entry(detailsLabel, width=10)
        self.Biology_Entry.grid(row=5, column=5)
        self.Biology_Entry.bind('<KeyRelease>', lambda event: self.GetTotalAverage())

        # Chemistry Entry and Label
        Chemistry_label = Label(detailsLabel, text="Chemistry")
        Chemistry_label.grid(row=6, column=0)
        self.Chemistry_Entry = Entry(detailsLabel, width=10)
        self.Chemistry_Entry.grid(row=6, column=1)
        self.Chemistry_Entry.bind('<KeyRelease>', lambda event: self.GetTotalAverage())

        # Physics Entry and Label
        Physics_label = Label(detailsLabel, text="Physics")
        Physics_label.grid(row=6, column=4)
        self.Physics_Entry = Entry(detailsLabel, width=10)
        self.Physics_Entry.grid(row=6, column=5)
        self.Physics_Entry.bind('<KeyRelease>', lambda event: self.GetTotalAverage())

        # Geography Entry and Label
        Geography_label = Label(detailsLabel, text="Geography")
        Geography_label.grid(row=7, column=0)
        self.Geography_Entry = Entry(detailsLabel, width=10)
        self.Geography_Entry.grid(row=7, column=1)
        self.Geography_Entry.bind('<KeyRelease>', lambda event: self.GetTotalAverage())

        # History Entry and Label
        History_label = Label(detailsLabel, text="History")
        History_label.grid(row=7, column=4)
        self.History_Entry = Entry(detailsLabel, width=10)
        self.History_Entry.grid(row=7, column=5)
        self.History_Entry.bind('<KeyRelease>', lambda event: self.GetTotalAverage())

        # CRE Entry and Label
        CRE_label = Label(detailsLabel, text="CRE")
        CRE_label.grid(row=8, column=0)
        self.CRE_Entry = Entry(detailsLabel, width=10)
        self.CRE_Entry.grid(row=8, column=1)
        self.CRE_Entry.bind('<KeyRelease>', lambda event: self.GetTotalAverage())

        # Computer Entry and Label
        Computer_label = Label(detailsLabel, text="Computer")
        Computer_label.grid(row=8, column=4)
        self.Computer_Entry = Entry(detailsLabel, width=10)
        self.Computer_Entry.grid(row=8, column=5)
        self.Computer_Entry.bind('<KeyRelease>', lambda event: self.GetTotalAverage())

        # Total Entry and Label
        Total_label = Label(detailsLabel, text="Total")
        Total_label.grid(row=10, column=0)
        self.Total_Entry = Entry(detailsLabel, width=10, state='disabled')
        self.Total_Entry.grid(row=10, column=1)

        # Average Entry and Label
        Average_label = Label(detailsLabel, text="Average")
        Average_label.grid(row=10, column=3)
        self.Average_Entry = Entry(detailsLabel, width=10, state='disabled')
        self.Average_Entry.grid(row=10, column=4)

        # Grade Entry and Label
        Grade_label = Label(detailsLabel, text="Grade", state='disabled')
        Grade_label.grid(row=10, column=5)
        self.Grade_Entry = Entry(detailsLabel, width=10)
        self.Grade_Entry.grid(row=10, column=6)
        self.Grade_Entry.bind('<KeyRelease>', lambda event: self.GetGrade())
    def ViewRecords(self):
        viewst = ViewEditStudent.ViewStudentDetails()
        viewst.ViewStudent()
    def Home(self):
        self.dashmaster.withdraw()
        self.teachermaster.deiconify()
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
        # self.tot = int(self.Total_Entry.get())
        # self.av = float(self.Average_Entry.get())
        self.grd = self.Grade_Entry.get()

        # self.tot = self.math + self.eng + self.kis + self.chem + self.bio + self.phy + self.geo + self.hist + self.cr + self.comp
        # self.av = (self.math + self.eng + self.kis + self.chem + self.bio + self.phy + self.geo + self.hist + self.cr + self.comp)/10

        results = messagebox.askyesno("Add Records to DataBase",f"Do you want to add the Exam Records for {self.reg} to the database?")
        if results:
            self.UpdateDataBase()

    def GetTotalAverage(self):
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
        # self.tot = int(self.Total_Entry.get())
        # self.av = float(self.Average_Entry.get())
        # self.grd = self.Grade_Entry.get()
        self.total = self.math + self.eng + self.kis + self.chem + self.bio + self.phy + self.geo + self.hist + self.cr + self.comp
        self.average = (self.math + self.eng + self.kis + self.chem + self.bio + self.phy + self.geo + self.hist + self.cr + self.comp)/10
        self.Total_Entry.config(state='normal')
        self.Total_Entry.delete(0,END)
        self.Total_Entry.insert(0,str(self.total))
        self.Total_Entry.config(state='disabled')

        self.Average_Entry.config(state='normal')
        self.Average_Entry.delete(0, END)
        self.Average_Entry.insert(0, str(self.average))
        self.Average_Entry.config(state='disabled')
    def Records(self):
       stdrec = StudentsDashboard.StudentsDashboardPage()
       stdrec.Records()
    def EditStudentScores(self):
        self.DisplayScores()
        self.EnableFields()
    def GetGrade(self):
        if 80 <= self.average <= 100:
            self.Grade = ' A '
            self.comment = "Excellent Performance"

        elif 60 <= self.average <= 79:
            self.Grade = ' B '
            self.comment = " A Good Performance "

        elif 50 <= self.average <= 59:
            self.Grade = ' C '
            self.comment = "Put in more effort"

        elif 40 <= self.average <= 49:
            self.Grade = ' D '
            self.comment = " Poor "

        else:
            self.Grade = ' E '
            self.comment = "Below Average. You Fail"

        self.Grade_Entry.config(state='normal')
        self.Grade_Entry.delete(0, END)
        self.Grade_Entry.insert(0, self.Grade)
        self.Grade_Entry.config(state='disabled')
    def UpdateDataBase(self):
        self.GetGrade()
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\ExamRecords.accdb;')
        cursor = conn.cursor()

        # Fetching the password for the given username
        cursor.execute(f"select * from ExamRecords WHERE REG_NO = '{self.reg}'")
        fetched_data = cursor.fetchone()

        if fetched_data:
            reg, math, eng, kis, bio, hist, chem, phy, geog, cre, comp, tot, av, grd,cmnt = fetched_data
            if self.math and self.eng and self.kis and self.bio:
                # f"UPDATE ExamRecords SET MATHS = '{self.math}', ENGLISH = '{self.eng}', KISWAHILI = '{self.kis}', BIOLOGY = '{self.bio}', CHEMISTRY = '{self.chem}', TOTAL ='{self.tot}', AVERAGE = '{self.av}' WHERE REG_NO = '{self.reg}'"
                response = messagebox.askyesno("Update Records.", f"There are Records for {self.reg}. Do you want to update the records?")
                if response:
                    results = cursor.execute(
                        "UPDATE ExamRecords SET MATHS = ?, ENGLISH = ?, KISWAHILI = ?, BIOLOGY = ?, CHEMISTRY = ?, PHYSICS = ?, GEOGRAPHY = ?, HISTORY = ?, CRE = ?, COMPUTER_STUDIES = ?, TOTAL = ?, AVERAGE = ?, GRADE = ?, COMMENT=? WHERE REG_NO = ?",
                        self.math, self.eng, self.kis, self.bio, self.chem, self.phy, self.geo, self.hist, self.cr,
                        self.comp, self.total, self.average, self.Grade,self.comment, self.reg)
                    conn.commit()

                    if results:
                        messagebox.showinfo("Update Success.", "Records updated successfully.")
                    else:
                        messagebox.showerror("Update Failure", "Update Failed.")
                else:
                    messagebox.showwarning("Cancel Update.","Update Cancelled.")
            else:
                messagebox.showerror("Null Fields", "Fields cannot be empty!!")
        else:
            response = messagebox.askyesno("Null Records.", f"There is no record for {self.reg}. \nDo you want to add these records? ")
            if response:
                results = cursor.execute(
                    f"INSERT INTO  ExamRecords ( MATHS , ENGLISH , KISWAHILI , BIOLOGY , CHEMISTRY, PHYSICS , GEOGRAPHY, HISTORY, CRE , COMPUTER_STUDIES, TOTAL, AVERAGE , GRADE , REG_NO, COMMENT) VALUES ( {self.math}, {self.eng}, {self.kis}, {self.bio}, {self.chem}, {self.phy}, {self.geo}, {self.hist}, {self.cr},{self.comp}, {self.total}, {self.average}, '{self.Grade}', '{self.reg}', '{self.comment}')")
                conn.commit()

                if results:
                    messagebox.showinfo("Update Success.", f"Records Added successfully for {self.reg}.")
                else:
                    messagebox.showerror("Update Failure", "Records Could Not Be added")
            else:
                messagebox.showwarning("Cancel Update.", "Update Cancelled.")
            # messagebox.showerror("Invalid Registration Number", "No data found for the given Registration Number!")


    def ClearLoginFields(self):
        self.UsernameEntry.delete(0, 'end')
        self.PasswordEntry.delete(0, 'end')
        self.UsernameEntry.focus()

    def ExitTeacher(self):
        self.teachermaster.withdraw()
    def StudentRecords(self):
        stud = StudentsDashboard.StudentsDashboardPage()
        stud.Records()
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

            if user not in [i[0] for i in registered_users]:
                print(registered_users)
                messagebox.showwarning("Invalid Id","The Teacher Id is Not Registered within our systems.\nKindly Contact the administrator first for Registration.")
                self.LogClear()
            else:
                # Fetching the password for the given username
                cursor.execute(f"SELECT Password FROM TeacherLogin WHERE Username = '{user}'")
                fetched_password = cursor.fetchone()

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
                        self.newmaster.deiconify()

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

