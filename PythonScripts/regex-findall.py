# Findall:
import sys, re
mytext="8610006728 hello 91762272996 welcome 8858237609 baby"
try:
 fileregex=re.compile(r'\d+\s\w+')
 mo1=fileregex.findall(mytext)
 print(mo1)
except:
 print('Sorry', sys.exc_info()[0], 'appeared')

#character class

myfinds=re.compile(r'[12345]')
file1="hi hello my number is 987812"
mo2=myfinds.findall(file1)
print(mo2)

# character class with successionn
myfinds=re.compile(r'[12345]{2}')
file1="hi hello my number is 987812"
mo2=myfinds.findall(file1)
print(mo2)

#negative chracter class '^' ignores specified search text.
myfinds=re.compile(r'[^12345]')
file1="hi hello my number is 987812"
mo2=myfinds.findall(file1)
print(mo2)

