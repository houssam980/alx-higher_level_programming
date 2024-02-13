#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let ctr = 0;
  list.forEach((ocur) => {
    if (ocur === searchElement) ctr++;
  });
  return ctr;
};
