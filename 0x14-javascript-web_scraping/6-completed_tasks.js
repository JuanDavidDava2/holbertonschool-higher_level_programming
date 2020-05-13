#!/usr/bin/node
/* Get request and computes the number of tasks completed by user id */
const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) throw err;
  const lis = {};
  const results = JSON.parse(body);

  for (let i = 0; i < results.length; i++) {
    const userId = results[i].userId;
    if (results[i].completed === true) {
      if (userId in lis) lis[userId]++;
      else lis[userId] = 1;
    }
  }
  console.log(lis);
});
