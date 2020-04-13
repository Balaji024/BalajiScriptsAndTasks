var fs = require("fs");
console.log("Start Reading");
fs.readFile("sample.txt","utf8",function(error,data){
 console.log(data);
});
console.log("stoped");
