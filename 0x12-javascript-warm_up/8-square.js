#!/usr/bin/node
// Script that prints a square

const arg = parseInt(process.argv[2]);
let i, j;
let val = '';

if (Number.isInteger(arg)) {
  for (i = 0; i < arg; i++) {
    for (j = 0; j < arg; j++) {
      val += 'X';
    }
    if (i < arg - 1) {
      val += '\n';
    }
  }
  console.log(val);
} else {
  console.log('Missing size');
}
