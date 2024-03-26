#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dir = {};

request(url, function (err, data, body) {
if (err) {
console.log(err);
} 
else {
const response = JSON.parse(body);
for (let i = 0; i < response.length; i++) {
if (response[i].completed === true) {
if (dir[response[i].userId] === undefined) {
dir[response[i].userId] = 1;
} else{
dir[response[i].userId] += 1;
}
}
}
}
console.log(dir);
});
