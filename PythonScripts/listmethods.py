#List Methods
num = ['cat','balaji','arti','aniket']
#append method to append a value to the list
num.append('ajeeth')
num[4:7] = 'ajeeth','kamesh','logesh','sethu'
# remove method to remove a value from the list
num.remove('sethu')
# del method to remove an index value form the list 
del num[0]
# sort method to sort the list
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num = ['Animal','Balaji','animal','balaji']
num.sort()
print(num)
# sorting in a upper and lowercase manner..
num.sort(key=str.lower)
print(num)
num.sort(key=str.upper)
print(num)


#Note: we cant sort if the integers and numbers are in the same list

