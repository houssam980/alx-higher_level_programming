#!/usr/bin/node
const rq = require('request');
const endp = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request({ url: endp, methods: 'GET' }, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(body && JSON.parse(body).title);
  }
});
