import pprint
import sys

students=[]
students.append({1001:'', 'subject':'','marks':''})
students.append({1002:'', 'subject':'','marks':''})
students.append({1003:'', 'subject':'','marks':''})
students.append({1004:'Aniket', 'subject':'Maths','marks':98})
students.append({1005:'Mani', 'subject':'Maths','marks':100})

pprint.pprint(students)
#for i in students:
    #students.append({1006:'Sethu','subject':'Maths','marks':76})


def table(ranks):
  try:  
   print(ranks['1001']+ '|' + ranks['subject'] + '|' + ranks['marks'])
   print ('---------------------------------------------')
   print(ranks['1002']+ '|' + ranks['subject'] + '|' + ranks['marks'])
   print ('---------------------------------------------')
   print(ranks['1003']+ '|' + ranks['subject'] + '|' + ranks['marks'])
  except:
      print('Sorry',sys.exc_info()[0],'appeared')
    
table(students)
