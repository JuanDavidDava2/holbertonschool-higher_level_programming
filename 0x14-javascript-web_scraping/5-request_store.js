#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, res, body) {
  if (err) throw err;
  fs.writeFile(process.argv[3], body, err => {
    if (err) throw err;
  });
});
