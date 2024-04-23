#!/usr/bin/node

const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i = 0;
    while (i < this.height) {
      let j = 0;
      let char = '';
      while (j < this.width) {
        char += c;
        j++;
      }
      console.log(char);
      i++;
    }
  }
}

module.exports = Square;
