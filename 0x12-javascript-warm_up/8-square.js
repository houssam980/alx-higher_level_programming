#!/usr/bin/node
if (isNaN(process.argv[2])) {
    console.log("Missing size");
  } else {
    for (let iter = 0; iter < parseInt(process.argv[2]); iter++) {
      console.log("X".repeat(parseInt(process.argv[2])));
    }
  }
