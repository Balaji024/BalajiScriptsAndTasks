const fs = require('fs');
function myfile(err, data){
	if(err)
	{
		console.log("Sorry File Does Not Exist",err);
	}
	else{
	console.log("data")
}}
fs.readFile('/home/ubuntu/console.js',myfile);
fs.readFile('/home/ubuntu/console23.js',myfile);

