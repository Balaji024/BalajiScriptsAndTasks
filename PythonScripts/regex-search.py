import re
import sys
#message="hi my no 56-56-56"
#search() method will find the first occurence of the search text.
ph=re.compile(r'\+91\d\d\d\d\d\d\d\d\d\d')
mo=ph.search("Hi is this you no +918989898989")
print(mo.group())


#Pipe and groups
mytexts = "logesh kamesh ritesh"
find=re.compile(r'(kam|rit|muk)esh')
mo1=find.search(mytexts)
print(mo1.group())


#Greedy and Non-Greedy
#* --> match 0 or more times
#+  ---> match 1 or more times.
#? ---> matches in or condition either of this or that.

# ------- (?)--------
file1= "Hi Im a batsman batswoman"
try:
  catch=re.compile(r'bats(wo)?man')
  mo2=catch.search(file1)
  print(mo2.group())
except:
  print('Sorry', sys.exc_info()[0], 'appeared')
#-----(*)------------------
file2= "Hi Im a  batswoman batsman"
try:
  catch=re.compile(r'bats(wo)*man')
  mo3=catch.search(file2)
  print(mo3.group())
except:
  print('Sorry', sys.exc_info()[0], 'appeared')
#---------(+) 
file3=('Hello guys there is a good batswoman batswoman batsman')  
try:
  catch=re.compile(r'bats(wo)+man')
  mo4=catch.search(file3)
  print(mo4.group())
except:
  print('Sorry', sys.exc_info()[0], 'appeared')

# Finding Multiple occurences
#{}curly braces indictaed how many occurence you want to find for the searching.
# Inside curly braces you can set the range of occurence you need to find (3,5)
mobile= ('+919551013265 +918610006728 8858237609 9176272697')
try:
 catch=re.compile(r'((\+91)?\d\d\d\d\d\d\d\d\d\d( )?){3,5}')
 mo5=catch.search(mobile)
 print(mo5.group())
except:
 print('Sorry', sys.exc_info()[0], 'appeared')







