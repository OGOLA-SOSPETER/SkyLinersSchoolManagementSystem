from tkinter import *
import tkinter as tk
from tkinter import messagebox

from App.AdminDashboard import AdminDashboardPage
from App.StudentsDashboard import StudentsDashboardPage
from App.TeachersDashBoard import TeacherDashboardPage


class WelcomePage:
    def __init__(self):
        self.welcomemaster = tk.Tk()
        self.welcomemaster.geometry("650x550+200+150")
        self.welcomemaster.title("SKYLINERS HIGH SCHOOL MANAGEMENT SYSTEM.")
    def Page(self):
        master_frame = tk.Frame(self.welcomemaster)
        self.welcomemaster.geometry("450x200+200+150")
        self.welcomemaster.resizable(width=True, height=True)
        master_frame.pack()
        lb1 = Label(master_frame, text="WELCOME TO SKYLINERS HIGH SCHOOL  SCHOOL MANAGEMENT SYSTEM.",font='Arial, 8')
        lb1.grid(column=0,row=0)

        # Log_Image_Frame = Frame(master_frame,bd = 3, bg = "black",width=200,height=200,relief=GROOVE)
        # Log_Image_Frame.grid(row=0,column=0)
        # img = Image.open("Images/Log1.png",mode="r",formats=["PNG"])
        # photo = ImageTk.PhotoImage(img)
        # imgLabel = Label(Log_Image_Frame,image=photo)
        # imgLabel.grid(row=1,column=0)


        self.student_var = BooleanVar()
        self.teacher_var = BooleanVar()
        self.admin_var = BooleanVar()
        User_option_Frame = tk.Frame(master_frame)
        User_option_Frame.grid(row=1, column=0)

        lb2 = Label(User_option_Frame, text="Select your Login option.")
        lb2.grid(row=1,column=1,padx=50)

        student_checkbox = Checkbutton(User_option_Frame, text="Student", variable=self.student_var)
        student_checkbox.grid(row=2,column=0)
        teacher_checkbox = Checkbutton(User_option_Frame, text="Teacher", variable=self.teacher_var)
        teacher_checkbox.grid(row=2,column=1)
        admin_checkbox = Checkbutton(User_option_Frame, text="Administrator", variable=self.admin_var)
        admin_checkbox.grid(row=2, column=3)

        # Login Button
        LoginButton = Button(User_option_Frame, text="Login", bg="blue", fg="white",width=20, command=self.selection)
        LoginButton.grid(row = 3,column=1,pady=10)

        # Exit Button
        ExitButton = Button(User_option_Frame, text="Exit App", bg="blue", fg="white", width=20, command=self.ExitApp)
        ExitButton.grid(row=4, column=1,pady=10)



        self.welcomemaster.mainloop()
    def ExitApp(self):
        AdminDashboardPage.Exit(AdminDashboardPage())
    def selection(self):

        if self.student_var.get() and self.teacher_var.get() and self.admin_var.get() or self.student_var.get() and self.admin_var.get() or self.student_var.get() and self.teacher_var.get() or self.teacher_var.get() and self.admin_var.get():
            messagebox.showerror("Multiple Selection!","Choose Only One Option!!!")
        elif self.student_var.get():
            self.welcomemaster.withdraw()
            StudentsDashboardPage.launch_student_window(StudentsDashboardPage().StudentDashBoard())
        elif self.admin_var.get():
            self.welcomemaster.withdraw()
            AdminDashboardPage.launch_admin_window(AdminDashboardPage())
            self.welcomemaster.withdraw()
        elif self.teacher_var.get():
            self.welcomemaster.withdraw()
            TeacherDashboardPage.launch_teacher_window(TeacherDashboardPage().TeacherLogin())
            messagebox.showerror("Coming soon!","Teacher Coming soon.!")
        else:
            messagebox.showerror("Error", "Please select your Login Option")

        self.welcomemaster.mainloop()




welcome = WelcomePage()
welcome.Page()
