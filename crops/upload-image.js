const connection = require("./db");
const testQuery = "SELECT name, src FROM board"

connection.connect()

connection.query(testQuery, (error, result, fields ) => {
    if (error) {
        throw error
    } else {
        src = result;
        console.log(src)
        return src
    }
})

connection.end();

console.log("연결 끝.")
console.log(src)