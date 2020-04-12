import send2trash
import shutil
import os
#shutil.copy('H:/pythonScripts/Verbose.py','H:/pythonScripts/2.txt')
#shutil.move('H:/pythonScripts/Verbose.py','H:/')
myfile=os.path.isfile('H:/Verbose.py')
print('myfile',myfile)
opened=open('H:/pythonScripts/2.txt')
read=opened.read()
print(read)
opened.close()
shutil.move('H:/pythonScripts','G:/')
shutil.copytree('H:/','g:/')  #copying folder
#removing files permanentlt
os.unlink('H:/Readme.md')
#'removing folder
shutil.rmtree()
send2trash.send2trash()