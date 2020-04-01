#Author: Balaji
#!/bin/bash
dir=apideploy
path=/home/ubuntu/apideploy/springbootapp_pune/FlightStatusServiceImpl
if [ -d $dir ]
then
   sudo rm -rf apideploy
   mkdir apideploy
   cd apideploy 
   git clone https://ansible-story@dev.azure.com/ansible-story/springbootapp_pune/_git/springbootapp_pune
   cd springbootapp_pune/FlightsStatusResource/
   nohup mvn spring-boot:run -Doracle.jdbc.timezoneAsRegion=false -DHOMEPATH=$path &
else
   mkdir apideploy
   cd apideploy 
   git clone https://ansible-story@dev.azure.com/ansible-story/springbootapp_pune/_git/springbootapp_pune
   cd springbootapp_pune/FlightsStatusResource/
   nohup mvn spring-boot:run -Doracle.jdbc.timezoneAsRegion=false -DHOMEPATH=$path & 
fi

