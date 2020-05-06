#!/usr/bin/node
// script that computes and prints a factorial
const a = parseInt(process.argv[2]);

function factorial (a) {
  if (process.argv.length <= 2 || a === 0) {
    return 1;
  }
  return (a * factorial(a - 1));
}
console.log(factorial(a));
