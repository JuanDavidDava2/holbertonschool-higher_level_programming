#!/usr/bin/node
// Display the status code of a GET request.
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
