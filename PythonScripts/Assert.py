#assert statements will be used to say the program to crash when certain condition is not met which.
#Assert error are not user exception it is a programmer exception
#user exception we can use raise Exceptions.

import time
import traceback
from datetime import datetime

now=datetime.now()
signalLights={1:"red", 2:"yellow", 3:"green"}

def trafficLights(signal):
 try:  
    for keys in signal.keys():
      if signal[keys]=="red":
         time.sleep(2)
         signal[keys]="yellow"
      elif signal[keys]=="yellow":
         time.sleep(2)
         signal[keys]="green"
      elif signal[keys]=="green":
         time.sleep(2)
         signal[keys]="red"
    assert "red" in signal.values(), 'Signal is Not working' + str(signal)
    assert "yellow" in signal.values(),'Signal is Not working' + str(signal)
    assert "green" in signal.values(),'Signal is Not working' + str(signal)
 except:
     errorFile=open('H:/py_errors.txt','a')
     currentTime=now.strftime("%d/%m/%y::%H:%M:%S")
     errorFile.write("----------------------------------")
     errorFile.write(currentTime)
     errorFile.write(traceback.format_exc())
     errorFile.write("----------------------------------")
     errorFile.close()
     print("Sorry Unexpected Error Happened Check the Logs")
     
print(signalLights)
trafficLights(signalLights)
print(signalLights)
   
