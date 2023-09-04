const fs = require('fs');
fs.readFile('./abc.json',function(err,data){
    console.log(data);
})