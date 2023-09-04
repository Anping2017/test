var http = require('http');
var fs = require('fs');
var path = require('path');
var mime = require('mime');  //mime模块有根据文件扩展名, 得出MIME类型的能力
var cache = {};
var chatServer = require('./lib/chat_server');

//静态404服务, 当文件不存在时响应
function send404(response) {
    response.writeHead(404,{'Content-Type': 'text/plain'});
    response.write('Error 404: resource not found.');
    response.end();
}

//文件数据服务
function sendFile(response, filePath, fileContents) {

    response.writeHead(
        200,
        {'content-type': mime.lookup(path.basename(filePath))}  //自动识别为text/html
    );
    response.end(fileContents);
}

//提供静态服务
function serveStatic(response, cache, absPath){
    if(cache[absPath]) {
        sendFile(response, absPath,cache[absPath]);
    } else {
        fs.exists(absPath,function(exists){
            if(exists) {
                console.log(absPath)
                fs.readFile(absPath,function(err,data){
                    if(err) {
                        send404(response);
                    } else {
                        cache[absPath] = data;
                        sendFile(response,absPath,data);
                    }
                });
            } else {
                send404(response);
            }
        });
    }
}


var server = http.createServer(function(request,response){
    var filePath = false;
 
    if(request.url == '/') {
        filePath = 'pub/index.html';
    } else {
        filePath = 'pub' + request.url;
    }
    var absPath = './nodejs/chatrooms/' + filePath;
    serveStatic(response,cache,absPath);
});

server.listen(3000,function(){
    console.log("server is on");
});

chatServer.listen(server);