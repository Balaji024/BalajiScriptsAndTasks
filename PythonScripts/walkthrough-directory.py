import os
#This loop gives all the folders and subfolders and files in H:/ directory
for folder,subfolder,files in os.walk('H:/'):

     print('The folder is' + folder)
     print('The subfolder is' + str(subfolder))
     print('The file is' + str(files))
     print()