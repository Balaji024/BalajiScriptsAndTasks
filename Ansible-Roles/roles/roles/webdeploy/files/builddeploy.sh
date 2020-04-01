# Author : "Balaji"
#!/bin/bash
dir=webdeploy
if [ -d $dir ]
then
   sudo rm -rf webdeploy
   mkdir webdeploy   
   cd webdeploy
   git clone -b Testing https://ansible-story@dev.azure.com/ansible-story/springbootapp_pune/_git/springbootapp_pune
   cd springbootapp_pune/flight-tracking/
   mvn clean package
   #cp /home/ubuntu/webdeploy/springbootapp_pune/flight-tracking/target/flight-tracking-web.war /usr/share/tomcat/webapps/
else
   mkdir webdeploy 
   cd webdeploy
   git clone -b Testing https://ansible-story@dev.azure.com/ansible-story/springbootapp_pune/_git/springbootapp_pune
   cd springbootapp_pune/flight-tracking/
   mvn clean package
   #cp /home/ubuntu/webdeploy/springbootapp_pune/flight-tracking/target/flight-tracking-web.war /usr/share/tomcat/webapps/
fi