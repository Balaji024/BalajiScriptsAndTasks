#Dictionary Data types
import pprint
students={1001:'Kamesh',1002:'Balaji',1003:'Ajeeth',1004:'Aniket',1005:'Mani'}
Marks={'Maths':80,'English':82,'Science':78,'Social':87,'Tamil':87}
for names in students.values():
    Marks.setdefault('Geography','98')
    print ((names),(Marks))
#Count of Character in a String

message='It balaji'
count={}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1
print(count)
pprint.pprint(count)
mykeys=pprint.pformat(count)
print (mykeys)
