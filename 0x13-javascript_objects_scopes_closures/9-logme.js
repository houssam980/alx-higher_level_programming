#!/usr/bin/node

let ctr = 0;
exports.logMe = function (item) {
  console.log(`${ctr++}: ${item}`);
};
