#!/usr/bin/node
// movies where the character Wedge Antilles.
const request = require('request');

request.get(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < json.count - 2; i++) {
      if (json.results[i].characters[18]) {
        count += 1;
      }
    }
    console.log(count);
  }
});
