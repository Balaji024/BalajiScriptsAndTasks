#Sqlplus Installation Steps on Ubuntu:
mkdir mydb
cd mydb
git clone https://github.com/Balaji024/AppSetups.git
cd /opt
mkdir /opt/oracle
sudo mv /home/ubuntu/AppSetups/oracleamd4-zip/instantclient-basic-linuxAMD64-10.1.0.5.0-20060519.zip .
sudo mv /home/ubuntu/AppSetups/oracleamd4-zip/instantclient-sdk-linuxAMD64-10.1.0.5.0-20060519.zip .
sudo mv /home/ubuntu/AppSetups/oracleamd4-zip/instantclient-jdbc-linuxAMD64-10.1.0.5.0-20060519.zip  .  
sudo mv /home/ubuntu/AppSetups/oracleamd4-zip/instantclient-sqlplus-linuxAMD64-10.1.0.5.0-20060519.zip . 
sudo apt install unzip
sudo unzip instantclient-basic-linuxAMD64-10.1.0.5.0-20060519.zip
sudo unzip instantclient-sqlplus-linuxAMD64-10.1.0.5.0-20060519.zip
cd instantclient10_1
#ln -s libclntsh.so.10.1 libnnz10.so
#ln -s libocci.so.10.1  libociei.so
sudo apt install libaio1
cd ~/
echo "export LD_LIBRARY_PATH=/opt/oracle/instantclient10_1:$LD_LIBRARY_PATH" > export1
echo "export PATH=/opt/oracle/instantclient10_1:$PATH" > export2
cat export1 export2 >> ~/.profile
source ~/.profile
#sqlplus hkiaflightsdb/hkiaflightsdbpassword@//172.25.4.112:1521/XE
 