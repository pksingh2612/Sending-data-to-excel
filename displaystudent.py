import xlsxwriter
import sqlite3 as s3
def display():
    expenses1 = ('RollNo', 'StudentId', 'StudentName','StudentPassword', 'Course', 
                'Branch', 'Year', 'DOB', 'StudentMobileNo', 'StudentEmailid',)
    expenses=[expenses1,]
    dbase = s3.connect('Database1.db')  # Open a database File
    print('Database opened')
    data = dbase.execute('Select * from student')
    for record in data:
        expenses.append(record)
    
    print(expenses)
    print(len(expenses))
    print(expenses[0][1])
    dbase.close()
    print('Database Closed')

    # Create a workbook and add a worksheet. 
    workbook = xlsxwriter.Workbook('Expenses02.xlsx') 
    worksheet = workbook.add_worksheet() 
    # Add a bold format to use to highlight cells. 
    bold = workbook.add_format({'bold': True,'font_color': '#9CB640'})
    date_format = workbook.add_format({'num_format': 'd mmm yyyy'})
    # Write some data headers.
    for i in range(0,len(expenses1)):
        worksheet.write(0, i,expenses[0][i],bold)
    
    #Start from the first cell below the headers. 

    # Iterate over the data and write it out row by row. 
    for i in range(0,len(expenses1)):
        for j in range(1,len(expenses)):
            worksheet.write(j,i,expenses[j][i])

    # date_format = workbook.add_format({'num_format': 'yyyy mmm d'})

    # for i in range(1,len(expenses)):
    #     worksheet.write(i, expenses1.index('DOB'), expenses[i][expenses1.index('DOB')], date_format)

    workbook.close()

