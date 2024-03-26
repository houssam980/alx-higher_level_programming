#!/usr/bin/node

const f_path = process.argv[2];
const fs = require('fs');
fs.readFile(f_path, 'utf8', function (err, data) {
if (err) {
console.log(err);
} 
else {
console.log(data);
  }
});
