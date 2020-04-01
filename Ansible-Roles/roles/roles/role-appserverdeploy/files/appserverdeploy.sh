# Author: balaji


#!/bin/bash
dir=appserverdeploy
path = /home/ubuntu/appserverdeploy/springbootapp_pune/FlightStatusServiceImpl
if [ -d $dir ]
then
   sudo rm -rf appserverdeploy
   mkdir appserverdeploy
   cd appserverdeploy
   git clone https://ansible-story@dev.azure.com/ansible-story/springbootapp_pune/_git/springbootapp_pune
   cd springbootapp_pune/FlightStatusServiceImpl/
   sleep 10s
   nohup mvn spring-boot:run -Doracle.jdbc.timezoneAsRegion=false -DHOMEPATH=$path &
else
   mkdir appserverdeploy
   cd appserverdeploy
   git clone https://ansible-story@dev.azure.com/ansible-story/springbootapp_pune/_git/springbootapp_pune
   cd springbootapp_pune/FlightStatusServiceImpl/
   sleep 10s
   nohup mvn spring-boot:run -Doracle.jdbc.timezoneAsRegion=false -DHOMEPATH=$path &
  
fi