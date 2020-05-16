#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    let r = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (c) {
          r += c;
        } else {
          r += 'X';
        }
      }
      if (i < this.height - 1) {
        r += '\n';
      }
    }
    console.log(r);
  }
}
module.exports = Square;
