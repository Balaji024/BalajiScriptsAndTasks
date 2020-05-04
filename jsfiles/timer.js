function welcome(){
	console.log("Hi Balaji how are youo");
}
var id3=setImmediate(welcome,1000);
//var id1=setInterval(welcome,1000);
welcome();
var id2=setTimeout(welcome,1000);
//clearTimeout (id2)

