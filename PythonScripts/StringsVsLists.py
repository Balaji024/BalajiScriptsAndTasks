#strings vs lists
#Strings are immutable it values cant be changed
#Lists are mutable and it can be changed.
import copy
#1. Testing String Immmutability
name='balaji'
print (name[4])
#name[2] = 'h'
print (name[4])
#2. Testing Lists Mutability.
lists=list(range(5,10))
lists[2]=8
print (lists)

#3. Function to check the refernces that neutralizes the gobal and local.
def myname(names):
  names.append('balaji')
spam=['sachin','Ronaldo']
myname(spam)
print (spam)

#4. References to a list
jungle=[1,2,'hello']
print (jungle)
cheese=jungle
print (cheese)
# changing the list through cheese reference affects jungle reference automatically.
cheese[2]='Hy'
print (jungle)
print (cheese)
# making a separate list to the reference thereby copying using copy module and deepcopy method
cheese=copy.deepcopy(jungle)
cheese[2]='HiHelloWelcome'
print (cheese)
print (jungle)
# to break the indentation and continue printing on same line
print ('Im a king for my own kingdom ' + \
       'so please be careful' )

#output:Im a king for my own kingdom so please be careful
