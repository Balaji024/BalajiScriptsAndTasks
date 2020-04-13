var fs = require("fs");
console.log("start");
var content = fs.readFileSync("sample.txt","utf8");
console.log(content);
console.log("stoped");
