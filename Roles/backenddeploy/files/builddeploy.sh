#Author: Balaji
#!/bin/bash
git clone -b Ansible-Roles https://ansible-story@dev.azure.com/ansible-story/springbootapp_pune/_git/springbootapp_pune
$path = ~/springbootapp_pune
if [ $path -eq true ]
then

cd springbootapp_pune/FlightStatusServiceImpl
else
	echo "failed to clone"
fi
mvn clean package
cp springbootapp_pune/FlightsStatusServiceImpl/target/FlightsStatusServiceImpl-0.1.0.jar /usr/share/tomcat/webapps
