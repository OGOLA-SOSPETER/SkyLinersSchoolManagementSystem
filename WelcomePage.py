from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

# from StudentsDashboard import stud
# from AdminDashboard import admin
# from tkinter import ttk

from AdminDashboard import admin
from StudentsDashboard import stud


class WelcomePage:
    def __init__(self):
        self.radio = IntVar()
        self.photo = None


    def Page(self):
        master = tk.Tk()
        master.geometry("650x550+200+150")
        master.title("SKYLINERS HIGH SCHOOL MANAGEMENT SYSTEM.")


        master_frame = tk.Frame(master)
        master.geometry("450x350+200+150")
        master.resizable(width=True,height=True)
        master_frame.pack()
        lb1 = Label(master_frame, text="Welcome to our school management system.")
        lb1.grid(column=0,row=0)

        # Log_Image_Frame = Frame(master_frame,bd = 3, bg = "black",width=200,height=200,relief=GROOVE)
        # Log_Image_Frame.grid(row=0,column=0)
        # img = Image.open("Images/Log1.png",mode="r",formats=["PNG"])
        # photo = ImageTk.PhotoImage(img)
        # imgLabel = Label(Log_Image_Frame,image=photo)
        # imgLabel.grid(row=1,column=0)



        User_option_Frame = tk.Frame(master_frame)
        User_option_Frame.grid(row=1, column=0)

        lb2 = Label(User_option_Frame, text="Select your Current Profession.")
        lb2.grid(row=1,column=0)

        rbtn1 = Radiobutton(User_option_Frame, text="Student", variable=self.radio, value=1)
        rbtn1.grid(row=2,column=0)
        rbtn2 = Radiobutton(User_option_Frame, text="Teacher", variable=self.radio, value=2)
        rbtn2.grid(row=3,column=0)

        # Login Button
        LoginButton = Button(User_option_Frame, text="Login", bg="blue", fg="white", command=self.selection)
        LoginButton.grid(row = 4,column=0,padx=5)



        master.mainloop()
        return self.radio

    def selection(self):
        value = self.radio.get()
        if value == 1:
            stud.StudentDashBoard()
        elif value == 2:
            admin.AdminDashboard()
        else:
            messagebox.showerror("Null Selection!","Null Selection!")
            # Do something else, such as displaying an error message
            pass
    # def Status(self):
    #     if self.v.get() == 1:
    #         student_dashboard = stud.StudentDashboard()
    #         student_dashboard.StudentDashBoard()
    #     elif self.v.get() == 2:
    #         admin_dashboard = admin.AdminDashboard()
    #         admin_dashboard.AdminDashBoard()


welcome = WelcomePage()
welcome.Page()
