var http = require('http');

var server = http.createServer();

server.on('request', function(request,response) {
    console.log('your request is from: ' + request.url);
    console.log('your request local address: ' , request.socket.remoteAddress, request.socket.remotePort);

    response.write('hello world');
    response.end();
}
)

server.listen(3000,function(){
    console.log('server is on');
})