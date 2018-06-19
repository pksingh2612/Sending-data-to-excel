from tkinter import *
import sqlite3 as s3
def insertstudent():
    root = Tk()  
    root.geometry('550x600')
    root.title('Exam Hall Allocated System')
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()
    var6 = StringVar()
    var7 = StringVar()
    var8 = StringVar()
    var9 = StringVar()
    var10 = StringVar()
    
    def reset1():
        var1.set('')
        var2.set('')
        var3.set('')
        var4.set('')
        var5.set('')
        var6.set('')
        var7.set('')
        var8.set('')
        var9.set('')
        var10.set('')
        
    def submit1():
        print('hi')
        Var1 = insstdentry_1.get()
        Var2 = insstdentry_2.get()
        Var3 = insstdentry_3.get()
        Var4 = insstdentry_4.get()
        Var5 = insstdentry_5.get()
        Var6 = insstdentry_6.get()
        Var7 = insstdentry_7.get()
        Var8 = insstdentry_8.get()
        Var9 = insstdentry_9.get()
        Var10 =insstdentry_10.get()
        dbase = s3.connect('Database1.db')  # Open a database File
        print('Database opened')

        dbase.execute('''CREATE TABLE IF NOT EXISTS student(
        RollNo TEXT,
        StudentId TEXT PRIMARY KEY,
        StudentName TEXT ,
        StudentPassword TEXT,
        Course TEXT,
        Branch TEXT,
        Year INT,
        DOB TEXT,
        StudentMobileNo TEXT,
        StudentEmailid TEXT
        )''')

        print('Table hall created')

        dbase.execute('''INSERT INTO student(RollNo,StudentId,StudentName,StudentPassword,Course,
        Branch,Year,DOB,StudentMobileNo,StudentEmailid)VALUES(?,?,?,?,?,?,?,?,?,?)''', 
                      (Var1, Var2, Var3, Var4, Var5, Var6, Var7, Var8, Var9, Var10))
        dbase.commit()
        print('Record inserted')
        dbase.close()
        print('Database Closed')
        
    insstdlabel_0 = Label(root, text='Insert New Student Detail',
                    width=20, font=('bold', 20))
    insstdlabel_0.place(x=90, y=30)

    insstdlabel_1 = Label(root, text='Roll No.', width=20, font=('bold', 10))
    insstdlabel_1.place(x=80, y=80)
    insstdentry_1 = Entry(root, width=30,textvariable=var1)
    insstdentry_1.place(x=240, y=80)

    insstdlabel_2 = Label(root, text='Id', width=20, font=('bold', 10))
    insstdlabel_2.place(x=80, y=120)
    insstdentry_2 = Entry(root, width=30,textvariable=var2)
    insstdentry_2.place(x=240, y=120)

    insstdlabel_3 = Label(root, text='Name', width=20, font=('bold', 10))
    insstdlabel_3.place(x=80, y=160)
    insstdentry_3 = Entry(root, width=30, textvariable=var3)
    insstdentry_3.place(x=240, y=160)

    insstdlabel_4 = Label(root, text='Password', width=20, font=('bold', 10))
    insstdlabel_4.place(x=80, y=200)
    insstdentry_4 = Entry(root, width=30, show='*', textvariable=var4)
    insstdentry_4.place(x=240, y=200)

    insstdlabel_5 = Label(root, text='Course', width=20, font=('bold', 10))
    insstdlabel_5.place(x=80, y=240)
    insstdentry_5 = Entry(root, width=30, textvariable=var5)
    insstdentry_5.place(x=240, y=240)

    insstdlabel_6 = Label(root, text='Branch', width=20, font=('bold', 10))
    insstdlabel_6.place(x=80, y=280)
    insstdentry_6 = Entry(root, width=30, textvariable=var6)
    insstdentry_6.place(x=240, y=280)

    insstdlabel_7 = Label(root, text='Year', width=20, font=('bold', 10))
    insstdlabel_7.place(x=80, y=320)
    insstdentry_7 = Entry(root, width=30, textvariable=var7)
    insstdentry_7.place(x=240, y=320)
    # label_1 = Label(root, text='Subjects', width=20, font=('bold', 10))
    # label_1.place(x=80, y=360)

    insstdlabel_8 = Label(root, text='DOB', width=20, font=('bold', 10))
    insstdlabel_8.place(x=80, y=360)
    insstdentry_8 = Entry(root, width=30, textvariable=var8)
    insstdentry_8.place(x=240, y=360)

    insstdlabel_9 = Label(root, text='Mobile No.', width=20, font=('bold', 10))
    insstdlabel_9.place(x=80, y=400)
    insstdentry_9 = Entry(root, width=30, textvariable=var9)
    insstdentry_9.place(x=240, y=400)

    insstdlabel_10 = Label(root, text='Email-id', width=20, font=('bold', 10))
    insstdlabel_10.place(x=80, y=440)
    insstdentry_10 = Entry(root, width=30, textvariable=var10)
    insstdentry_10.place(x=240, y=440)

    logbtn1 = Button(root, text='Submit', width=15, bg='brown',
                     fg='white', relief=RAISED, command=submit1).place(x=130, y=500)

    logbtn2 = Button(root, text='Reset', width=15, bg='brown',
                     fg='white', relief=RAISED, command=reset1).place(x=300, y=500)

    root.mainloop()


#insertstudent()
