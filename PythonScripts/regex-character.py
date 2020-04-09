# Dot,Dollar,Caret,star characters:
import sys, re
myfile="Hi hello are you there"
try:
    find=re.compile(r'^hello')
    mo1=find.search(myfile)
    print(mo1.group())
except:
    print('Sorry',sys.exc_info()[0], 'found')
