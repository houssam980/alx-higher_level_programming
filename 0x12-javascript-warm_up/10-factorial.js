#!/usr/bin/node

#!/usr/bin/node
function factor(n) {
    if (n === 1) {
      return 1;
    } else {
      return n * factor(n - 1);
    }
  }

  if (isNaN(process.argv[2])) {
    console.log(1);
  } else {
    console.log(factor(parseInt(process.argv[2])));
  }
