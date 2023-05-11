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
        self.viewmaster.geometry("1000x600+200+100")
        self.viewmaster.config(padx=50, pady=5)
        self.viewmaster.resizable(True, True)
        main_frame = Frame(self.viewmaster)
        main_frame.grid(row=0, column=0)

        entry_frame = Frame(main_frame, borderwidth=2, relief=GROOVE, width=500, height=350, padx=50, pady=10)
        entry_frame.grid(row=2, column=0, sticky=W + E,pady=10)



        buttons_frame = Frame(main_frame, borderwidth=2, relief=GROOVE, width=500, height=350, padx=50, pady=10)
        buttons_frame.grid(row=2, column=1, sticky=W + E,padx= 5,pady=5,ipadx=10,ipady=10)

        lbl = Label(entry_frame, text="Enter the Registration Number to View Student Details")
        lbl.grid(row=0, column=0)
        S_label = tk.Label(entry_frame, text="Student Details.")
        S_label.grid(row=1, column=0)
        lbl1frame = Frame(entry_frame, borderwidth=2, relief=GROOVE, width=500, height=350, padx=50, pady=10)
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
        self.Reg_Entry = Combobox(lbl1frame, width=20, values=[f'{row}' for row in fetched_reg])
        self.Reg_Entry.grid(row=1, column=1)

        # Name Entry and Label
        Name_label = tk.Label(lbl1frame, text="Name")
        Name_label.grid(row=2, column=0)
        self.Name_Entry = tk.Entry(lbl1frame, width=20)
        self.Name_Entry.grid(row=2, column=1)
        # self.Name_Entry.bind('<KeyRelease>', lambda event: self.ViewDetails())

        # Fees Entry and Label
        Fee_Due_label = tk.Label(lbl1frame, text="Fees Due")
        Fee_Due_label.grid(row=3, column=0)
        self.Fee_Due_Entry = tk.Entry(lbl1frame, width=20)
        self.Fee_Due_Entry.grid(row=3, column=1)
        # self.Fee_Due_Entry.bind('<KeyRelease>', lambda event: self.ViewDetails())
        self.Fee_Due_Entry.bind('<KeyRelease>', lambda event:self.calculate_fee_balance())

        # Fees Entry and Label
        Fee_Paid_label = tk.Label(lbl1frame, text="Fees Paid")
        Fee_Paid_label.grid(row=4, column=0)
        self.Fee_Paid_Entry = tk.Entry(lbl1frame, width=20)
        self.Fee_Paid_Entry.grid(row=4, column=1)
        # self.Fee_Paid_Entry.bind('<KeyRelease>', lambda event: self.ViewDetails())
        self.Fee_Paid_Entry.bind('<KeyRelease>', lambda event:self.calculate_fee_balance())

        # Fee Balance Entry and Label
        Fee_Balance_label = tk.Label(lbl1frame, text="Fee Balance", state="disabled")
        Fee_Balance_label.grid(row=1, column=3, pady=2)
        self.Fee_Balance_Entry = tk.Entry(lbl1frame, width=20, state="disabled")
        self.Fee_Balance_Entry.grid(row=1, column=4)
        # self.Fee_Balance_Entry.bind('<KeyRelease>', lambda event: self.ViewDetails())
        self.Fee_Balance_Entry.bind('<KeyRelease>', lambda event:self.calculate_fee_balance())

        # Stream Entry and Label
        Stream_label = tk.Label(lbl1frame, text="Stream")
        Stream_label.grid(row=2, column=3, padx=10, pady=2)
        self.Stream_Entry = Combobox(lbl1frame, width=20, values=['North', ' South', ' East', 'West'])
        self.Stream_Entry.grid(row=2, column=4)
        # self.Stream_Entry.bind('<KeyRelease>', lambda event: self.ViewDetails())

        # Form Entry and Label
        Form_label = tk.Label(lbl1frame, text="Form")
        Form_label.grid(row=3, column=3, padx=10, pady=2)
        self.Form_Entry = Combobox(lbl1frame, width=20, values=['1', ' 2', ' 3', ' 4'])
        self.Form_Entry.grid(row=3, column=4)
        # self.Form_Entry.bind('<KeyRelease>', lambda event: self.ViewDetails())

        # County Label
        stdCounty_label = tk.Label(lbl1frame, text="County")
        stdCounty_label.grid(row=4, column=3, padx=20, pady=2)
        self.stdCountyEntry = Combobox(lbl1frame, width=8,
                                       values=['HomaBay', 'Mombasa', 'Malindi', 'Kisumu', 'Kisii', 'Nyamira', 'Migori',
                                               'Kitale', 'Nairobi', 'Turkana', 'Eldoret', 'Lamu', 'Kilifi'])
        self.stdCountyEntry.grid(row=4, column=4)
        self.stdCountyEntry.set("Select County")
        # self.stdCountyEntry.bind('<KeyRelease>', lambda event: self.ViewDetails())

        prntlbl = Label(entry_frame, text="Parents' Details.")
        prntlbl.grid(row=4, column=0,padx=10)

        parntframe = Frame(entry_frame, borderwidth=2, relief=GROOVE, width=500, height=350, padx=50, pady=10)
        parntframe.grid(row=5, column=0,padx=10)

        # Father's Details.
        # ID Number Entry and Label
        fthLabel = Label(parntframe, text="Father's Details", font="Montserrat 12 ", justify=CENTER)
        fthLabel.grid(row=0, column=0)
        Fatherid_label = tk.Label(parntframe, text="ID. NO.")
        Fatherid_label.grid(row=1, column=0)
        self.Father_id_Entry = tk.Entry(parntframe, width=30)
        self.Father_id_Entry.grid(row=1, column=1)
        # self.Father_id_Entry.bind('<KeyRelease>', lambda event: self.ViewDetails())

        # Name Entry and Label
        FatherName_label = tk.Label(parntframe, text="Name: ")
        FatherName_label.grid(row=2, column=0)
        self.FatherName_Entry = tk.Entry(parntframe, width=30)
        self.FatherName_Entry.grid(row=2, column=1)
        # self.FatherName_Entry.bind('<KeyRelease>', lambda event: self.ViewDetails())

        # Stream Entry and Label
        FatherContact_label = tk.Label(parntframe, text="Contact: ")
        FatherContact_label.grid(row=3, column=0)
        self.FatherContact_Entry = tk.Entry(parntframe, width=30)
        self.FatherContact_Entry.grid(row=3, column=1)
        # self.FatherContact_Entry.bind('<KeyRelease>', lambda event: self.ViewDetails())

        # Form Entry and Label
        FatherEmail_label = tk.Label(parntframe, text="Email: ")
        FatherEmail_label.grid(row=4, column=0)
        self.FatherEmail_Entry = tk.Entry(parntframe, width=30)
        self.FatherEmail_Entry.grid(row=4, column=1)
        # self.FatherEmail_Entry.bind('<KeyRelease>', lambda event: self.ViewDetails())

        # Mother's Details.
        # ID Number Entry and Label
        mthLabel = Label(parntframe, text="Mother's Details", font="Montserrat 12 ", justify=CENTER)
        mthLabel.grid(row=5, column=0)
        mother_id_label = tk.Label(parntframe, text="ID. NO.")
        mother_id_label.grid(row=6, column=0)
        self.Mother_id_Entry = tk.Entry(parntframe, width=30)
        self.Mother_id_Entry.grid(row=6, column=1)
        # self.Mother_id_Entry.bind('<KeyRelease>', lambda event: self.ViewDetails())

        # Name Entry and Label
        MotherName_label = tk.Label(parntframe, text="Name: ")
        MotherName_label.grid(row=7, column=0)
        self.MotherName_Entry = tk.Entry(parntframe, width=30)
        self.MotherName_Entry.grid(row=7, column=1)
        # self.MotherName_Entry.bind('<KeyRelease>', lambda event: self.ViewDetails())

        # Stream Entry and Label
        MotherContact_label = tk.Label(parntframe, text="Contact: ")
        MotherContact_label.grid(row=8, column=0)
        self.MotherContact_Entry = tk.Entry(parntframe, width=30)
        self.MotherContact_Entry.grid(row=8, column=1)
        # self.MotherContact_Entry.bind('<KeyRelease>', lambda event: self.ViewDetails())

        # Form Entry and Label
        MotherEmail_label = tk.Label(parntframe, text="Email: ")
        MotherEmail_label.grid(row=9, column=0)
        self.MotherEmail_Entry = tk.Entry(parntframe, width=30)
        self.MotherEmail_Entry.grid(row=9, column=1)
        # self.MotherEmail_Entry.bind('<KeyRelease>', lambda event: self.ViewDetails())

        ViewButton = Button(buttons_frame, text="View Details", bg='blue', fg='white', command=self.ViewDetails,
                            width=20)
        ViewButton.grid(row=1, column=0,columnspan=2,pady=7)

        RefreshButton = Button(buttons_frame, text="Refresh", bg='green', fg='white', command=self.RefreshDetails,
                               width=20)
        RefreshButton.grid(row=2, column=0,columnspan=2,pady=7)

        EditButton = Button(buttons_frame, text="Edit Details", bg='green', fg='white', command=self.EditDetails,
                            width=20)
        EditButton.grid(row=3, column=0,columnspan=2,pady=7)

        CommitButton = Button(buttons_frame, text="Commit Changes", bg='blue', fg='white', command=self.CommitUpdate,
                              width=20)
        CommitButton.grid(row=4, column=0,columnspan=2,pady=7)

        ExitButton = Button(buttons_frame, text="Exit", bg='red', fg='white', command=self.ExitView, width=20)
        ExitButton.grid(row=5, column=0,columnspan=2,pady=7)

        self.viewmaster.mainloop()
    def calculate_fee_balance(self):
        fee_due = float(self.Fee_Due_Entry.get())
        fee_paid = float(self.Fee_Paid_Entry.get())
        self.fee_balance = fee_due - fee_paid
        self.Fee_Balance_Entry.config(state="normal")
        self.Fee_Balance_Entry.delete(0, tk.END)
        self.Fee_Balance_Entry.insert(0, str(self.fee_balance))
        self.Fee_Balance_Entry.config(state='disabled')
        fee_balance = self.fee_balance
    def RefreshDetails(self):
        self.EnableFields()
        self.DeleteEntries()
        self.DisableFields()
        self.RefreshFee()
        self.Reg_Entry.config(state='normal')
    def RefreshFee(self):
        self.Fee_Balance_Entry.config(state='normal')
        self.Fee_Balance_Entry.delete(0,END)
        self.Fee_Balance_Entry.config(state='disabled')
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

                self.Fee_Balance_Entry.config(state='normal')
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

                self.DisableFields()
                conn.commit()
                conn.close()
                # cursor.close()

            else:
                messagebox.showerror("Error", f"No record found for registration number {reg}")

            # close database connection
            # conn.close()
        else:
            messagebox.showwarning('Null Entry.', "Enter the Registration Number.")

    def DeleteEntries(self):
        self.Reg_Entry.config(state='normal')
        self.Reg_Entry.delete(0, END)
        self.Name_Entry.delete(0, END)
        self.Stream_Entry.delete(0, END)
        self.Form_Entry.delete(0, END)
        self.Fee_Due_Entry.delete(0, END)
        self.Fee_Paid_Entry.delete(0, END)
        self.Fee_Balance_Entry.config(state='normal')
        self.Fee_Balance_Entry.delete(0, END)
        self.Fee_Balance_Entry.config(state='disabled')
        self.Father_id_Entry.delete(0, END)
        self.FatherName_Entry.delete(0, END)
        self.FatherContact_Entry.delete(0, END)

        self.FatherEmail_Entry.delete(0, END)
        self.Mother_id_Entry.delete(0, END)
        self.MotherName_Entry.delete(0, END)
        self.MotherContact_Entry.delete(0, END)
        self.MotherEmail_Entry.delete(0, END)
        self.stdCountyEntry.delete(0, END)

    def DisableFields(self):
        self.Reg_Entry.config(state='disabled')
        self.Name_Entry.config(state="disabled")
        self.Fee_Due_Entry.config(state="disabled")
        self.Fee_Paid_Entry.config(state="disabled")
        self.Fee_Balance_Entry.config(state='disabled')
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

    def EnableFields(self):
        print("Enabling fields...")
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
    def EditDetails(self):
        self.EnableFields()
    def CommitUpdate(self):
        self.EditStudentRecord()

    def EditStudentRecord(self):

        reg = self.Reg_Entry.get()
        name = self.Name_Entry.get()
        feeD = self.Fee_Due_Entry.get()
        feeP = self.Fee_Paid_Entry.get()
        fees_balance = self.Fee_Balance_Entry.get()
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
        if reg == "":
            messagebox.showwarning('Null Registration', 'Registration cannot be Empty!!')
        # Validate the input fields
        elif not all((name, feeD, feeP, stream, form, fathId, fathNm, fathCnt, fathEm, mothId, mothNm, mothCnt,
                      mothEm, county)):
            results = messagebox.askyesno('Delete Record', f'Do you want to delete the records for {reg}?')
            if results:
                conn = pyodbc.connect(
                    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
                # Create a cursor object
                cursor = conn.cursor()
                # Execute the delete query
                cursor.execute(f"DELETE FROM StudentData WHERE REG_NO = '{reg}'")
                conn.commit()

                messagebox.showerror("Deletion Success", "Records deleted successfully.")
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
            result = messagebox.askyesno("Update Records.", f"Do you want to update the records for {reg} ?")
            if result:
                # cursor.execute(
                #     f"INSERT INTO StudentData (REG_NO, NAME, STREAM, FORM, FEES_DUE, FEES_PAID, FEES_BALANCE, FATHER_ID, FATHER_NAME, FATHER_CONTACT, FATHER_EMAIL, MOTHER_ID, MOTHER_NAME, MOTHER_CONTACT, MOTHER_EMAIL, COUNTY)  VALUES ('{reg}', '{name}', '{stream}', '{form}', '{feeD}', '{feeP}', '{self.fee_balance}', '{fathId}', '{fathNm}', '{fathCnt}', '{fathEm}', '{mothId}', '{mothNm}', '{mothCnt}', '{mothEm}', '{county}')")
                #
                # # Commit the changes
                # conn.commit()
                # conn.close()
                # Update the record
                cursor.execute(
                    f"UPDATE StudentData SET NAME='{name}', STREAM='{stream}', FORM='{form}', FEES_DUE='{feeD}', FEES_PAID='{feeP}', FEES_BALANCE='{fees_balance}', FATHER_ID='{fathId}', FATHER_NAME='{fathNm}', FATHER_CONTACT='{fathCnt}', FATHER_EMAIL='{fathEm}', MOTHER_ID='{mothId}', MOTHER_NAME='{mothNm}', MOTHER_CONTACT='{mothCnt}', MOTHER_EMAIL='{mothEm}', COUNTY='{county}' WHERE REG_NO='{reg}'"
                )
                # Commit the changes
                conn.commit()
                conn.close()
                self.DeleteEntries()
                messagebox.showinfo("Success.", "Record Updated Successfully!")
            return
        # Insert the new record
        self.master.deiconify()

    def ExitView(self):
        self.viewmaster.withdraw()
