from tkinter import Label
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox

import pyodbc


class ViewStudentDetails:
    def __init__(self):
        self.viewmaster = tk.Tk()
        self.viewmaster.title("SkyLiners High School Student Details")

    def ViewStudent(self):
        self.viewmaster.geometry("900x600+200+100")
        self.viewmaster.config(padx=50, pady=5)
        self.viewmaster.resizable(True, True)

        lbl = Label(self.viewmaster, text="Enter the Registration Number to View Student Details")
        lbl.grid(row=0, column=0)
        Reg_label = tk.Label(self.viewmaster, text="Student Details.")
        Reg_label.grid(row=1, column=0)
        lbl1frame = Frame(self.viewmaster, borderwidth=2, relief=GROOVE, width=500, height=350, padx=50, pady=10)
        lbl1frame.grid(row=2, column=0, sticky=W + E)

        # # Registration Number Entry and Label
        # Reg_label = tk.Label(lbl1frame, text="Reg_Number")
        # Reg_label.grid(row=1, column=0)
        # self.Reg_Entry = tk.Entry(lbl1frame, width=20)
        # self.Reg_Entry.grid(row=1, column=1)
        # Establish a connection to the StudentData Access database
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
        # Create a cursor object
        cursor = conn.cursor()

        cursor.execute("SELECT REG_NO FROM StudentData")
        rows = cursor.fetchall()
        fetched_reg = [row[0] for row in rows]
        # Registration Number Entry and Label
        Reg_label = tk.Label(lbl1frame, text="Reg_Number")
        Reg_label.grid(row=1, column=0)
        self.Reg_Entry = Combobox(lbl1frame, width=20,values=[f'{row}' for row in fetched_reg])
        self.Reg_Entry.grid(row=1, column=1)

        # Name Entry and Label
        Name_label = tk.Label(lbl1frame, text="Name")
        Name_label.grid(row=2, column=0)
        self.Name_Entry = tk.Entry(lbl1frame, width=20)
        self.Name_Entry.grid(row=2, column=1)
        self.Name_Entry.bind('<KeyRelease>',lambda event: self.ViewDetails())


        # Fees Entry and Label
        Fee_Due_label = tk.Label(lbl1frame, text="Fees Due")
        Fee_Due_label.grid(row=3, column=0)
        self.Fee_Due_Entry = tk.Entry(lbl1frame, width=20)
        self.Fee_Due_Entry.grid(row=3, column=1)
        self.Fee_Due_Entry.bind('<KeyRelease>',lambda event: self.ViewDetails())

        # Fees Entry and Label
        Fee_Paid_label = tk.Label(lbl1frame, text="Fees Paid")
        Fee_Paid_label.grid(row=4, column=0)
        self.Fee_Paid_Entry = tk.Entry(lbl1frame, width=20)
        self.Fee_Paid_Entry.grid(row=4, column=1)
        self.Fee_Paid_Entry.bind('<KeyRelease>',lambda event: self.ViewDetails())


        # Fee Balance Entry and Label
        Fee_Balance_label = tk.Label(lbl1frame, text="Fee Balance", state="disabled")
        Fee_Balance_label.grid(row=1, column=3, pady=2)
        self.Fee_Balance_Entry = tk.Entry(lbl1frame, width=20, state="disabled")
        self.Fee_Balance_Entry.grid(row=1, column=4)
        self.Fee_Balance_Entry.bind('<KeyRelease>',lambda event: self.ViewDetails())

        # Stream Entry and Label
        Stream_label = tk.Label(lbl1frame, text="Stream")
        Stream_label.grid(row=2, column=3, padx=10, pady=2)
        self.Stream_Entry = Combobox(lbl1frame, width=20, values=['North', ' South', ' East', 'West'])
        self.Stream_Entry.grid(row=2, column=4)
        self.Stream_Entry.bind('<KeyRelease>',lambda event: self.ViewDetails())

        # Form Entry and Label
        Form_label = tk.Label(lbl1frame, text="Form")
        Form_label.grid(row=3, column=3, padx=10, pady=2)
        self.Form_Entry = Combobox(lbl1frame, width=20, values=['1', ' 2', ' 3', ' 4'])
        self.Form_Entry.grid(row=3, column=4)
        self.Form_Entry.bind('<KeyRelease>',lambda event: self.ViewDetails())

        # County Label
        stdCounty_label = tk.Label(lbl1frame, text="County")
        stdCounty_label.grid(row=4, column=3, padx=20, pady=2)
        self.stdCountyEntry = Combobox(lbl1frame, width=8,
                                       values=['HomaBay', 'Mombasa', 'Malindi', 'Kisumu', 'Kisii', 'Nyamira', 'Migori',
                                               'Kitale', 'Nairobi', 'Turkana', 'Eldoret', 'Lamu', 'Kilifi'])
        self.stdCountyEntry.grid(row=4, column=4)
        self.stdCountyEntry.set("Select County")
        self.stdCountyEntry.bind('<KeyRelease>',lambda event: self.ViewDetails())

        prntlbl = Label(self.viewmaster, text="Parents' Details.")
        prntlbl.grid(row=3, column=0)

        parntframe = Frame(self.viewmaster, borderwidth=2, relief=GROOVE, width=500, height=350, padx=50, pady=10)
        parntframe.grid(row=4, column=0)

        # Father's Details.
        # ID Number Entry and Label
        fthLabel = Label(parntframe, text="Father's Details", font="Montserrat 12 ", justify=CENTER)
        fthLabel.grid(row=0, column=0)
        Fatherid_label = tk.Label(parntframe, text="ID. NO.")
        Fatherid_label.grid(row=1, column=0)
        self.Father_id_Entry = tk.Entry(parntframe, width=30)
        self.Father_id_Entry.grid(row=1, column=1)
        self.Father_id_Entry.bind('<KeyRelease>',lambda event: self.ViewDetails())

        # Name Entry and Label
        FatherName_label = tk.Label(parntframe, text="Name: ")
        FatherName_label.grid(row=2, column=0)
        self.FatherName_Entry = tk.Entry(parntframe, width=30)
        self.FatherName_Entry.grid(row=2, column=1)
        self.FatherName_Entry.bind('<KeyRelease>',lambda event: self.ViewDetails())

        # Stream Entry and Label
        FatherContact_label = tk.Label(parntframe, text="Contact: ")
        FatherContact_label.grid(row=3, column=0)
        self.FatherContact_Entry = tk.Entry(parntframe, width=30)
        self.FatherContact_Entry.grid(row=3, column=1)
        self.FatherContact_Entry.bind('<KeyRelease>',lambda event: self.ViewDetails())

        # Form Entry and Label
        FatherEmail_label = tk.Label(parntframe, text="Email: ")
        FatherEmail_label.grid(row=4, column=0)
        self.FatherEmail_Entry = tk.Entry(parntframe, width=30)
        self.FatherEmail_Entry.grid(row=4, column=1)
        self.FatherEmail_Entry.bind('<KeyRelease>',lambda event: self.ViewDetails())

        # Mother's Details.
        # ID Number Entry and Label
        mthLabel = Label(parntframe, text="Mother's Details", font="Montserrat 12 ", justify=CENTER)
        mthLabel.grid(row=5, column=0)
        mother_id_label = tk.Label(parntframe, text="ID. NO.")
        mother_id_label.grid(row=6, column=0)
        self.Mother_id_Entry = tk.Entry(parntframe, width=30)
        self.Mother_id_Entry.grid(row=6, column=1)
        self.Mother_id_Entry.bind('<KeyRelease>',lambda event: self.ViewDetails())

        # Name Entry and Label
        MotherName_label = tk.Label(parntframe, text="Name: ")
        MotherName_label.grid(row=7, column=0)
        self.MotherName_Entry = tk.Entry(parntframe, width=30)
        self.MotherName_Entry.grid(row=7, column=1)
        self.MotherName_Entry.bind('<KeyRelease>',lambda event: self.ViewDetails())

        # Stream Entry and Label
        MotherContact_label = tk.Label(parntframe, text="Contact: ")
        MotherContact_label.grid(row=8, column=0)
        self.MotherContact_Entry = tk.Entry(parntframe, width=30)
        self.MotherContact_Entry.grid(row=8, column=1)
        self.MotherContact_Entry.bind('<KeyRelease>',lambda event: self.ViewDetails())

        # Form Entry and Label
        MotherEmail_label = tk.Label(parntframe, text="Email: ")
        MotherEmail_label.grid(row=9, column=0)
        self.MotherEmail_Entry = tk.Entry(parntframe, width=30)
        self.MotherEmail_Entry.grid(row=9, column=1)
        self.MotherEmail_Entry.bind('<KeyRelease>',lambda event: self.ViewDetails())

        ViewButton = Button(self.viewmaster, text="View Details", command=self.ViewDetails, width=20)
        ViewButton.grid(row=2, column=2)

        RefreshButton = Button(self.viewmaster, text="Refresh", command=self.RefreshDetails, width=20)
        RefreshButton.grid(row=3, column=2)

        EditButton = Button(self.viewmaster, text="Edit Details", command=self.EditDetails, width=20)
        EditButton.grid(row=4, column=2)

        ExitButton = Button(self.viewmaster, text="Exit", command=self.ExitView, width=20)
        ExitButton.grid(row=5, column=2)

        self.viewmaster.mainloop()
    def RefreshDetails(self):
        self.Reg_Entry.config(state='normal')
        self.Name_Entry.config(state="disabled")
        self.Fee_Due_Entry.config(state="disabled")
        self.Fee_Paid_Entry.config(state="disabled")
        self.Stream_Entry.config(state="disabled")
        self.Form_Entry.config(state="disabled")
        self.Father_id_Entry.config(state="disabled")
        self.FatherName_Entry.config(state="disabled")
        self.FatherContact_Entry.config(state="disabled")
        self.FatherEmail_Entry.config(state="disabled")
        self.Mother_id_Entry.config(state="disabled")
        self.MotherName_Entry.config(state="disabled")
        self.MotherContact_Entry.config(state="disabled")
        self.MotherEmail_Entry.config(state="disabled")
        self.stdCountyEntry.config(state="disabled")
    def ViewDetails(self):
        self.Reg_Entry.config(state='normal')
        self.Name_Entry.config(state="normal")
        self.Fee_Due_Entry.config(state="normal")
        self.Fee_Paid_Entry.config(state="normal")
        self.Stream_Entry.config(state="normal")
        self.Form_Entry.config(state="normal")
        self.Father_id_Entry.config(state="normal")
        self.FatherName_Entry.config(state="normal")
        self.FatherContact_Entry.config(state="normal")
        self.FatherEmail_Entry.config(state="normal")
        self.Mother_id_Entry.config(state="normal")
        self.MotherName_Entry.config(state="normal")
        self.MotherContact_Entry.config(state="normal")
        self.MotherEmail_Entry.config(state="normal")
        self.stdCountyEntry.config(state="normal")
        reg = self.Reg_Entry.get()
        if reg != "":
            # Establish a connection to the StudentData Access database
            conn = pyodbc.connect(
                r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
            # Create a cursor object
            cursor = conn.cursor()

            cursor.execute("SELECT REG_NO FROM StudentData")
            self.fetched_reg = cursor.fetchall()

            cursor.execute(
                f"SELECT REG_NO,  NAME, STREAM, FORM, FEES_DUE, FEES_PAID, FEES_BALANCE, FATHER_ID, FATHER_NAME, FATHER_CONTACT, FATHER_EMAIL, MOTHER_ID, MOTHER_NAME, MOTHER_CONTACT, MOTHER_EMAIL, COUNTY FROM StudentData WHERE REG_NO  = '{reg}'")
            fetched_records = cursor.fetchone()

            if fetched_records:
                self.Reg_Entry.config(state='normal')
                self.Reg_Entry.delete(0, END)
                self.Reg_Entry.insert(0, str(fetched_records[0]))

                self.Name_Entry.delete(0, END)
                self.Name_Entry.insert(0, str(fetched_records[1]))

                self.Stream_Entry.delete(0, END)
                self.Stream_Entry.insert(0, str(fetched_records[2]))

                self.Form_Entry.delete(0, END)
                self.Form_Entry.insert(0, str(fetched_records[3]))

                self.Fee_Due_Entry.delete(0, END)
                self.Fee_Due_Entry.insert(0, str(fetched_records[4]))

                self.Fee_Paid_Entry.delete(0, END)
                self.Fee_Paid_Entry.insert(0, str(fetched_records[5]))

                self.Fee_Balance_Entry.delete(0, END)
                self.Fee_Balance_Entry.insert(0, str(fetched_records[6]))

                self.Father_id_Entry.delete(0, END)
                self.Father_id_Entry.insert(0, str(fetched_records[7]))

                self.FatherName_Entry.delete(0, END)
                self.FatherName_Entry.insert(0, str(fetched_records[8]))

                self.FatherContact_Entry.delete(0, END)
                self.FatherContact_Entry.insert(0, str(fetched_records[9]))

                self.FatherEmail_Entry.delete(0, END)
                self.FatherEmail_Entry.insert(0, str(fetched_records[10]))

                self.Mother_id_Entry.delete(0, END)
                self.Mother_id_Entry.insert(0, str(fetched_records[11]))

                self.MotherName_Entry.delete(0, END)
                self.MotherName_Entry.insert(0, str(fetched_records[12]))

                self.MotherContact_Entry.delete(0, END)
                self.MotherContact_Entry.insert(0, str(fetched_records[13]))

                self.MotherEmail_Entry.delete(0, END)
                self.MotherEmail_Entry.insert(0, str(fetched_records[14]))

                self.stdCountyEntry.delete(0, END)
                self.stdCountyEntry.insert(0, str(fetched_records[15]))

                self.Reg_Entry.config(state='disabled')
                self.Name_Entry.config(state="disabled")
                self.Fee_Due_Entry.config(state="disabled")
                self.Fee_Paid_Entry.config(state="disabled")
                self.Stream_Entry.config(state="disabled")
                self.Form_Entry.config(state="disabled")
                self.Father_id_Entry.config(state="disabled")
                self.FatherName_Entry.config(state="disabled")
                self.FatherContact_Entry.config(state="disabled")
                self.FatherEmail_Entry.config(state="disabled")
                self.Mother_id_Entry.config(state="disabled")
                self.MotherName_Entry.config(state="disabled")
                self.MotherContact_Entry.config(state="disabled")
                self.MotherEmail_Entry.config(state="disabled")
                self.stdCountyEntry.config(state="disabled")
            else:
                messagebox.showerror("Error", f"No record found for registration number {reg}")

            # close database connection
            conn.close()
        else:
            messagebox.showwarning('Null Entry.', "Enter the Registration Number.")

    def EditDetails(self):
        pass

    def ExitView(self):
        self.viewmaster.withdraw()




