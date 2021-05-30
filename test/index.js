var http = require('http');
var fs = require('fs');
var url = require('url');
var qs = require('querystring');
var mysql = require('mysql2');
var db = mysql.createConnection({
    host:'localhost',
    user:'root',
    password:'0000',
    database:'pbl'
});
db.connect();


function templateHTML(title, body, control){
    return template = `
        <!doctype html>
        <html>
        <head>
        <title>WEB - ${title}</title>
        <meta charset="utf-8">
        </head>
        <body>
        <h1><a href="/">WEB</a></h1>
        ${control}
        <br>
        ${body}
        </body>
        </html>
        `;
}



var app = http.createServer(function(request, response){
    var _url = request.url;
    var queryData = url.parse(_url, true).query;
    var pathname = url.parse(_url, true).pathname;  

    if (pathname === '/'){
        if (queryData.id === undefined){
          
            var title = "Welcome";
            var description = "Hello, Node.js";
            var template = templateHTML(
                title, 
                description,
                `<a href="/create">create</a>`
            );
            response.writeHead(200);
            response.end(template);
            
        } 

    } else if(pathname === "/create") {
        var title = "Web-Create";
        var template = templateHTML(
            title, 
            "test",
            `
            <form action="/create_process" method="POST">
                <p><input type="text" name="title" placeholder="title"><p>
                <p><textarea name="description" placeholder="description"></textarea></p>
                <p><input type="submit"></p>
            </form>
            `);
        
        response.writeHead(200);
        response.end(template);

    } else if(pathname === "/create_process") {
        var body = '';

        request.on('data', (data)=>{
            body = body + data;
        });

        request.on('end', function(){
            var post = qs.parse(body);
            db.query(`
                INSERT INTO board_test (name, content, created) 
                VALUES(?, ?, NOW())`,
                [post.title, post.description], 
                function(error, result){
                    if(error){
                        throw error;
                    }
                    
                    response.writeHead(302, {Location: `/`});
                    // response.writeHead(200);
                    response.end();
                }
            )
        });

    } else {
        response.writeHead(404);
        response.end('NOT FOUND');
    }
});

app.listen(3000);