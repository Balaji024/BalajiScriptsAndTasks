

import shelve
filePath='H:\pythonScripts\Verbose.py'
openFile=open(filePath)
content=openFile.read()
print(content)

read=openFile.readlines()
print(read)
openFile.close()

newfile='H:\pythonScripts\Cristiano.txt'
newfile1=open(newfile,'w')
newfile1.write('''
Cristianoooooooo 
Ronaldo
s''')
newfile1.close()
newfile2=open(newfile)
content1=newfile2.read()
print(content1)
newfile2.close()


shelfile=shelve.open('H:/Cristiano1.txt')
shelfile['realmadrid-fullbacks']=['Marcelo','Sergio Ramos','Rapahel Varane','Mendy']
readit=shelfile.keys()
print(readit)
shelfile.close()