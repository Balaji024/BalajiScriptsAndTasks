import openpyxl
import os

wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')
sheet['A1'] = 'Name'
sheet['A2'] = 'Age'
os.chdir('H:\pythonScripts\BalajiScriptsAndTasks\PythonScripts')
wb.save('workbook2.xlsx')
wb.create_sheet('MySheet')
MySheet = wb.get_sheet_by_name('MySheet')
MySheet['A1'] = 'Company'
wb.save('workbook2.xlsx')
