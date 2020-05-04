text="Yes"
print(text.upper())
print(text.lower())
answer = "yes"

if answer.lower() == "yes":
 print (answer.lower() )
else:
    print("Program Malfunctioned")

result1=answer.isalpha() # will look for string only
print(result1)
ans="hello123"
result2=ans.isalnum()  # will look for string and integers
print(result2)
ans2='123'
result3=ans2.isdecimal() # will look for decimals
print(result3)
space=" "
result4=space.isspace()  # will look for space
print(result4)
text1="hello World"
print(text1.title()) # will print 1st letter in uppercase
text2="Heloo-world"
result5=text2.istitle() # will look for 1st letter uppercase
print(result5)
ronaldo='Ronaldo CR7'.endswith('CR7')
print(ronaldo,'ronaldo')
cr7='Ronaldo CR7'.startswith('Ronaldo')
print(cr7,'cr7')
combine=''.join(text2 +' '+ text1)
print(combine,'combine')
split='viva ronaldocr7'.split('cr7')
print(split,'split')
.ljust()
.rjust()
.center()
.strip()
.rstrip()
.lstrip()