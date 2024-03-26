#!/usr/bin/node
const fss = require('fs');
const request = require('request');
const url = process.argv[2];
const pth = process.argv[3];

request(url, function (err, data, body) {
  if (err) {
console.log(err);
} 
else {
fss.writeFile(pth, body, 'utf8', function (err) {
if (err) {
console.log(err);
}
});
}
});
