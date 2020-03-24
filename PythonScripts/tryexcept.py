import sys
def mysalary(sal):
    try:
     con= 10000
     salupdate =con/sal
     print (salupdate)
    except:
        print ('Incorrect',sys.exc_info()[0], 'found')
   
mysalary(2)
mysalary(0)
mysalary('Hello')
mysalary(4)
