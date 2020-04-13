var age = process.stdin;
age.setEncoding('utf-8');
console.log("Please Enter your age");
age.on('age',function vote(age){
	if(age < 18){
	console.log("Only people above 18years of age can vote");
	}
	else{
		console.log("You are eligible to vote");
	}

});
//vote(20);
//vote(19);
//vote(16);
//vote(age);
