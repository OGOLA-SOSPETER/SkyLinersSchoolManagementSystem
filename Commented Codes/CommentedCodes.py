# .............Admin Dashboard...............
#
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


# ..............Student Dashboard................

# def StudentDashboard(self):
#     self.root = tk.Tk()
#     self.root.title("Student Dashboard")
#     self.root.geometry("800x400")
#     self.root.resizable(False, False)
#     self.root.config(bg="#ECECEC")
#
#     # Side Frame
#     side_frame = tk.Frame(self.root, bg="#06283D", width=200)
#     side_frame.pack(fill="y", side="left")
#
#     # # Logo Image
#     # logo_img = tk.PhotoImage(file="E:\Desktop\Design\designs\mew.png",width=100,height=100)
#     # logo_label = tk.Label(side_frame, image=logo_img, bg="#06283D")
#     # logo_label.pack(pady=20)
#
#     # Main Frame
#     main_frame = tk.Frame(self.root, bg="#ECECEC", padx=40, pady=20)
#     main_frame.pack(fill="both", expand=True)
#
#     # Title Label
#     title_label = tk.Label(main_frame, text="Student Login", font=("Montserrat", 20), bg="#ECECEC", fg="#06283D")
#     title_label.grid(row=0, column=0, columnspan=2, pady=20)
#
#     # Username Label and Entry
#     username_label = tk.Label(main_frame, text="Username", font=("Montserrat", 12), bg="#ECECEC", fg="#06283D")
#     username_label.grid(row=1, column=0, pady=10)
#     self.UsernameEntry = tk.Entry(main_frame, width=30, font=("Montserrat", 12))
#     self.UsernameEntry.grid(row=1, column=1, pady=10)
#
#     # Password Label and Entry
#     password_label = tk.Label(main_frame, text="Password", font=("Montserrat", 12), bg="#ECECEC", fg="#06283D")
#     password_label.grid(row=2, column=0, pady=10)
#     self.PasswordEntry = tk.Entry(main_frame, width=30, font=("Montserrat", 12), show="*")
#     self.PasswordEntry.grid(row=2, column=1, pady=10)
#
#     # Login Button
#     login_button = tk.Button(main_frame, text="Login", bg="#06283D", fg="white", font=("Montserrat", 12),
#                              command=self.ValidateUser)
#     login_button.grid(row=3, column=0, pady=20)
#
#     # Register Button
#     register_button = tk.Button(main_frame, text="Register", bg="#06283D", fg="white", font=("Montserrat", 12),
#                                 command=self.RegisterStudentPassword)
#     register_button.grid(row=3, column=1, pady=20)
#
#     # Exit Button
#     exit_button = tk.Button(main_frame, text="Exit", bg="#06283D", fg="white", font=("Montserrat", 12),
#                             command=self.ExitStudent)
#     exit_button.grid(row=4, column=0, columnspan=2, pady=20)
#
#     self.root.mainloop()

# ......................Admin Tree Views.........................
# col_width = lambda i: max(len(str(row[i])) for row in class_records) * 20
# [tree.column(i, width=min(col_width(i), len(str(col)) * 10), anchor="center") for i, col in
#  enumerate(class_records[0])]

# ...................Viewing teachers..............
# # This method will show all the registered teachers in a new window
# # This method will open a form for displaying all teachers
# global col, i
# self.masterTeacher = Toplevel(self.master)
# self.master.withdraw()
# self.masterTeacher.deiconify()
# self.masterTeacher.title("SkyLiners High School  Teachers Data.")
# self.masterTeacher.geometry("1100x500+200+100")
# self.masterTeacher.resizable(width=True,height=True)
# self.masterTeacher.config(padx=60, pady=50)
# frm1 = Frame(self.masterTeacher)
# frm1.grid(row=0, column=0)
#
# conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
# cursor = conn.cursor()
#
# cursor.execute('SELECT * FROM TeachersData')
# records = cursor.fetchall()
#
# tree = ttk.Treeview(frm1)
# tree["columns"] = tuple(range(len(records[0])))
# tree["show"] = "headings"
# # for i, col in enumerate(records[0]):
# for i, col in enumerate(cursor.description):
#     tree.heading(i,text=col[0])
#
# col_width = max(max(len(str(row[i])) for row in records), len(col[0])) * 5
# for i, col in enumerate(records[0]):
#     tree.column(i,width=col_width,anchor="center")
#
#
# for record in records:
#     tree.insert("","end",values=list(record))
#     # tree.insert("","end",values=record[0])
#
# tree.grid(row=0,column=0)
# ExitButton = Button(frm1, text="Exit", bg="Blue", fg="White", width=20, command=self.ExitTeacher)
# ExitButton.grid(row=1, column=0, pady=10,padx=50)
#
#
# self.masterTeacher.mainloop()
# 1.
# ...........configuring trees..............
# tree.grid_columnconfigure(0,weight=1)
# tree.grid_rowconfigure(0,weight=1)
# hsb = Scrollbar(frm1,orient="horizontal",command=tree.xview)
# tree.configure(xscrollcommand=hsb.set)
# hsb.grid(row= 1,column=0,sticky='ew',columnspan=5)
# 2
# col_width = lambda i: max(len(str(row[i])) for row in class_records) * 10
# [tree.column(i, width=min(col_width(i), len(str(col)) * 10), anchor="center") for i, col in
#  enumerate(class_records[0])]


# ......................Teacher Login................
# def AdminLogin(self):
#     self.teachermaster = tk.Tk()
#     self.teachermaster.title("Teachers Login Page")
#     master_frame = Frame(self.teachermaster)
#     master_frame.pack()
#     self.teachermaster.geometry("650x280+210+100")
#     self.teachermaster.config(padx=10, pady=50)
#     label1 = tk.Label(master_frame, text="Welcome to the Teachers Login  dashboard.", font='Arial, 10')
#     label1.grid(row=0, column=1, columnspan=3)
#
#     # UserName Entry.
#     UsernameLabel = tk.Label(master_frame, text="Staff Id", bg="#EDEDED", fg="#06283D")
#     UsernameLabel.grid(row=2, column=1)
#     self.UsernameEntry = Entry(master_frame, width=30)
#     self.UsernameEntry.grid(row=3, column=1, padx=10)
#
#     # Password Entry.
#     PasswordLabel = tk.Label(master_frame, text="Password", bg="#EDEDED", fg="#06283D")
#     PasswordLabel.grid(row=2, column=2)
#     self.PasswordEntry = Entry(master_frame, width=30, show="*")
#     self.PasswordEntry.grid(row=3, column=2, padx=10)
#
#     # Login Button
#     LoginButton = Button(master_frame, text="Login", bg="blue", fg="white", width=20, command=self.ValidateUser,justify=CENTER)
#     LoginButton.grid(row=5, column=1, padx=30, pady=20)
#
#     # Login Button
#     RegisterButton = Button(master_frame, text="Register", bg="blue", fg="white", width=20, command=lambda:self.NewTeacher(),justify=CENTER)
#     RegisterButton.grid(row=5, column=2, pady=20)
#
#     ExitButton = Button(master_frame, text="Exit", bg="blue", fg="white", width=20, command=self.ExitTeacher)
#     ExitButton.grid(row=6, column=1,  padx=115, pady=1)
#
#
#     self.teachermaster.mainloop()

#
# import bcrypt
# from bcrypt import hashpw
#
#
# def hash_password(password: str) -> bytes:
#     """
#     Returns a hashed password
#     Args:
#         password (str): password to be hashed
#     """
#     b = password.encode()
#     hashed = hashpw(b, bcrypt.gensalt())
#     return hashed
#
#
# def is_valid(hashed_password: bytes, password: str) -> bool:
#     """
#     Check whether a password is valid
#     Args:
#         hashed_password (bytes): hashed password
#         password (str): password in string
#     Return:
#         bool
#     """
#     return bcrypt.checkpw(password.encode(), hashed_password)

# !/usr/bin/env python3
"""
Defines a hash_password function to return a hashed password
"""
from tkinter import messagebox

import bcrypt
from bcrypt import hashpw

password = "sunday"
# def hash_password(password: str) -> bytes:
#     """
#     Returns a hashed password
#     Args:
#         password (str): password to be hashed
#     """
#     b = password.encode()
#     hashed = hashpw(b, bcrypt.gensalt())
#     messagebox.showinfo('Hashed',f'HASHED Password:{hashed}')
#     return hashed
#
#
#
# def is_valid(hashed_password: bytes, password: str) -> bool:
#     """
#     Check whether a password is valid
#     Args:
#         hashed_password (bytes): hashed password
#         password (str): password in string
#     Return:
#         bool
#     """
#     return bcrypt.checkpw(password.encode(), hashed_password)
#
# hash_password('Sunday')
# is_valid(hash_password('Sunday'),'Sunday')


# def SendMessage(self):
#     reg = self.Reg_Entry.get()
#     if reg != "":
#         account_sid = 'AC16643eb157305aed5a50dcfefd0c4ecf'
#         auth_token = '3e71fd4a0d520f8e4b3e26a504b92ac0'
#
#         client = Client(account_sid, auth_token)
#         conn = pyodbc.connect(
#             r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=J:\My Drive\SkyLinersSchoolManagementSystem\DataBases\StudentData.accdb;')
#         # Create a cursor object
#         cursor = conn.cursor()
#         cursor.execute(f"SELECT FATHER_NAME FROM StudentData WHERE REG_NO = '{reg}' ")
#         fath = cursor.fetchone()
#
#         cursor.execute(f"SELECT REG_NO, MATHS, ENGLISH, KISWAHILI, BIOLOGY, CHEMISTRY, PHYSICS, GEOGRAPHY, HISTORY, CRE, COMPUTER_STUDIES, TOTAL, AVERAGE, GRADE,COMMENT FROM ExamRecords WHERE REG_NO='{self.reg}'")
#         rows = cursor.fetchone()
#         msg = f"\n\nSKYLINE HIGH SCHOOL STUDENT RESULTS\n" \
#               f"Greetings, Mr. {fath[0]}. This is your Son's {rows[0]} performance.\n" \
#               f"Maths: {rows[1]}\nEnglish: {rows[2]}\nKiswahili: {rows[3]}\n" \
#               f"Biology: {rows[4]}\nChemistry: {rows[5]}.\n" \
#               f"Physics: {rows[6]}.\nGeography: {rows[7]}\nHistory: {rows[8]}\nCRE: {rows[9]}\n" \
#               f"Computer Studies: {rows[10]}\n\nTOTAL: {rows[11]}\nAVERAGE SCORE: {rows[12]}\nGRADE: {rows[13]}" \
#               f"Class Teacher's Comment: {rows[14]}"
#         message = client.messages.create(
#             body=msg,
#             from_='+12545664699',
#             to='+254 795 398253'
#         )
#         if message:
#             messagebox.showinfo('Success.','Message Sent Successfully.')
#         print(message.sid)
#     messagebox.showerror('Null Registration',"Enter the Registration Number!!")

# def SendEmail(self):
#     sender_email = 'your_sender_email@example.com'
#     receiver_email = 'your_receiver_email@example.com'
#     subject = 'Test Email'
#     message = 'This is a test email.'
#
#     self.send_email(sender_email, receiver_email, subject, message)
# sg_api_key = 'YOUR_SENDGRID_API_KEY'
#
# def send_email(sender_email, receiver_email, subject, message):
#     message = Mail(
#         from_email=sender_email,
#         to_emails=receiver_email,
#         subject=subject,
#         plain_text_content=message)
#
#     try:
#         sendgrid_client = SendGridAPIClient(sg_api_key)
#         response = sendgrid_client.send(message)
#         print('Email sent successfully')
#     except Exception as e:
#         print('Email sending failed')
#         print(str(e))

#.......................sending mails..................
# Set up your SendGrid API key
# sg_api_key = os.environ.get('SENDGRID_API_KEY')
#
# # Create a Mail object
# message = Mail(
#     from_email='sender@example.com',
#     to_emails='recipient@example.com',
#     subject='Example Email',
#     plain_text_content='This is the plain text content of the email.'
# )
#
# # Create an instance of the SendGridAPIClient
# sg_client = SendGridAPIClient(api_key=sg_api_key)
#
# # Send the email using the SendGridAPIClient
# response = sg_client.send(message)
#
# # Check the response status code
# if response.status_code == 202:
#     print('Email sent successfully')
# else:
#     print('Email sending failed')
#     print(response.body)

