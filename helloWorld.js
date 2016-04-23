var http = require('http');

var express = require('express');

var exec = require('child_process').exec;

var server = express.createServer();

server.configure(function(){    

    server.use(express.static(__dirname + '/public'));

});

server.get('/', function(req, res) {

    res.writeHead(200, {'Content-Type': 'text/html'});

    res.write('R graph<br>');

    process.env.R_WEB_DIR = process.cwd() + '/public';

    var child = exec('Rscript script/xyplot.R', function(error, stdout, stderr) {

        console.log('stdout: ' + stdout);

        console.log('stderr: ' + stderr);

        if (error !== null) {

            console.log('exec error: ' + error);

        }

        res.write('<img src="/xyplot.png"/>');

        res.end('<br>end of R script');

    });

});

server.listen(1337, "127.0.0.1");

console.log('Server running at http://127.0.0.1:1337/');
