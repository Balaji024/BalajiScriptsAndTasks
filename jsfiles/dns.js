
// Finding the dns name for the service and host:

const dns = require('dns');  
dns.lookupService('13.234.31.172',22,(err,hostname, service) => {  
  console.log(hostname, service);
 // var host = hostname
  
    // Prints: localhost  
});  

//finding ip address of the dns name.
//const dns = require('dns');  
dns.lookup('ec2-13-234-31-172.ap-south-1.compute.amazonaws.com', (err, addresses, family) => {  
  console.log('addresses:', addresses);  
  console.log('family:',family);  
});  
