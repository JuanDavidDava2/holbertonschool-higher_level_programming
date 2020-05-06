#!/usr/bin/node
// Script that prints x times C is fun

const arg = parseInt(process.argv[2]);
let i;

if (Number.isInteger(arg)) {
  for (i = 0; i < arg; i++) { 
      console.log('C is fun'); }
} else {
  console.log('Missing number of occurrences');
}
