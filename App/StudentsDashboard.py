import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pyodbc
from datetime import datetime
from Models import ReusableMethods
class StudentsDashboardPage:
    # def __init__(self):
    def StudentDashBoard(self):

        self.root = tk.Tk()
        self.root.title("Student Dashboard")
        self.root.geometry("600x250+210+100")
        self.root.deiconify()
        self.root.config(padx=60,pady=10)
        # self.root.config(bg="#06283D")

        label1 = tk.Label(self.root, text="Welcome to the student Login.",font='Montserrat, 7 ')
        label1.grid(row=0, column=1, columnspan=3,ipady = 30)

        # UserName Entry.
        UsernameLabel = tk.Label(self.root, text="UserName", bg="#EDEDED", fg="#06283D")
        UsernameLabel.grid(row=2, column=1)
        self.UsernameEntry = Entry(self.root, width=30)
        self.UsernameEntry.grid(row=2, column=2)

        # Password Entry.
        PasswordLabel = tk.Label(self.root, text="Password", bg="#EDEDED", fg="#06283D")
        PasswordLabel.grid(row=3, column=1)
        self.PasswordEntry = Entry(self.root, width=30, show="*")
        self.PasswordEntry.grid(row=3, column=2)

        # Login Button
        LoginButton = Button(self.root, text="Login", bg="blue", fg="white",width=20, command=self.ValidateStudent,justify=CENTER)
        LoginButton.grid(row=5, column=1,padx=20,pady=20)
        # LoginButton.config(padx=40)

        ExitButton = Button(self.root, text="Exit", bg="blue", fg="white",width=20, command=self.ExitStudent)
        ExitButton.grid(row=6, column=1,padx=20,pady=1)

        # RegisterLabel = tk.Label(self.root, text="If Not Registered, kindly proceed to register here.")
        # RegisterLabel.grid(row=5, column=0, columnspan=2)

        RegisterButton = Button(self.root, text="Register Password", bg="blue", fg="white",width=20, command=self.RegisterStudentPassword)
        RegisterButton.grid(row=5, column=2, pady=10)

        self.root.mainloop()


    def ExitStudent(self):
        self.root.withdraw()
        # self.welcomemaster.deiconify()

    def ValidateStudent(self):

        username = self.UsernameEntry.get()
        password = self.PasswordEntry.get()

        errorcount = 0
        if username != "" and password != "":
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
            cursor = conn.cursor()

            # Fetching the password for the given username
            cursor.execute(f"select Password from StudentLogin WHERE Username = '{username}'")
            fetched_password = cursor.fetchone()
            # cursor.execute("select  Username from StudentLogin ")
            # fetched_users = cursor.fetchall()
            cursor.execute("select  REG_NO from StudentData ")
            fetched_user = cursor.fetchall()
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
                if username in [row[0] for row in fetched_user]:
                    messagebox.showerror('Set Password.',"You have not set Your Password. Continue to set your password first.")
                    self.ClearLoginFields()
                # messagebox.showerror("Login Error", "Username Not Found")
                else:
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
        self.master = tk.Tk()
        self.master.title("SkyLiners High School Student Exam Records")
        self.master.geometry("1000x600+250+100")

        frame = tk.Frame(self.master, borderwidth=3)
        frame.pack()


        # Registration Number Entry and Label
        dateLabel = Label(frame,text="Date: ")
        dateLabel.grid(row=0,column=2,padx=25)
        dateEntry = Entry(frame)
        dateEntry.grid(row=0, column=3, padx=25)

        current_date = datetime.now().strftime("%d/-%m-/%y")
        dateEntry.insert(0,current_date)


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

        DisplayButton = Button(buttonsFrame, text="Display Records",width=15, command=self.DisplayScores)
        DisplayButton.grid(row=1, column=0,pady=5)

        EditButton = Button(buttonsFrame, text="Edit Records", width=15, command=self.EditStudentScores)
        EditButton.grid(row=2, column=0,pady=5)

        ClearButton = Button(buttonsFrame,text="Refresh",width=15, command=self.ClearFields)
        ClearButton.grid(row=3,column=0,pady=5)

        UpdateRecordsButton = Button(buttonsFrame, text="Update Records", width=15, command=self.UpdateDataBase)
        UpdateRecordsButton.grid(row=4, column=0, pady=5)

        ExitButton = Button(buttonsFrame, text="Exit",width=15, command=self.Close)
        ExitButton.grid(row=5, column=0)


        self.master.mainloop()

    def DisplayScores(self):
        try:
            reg = self.Reg_Entry.get()
            if reg == "":
                self.EnableFields()
            else:
                self.EnableFields()
                self.FillEntries()
                self.DisableFields()
        except pyodbc.Error as e:
            messagebox.showerror("Error", str(e))


    def ClearFields(self):
        response = messagebox.askyesno("Clear Fields.", f"Do you want to clear the Entries for  {self.reg} ?")
        if response:
            self.EnableFields()
            self.Reg_Entry.delete(0, 'end')
            self.Reg_Entry.focus()
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
            self.DisableFields()
            self.Reg_Entry.config(state='normal')

    def EditStudentScores(self):
        self.DisplayScores()
        self.EnableFields()
        self.Reg_Entry.config(state='disabled')

    def EnableFields(self):
        self.Reg_Entry.config(state='normal')
        self.Maths_Entry.config(state='normal')
        self.English_Entry.config(state='normal')
        self.Kiswahili_Entry.config(state='normal')
        self.Biology_Entry.config(state='normal')
        self.History_Entry.config(state='normal')
        self.Chemistry_Entry.config(state='normal')
        self.Physics_Entry.config(state='normal')
        self.Geography_Entry.config(state='normal')
        self.CRE_Entry.config(state='normal')
        self.Computer_Entry.config(state='normal')
        self.Total_Entry.config(state='normal')
        self.Average_Entry.config(state='normal')
        self.Grade_Entry.config(state='normal')

    def DisableFields(self):
        self.Reg_Entry.config(state='disabled')
        self.Maths_Entry.config(state='disabled')
        self.English_Entry.config(state='disabled')
        self.Kiswahili_Entry.config(state='disabled')
        self.Biology_Entry.config(state='disabled')
        self.History_Entry.config(state='disabled')
        self.Chemistry_Entry.config(state='disabled')
        self.Physics_Entry.config(state='disabled')
        self.Geography_Entry.config(state='disabled')
        self.CRE_Entry.config(state='disabled')
        self.Computer_Entry.config(state='disabled')
        self.Total_Entry.config(state='disabled')
        self.Average_Entry.config(state='disabled')
        self.Grade_Entry.config(state='disabled')
    def FillEntries(self):
        self.reg = self.Reg_Entry.get()
        # establish database connection
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
        cursor = conn.cursor()

        # retrieve subject scores for given registration number
        cursor.execute(
            f"SELECT MATHS, ENGLISH, KISWAHILI, BIOLOGY, CHEMISTRY, PHYSICS, GEOGRAPHY, HISTORY, CRE, COMPUTER_STUDIES, TOTAL, AVERAGE, GRADE FROM ExamRecords WHERE REG_NO='{self.reg}'")
        row = cursor.fetchone()

        # display scores in entry boxes
        if row:

            self.Reg_Entry.delete(0, 'end')
            self.Reg_Entry.insert(0, self.reg)
            # self.Reg_Entry.config(state='disabled')

            self.Maths_Entry.delete(0, 'end')
            self.Maths_Entry.insert(0, row[0])
            # self.Maths_Entry.config(state='disabled')

            self.English_Entry.delete(0, 'end')
            self.English_Entry.insert(0, row[1])
            # self.English_Entry.config(state='disabled')

            self.Kiswahili_Entry.delete(0, 'end')
            self.Kiswahili_Entry.insert(0, row[2])
            # self.Kiswahili_Entry.config(state='disabled')

            self.Biology_Entry.delete(0, 'end')
            self.Biology_Entry.insert(0, row[3])
            # self.Biology_Entry.config(state='disabled')

            self.History_Entry.delete(0, 'end')
            self.History_Entry.insert(0, row[7])
            # self.History_Entry.config(state='disabled')

            self.Chemistry_Entry.delete(0, 'end')
            self.Chemistry_Entry.insert(0, row[4])
            # self.Chemistry_Entry.config(state='disabled')

            self.Physics_Entry.delete(0, 'end')
            self.Physics_Entry.insert(0, row[5])
            # self.Physics_Entry.config(state='disabled')

            self.Geography_Entry.delete(0, 'end')
            self.Geography_Entry.insert(0, row[6])
            # self.Geography_Entry.config(state='disabled')

            self.CRE_Entry.delete(0, 'end')
            self.CRE_Entry.insert(0, row[8])
            # self.CRE_Entry.config(state='disabled')

            self.Computer_Entry.delete(0, 'end')
            self.Computer_Entry.insert(0, row[9])
            # self.Computer_Entry.config(state='disabled')

            self.Total_Entry.delete(0, 'end')
            self.Total_Entry.insert(0, row[10])
            # self.Total_Entry.config(state='disabled')

            self.Average_Entry.delete(0, 'end')
            self.Average_Entry.insert(0, row[11])
            # self.Average_Entry.config(state='disabled')

            self.Grade_Entry.delete(0, 'end')
            self.Grade_Entry.insert(0, row[12])
            # self.Grade_Entry.config(state='disabled')
        else:
            messagebox.showerror("Error", f"No record found for registration number {self.reg}")

        # close database connection
        conn.close()

    def UpdateDataBase(self):
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
        self.average = (self.math + self.eng + self.kis + self.chem + self.bio + self.phy + self.geo + self.hist + self.cr + self.comp) / 10
        self.GetGrade()

        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
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
    def GetGrade(self):
        # self.total = self.math + self.eng + self.kis + self.chem + self.bio + self.phy + self.geo + self.hist + self.cr + self.comp
        # self.average = (self.math + self.eng + self.kis + self.chem + self.bio + self.phy + self.geo + self.hist + self.cr + self.comp) // 10
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
    def RegisterStudentPassword(self):
        self.newmaster = Toplevel(self.root)
        self.newmaster.geometry("550x300+200+150")
        self.newmaster.config(padx=10, pady=10)
        self.newmaster.title("Student Password  Registration.")

        mainFrame = tk.Frame(self.newmaster)
        mainFrame.pack()

        mainLabel = Label(mainFrame, text="Student Password Registration.",font='montserrat 12')
        mainLabel.grid(row=0, column=0,padx=30)

        usernamelabel = Label(mainFrame, text="Student Reg. No.")
        usernamelabel.grid(row=1, column=0)
        passwordlabel = Label(mainFrame, text="Password.")
        passwordlabel.grid(row=1, column=1)

        self.UsernameEntry = Entry(mainFrame, width=20)
        self.UsernameEntry.grid(row=2, column=0)

        self.Passwordentry = Entry(mainFrame, width=20)
        self.Passwordentry.grid(row=2, column=1)
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')

        registerButton = Button(mainFrame, text="Set Password", bg="Blue", fg="White", width=20,
                                command=lambda: self.RegisterPassword(connect=conn))
        registerButton.grid(row=5, column=0, padx=35, pady=20)

        exitButton = Button(mainFrame, text="Exit ", bg="Blue", fg="White", width=20, command=self.Quit)
        exitButton.grid(row=5, column=1, padx=35, pady=20)
        self.newmaster.mainloop()

    def Quit(self):
        self.newmaster.withdraw()
        # self.welcomemaster.deiconify()

    def RegisterPassword(self, connect):
        passw = self.Passwordentry.get()
        user = self.UsernameEntry.get()
        conn = connect
        if user != "" and passw != "":
            cursor = conn.cursor()

            # Fetching the password for the given username
            cursor.execute("SELECT REG_NO FROM StudentData ")
            registered_users = cursor.fetchall()

            if user not in [i[0] for i in registered_users]:
                print(registered_users)
                messagebox.showwarning("Unregistered!",
                                       "The Reg.No is Not Registered within our systems.\nKindly Contact the administrator first for Registration.")
                self.LogClear()
            else:
                # Fetching the password for the given username
                cursor.execute(f"SELECT Password FROM StudentLogin WHERE Username = '{user}'")
                fetched_password = cursor.fetchone()

                if fetched_password:
                    messagebox.showerror("Invalid User", "Registration Number already exists. Please choose a different one."
                                                         "\nContact The Administrator for password Reset If you Forgot the Password")
                    self.LogClear()
                    self.newmaster.deiconify()
                else:
                    cursor.execute(f"SELECT Username FROM StudentLogin WHERE Password = '{passw}'")
                    fetched_username = cursor.fetchone()

                    if fetched_username:
                        messagebox.showerror("Password Error! ",
                                             "Password already used. Please choose a different one.")
                        self.LogClear()
                        self.newmaster.deiconify()
                    elif len(passw) < 4:
                        messagebox.showerror("Password Error! ", "Password must be Greater than 4 digits or letters .")
                        self.LogClear()
                        self.newmaster.deiconify()

                    elif len(passw) > 6:
                        messagebox.showerror("Password Error! ",
                                             "Password must not be Greater than 6 digits or letters .")
                        self.LogClear()
                        self.newmaster.deiconify()

                    else:
                        cursor.execute(f"INSERT INTO StudentLogin (Username, Password) VALUES ('{user}', '{passw}')")
                        cursor.commit()
                        cursor.close()
                        messagebox.showinfo("Registration Success", "Password has been  Set Successfully !")
                        self.LogClear()
                        self.newmaster.withdraw()
                        self.root.deiconify()

        else:
            messagebox.showerror("Empty Fields Error", "Please enter both  username and  password.")
            self.newmaster.deiconify()
            self.LogClear()

    def LogClear(self):
        self.Passwordentry.delete(0, 'end')
        self.UsernameEntry.delete(0, 'end')
        self.UsernameEntry.focus()
    def Close(self):
        self.master.withdraw()
        self.root.deiconify()
        # exit()


    def launch_student_window(self):
        stud = StudentsDashboardPage()
        stud.StudentDashBoard()



