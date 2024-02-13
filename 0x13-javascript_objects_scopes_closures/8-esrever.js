#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((_, indx, arr) => arr[arr.length - 1 - indx]);
};
