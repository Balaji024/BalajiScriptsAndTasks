# verbose mode
#Useful to know about the pattern we have given to be matched later on if we see the script.
import re
import pyperclip
import sys
text= pyperclip.paste() # holds the clipboard's copied text.
emailRegex=re.compile(r'''
[a-zA-Z0-9+*$%]+  # emailname
@                 #@
[a-zA-Z0-9+*$%]+  # domain name 
.[a-z]+           #.com
''',re.VERBOSE)
try:
 extractedEmail=emailRegex.findall(text)
 #print(extractedEmail)
except:
 print('Sorry',sys.exc_info()[0], found)
allemails=[]
for email in extractedEmail:
  allemails.append(email)
#result='\n'.join(extractedEmail)
result=' '.join(allemails)
pyperclip.copy(result)