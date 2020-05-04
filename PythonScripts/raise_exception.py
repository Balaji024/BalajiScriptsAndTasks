import traceback

def mobileVerification(number):
  try:
    if(len(str(number)) < 10):
        raise Exception("Please enter a Valid mobile number")
    else:
        print('Thank you ')
  except:
      errorFile= open('H:/py_errors.txt','a')
      errorFile.write(traceback.format_exc())
      errorFile.close()
      print('The Error is Captured in your Log File')
mobileVerification(8858237609)
mobileVerification(861000672)
