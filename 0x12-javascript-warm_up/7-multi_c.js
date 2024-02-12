#!/usr/bin/node
if (isNaN(process.argv[2])) {
    console.log("Missing number of occurrences");
  } else {
    for (let iter = 0; iter < parseInt(process.argv[2]); iter++) {
      console.log("C is fun");
    }
  }
