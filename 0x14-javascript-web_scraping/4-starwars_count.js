#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    let ctr = 0;
    const mvs = JSON.parse(body).results;
    for (let result = 0; result < mvs.length; result++) {
      const characters = mvs[result].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j] === 'https://swapi-api.hbtn.io/api/people/18/' || characters[j] === 'http://swapi-api.hbtn.io/api/people/18/') {
          ctr += 1;
        }
      }
    }
    console.log(ctr);
  }
});
