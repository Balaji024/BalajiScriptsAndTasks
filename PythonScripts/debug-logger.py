# logging is used to log the program flow line by line and thereby show the output to the suer and the log info in separate file.

import logging

logging.basicConfig(filename="H:/pythonScripts/logs.txt", level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

logging.debug("Start of the Program")
Students=["Ajeeth", "Aniket", "Kamesh", "Mani", "Logesh", "SethuRaman"]
for students in Students:
    logging.debug('students is %s, Students is %s' % (students, Students))
    print('My name is :', students)
    
    
    
