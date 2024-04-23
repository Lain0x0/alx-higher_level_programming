#!/usr/bin/node

const Rectangle = require('./5-square.js');
class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const i = 0;
    while (i < this.width) {
      let j = 0;
      let char = '';
      while (j < this.height) {
        char += 'X';
        j++;
      }
      console.log(char);
    }
  }
}
module.exports = Square;
