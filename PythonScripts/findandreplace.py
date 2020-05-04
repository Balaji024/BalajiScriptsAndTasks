#Find and Replace

import re
text="This was my perfect way to think about docker"
myfile=re.compile(r'about \w+')
mo1=myfile.findall(text)
print(mo1)
mo2=myfile.sub('kuberntes',text)
print(mo2)

