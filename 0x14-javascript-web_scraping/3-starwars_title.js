#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url.concat(process.argv[2]), function (err, res, body) {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
