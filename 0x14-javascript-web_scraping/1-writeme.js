t fss = require('fs');
fss.writeFile(process.argv[2], process.argv[3], err => {
  if (err) {
    console.log(err);
  }
});
