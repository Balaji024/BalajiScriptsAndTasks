import PyPDF2
import os
os.chdir('H:\pythonScripts\BalajiScriptsAndTasks\PythonScripts')

pdf=open('mypdf.pdf', 'rb')
reader=PyPDF2.PdfFileReader(pdf)
print(reader.numPages)
page = reader.getPage(0)
print(page.extractText())


for content in range(reader.numPages):
   print(reader.getPage(content).extractText())

content = reader.getPage(content).extractText()

writer = PyPDF2.PdfFileWriter()
page = writer.addPage('Hi helolo')
outputfile = open('mypdf2', 'wb')
writer.write(outputFile)
outputfile.close()
pdf.close()
