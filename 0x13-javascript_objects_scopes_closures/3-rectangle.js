#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width > 0 && this.height > 0) {
      let i = 0;
      while (i < this.height) {
        let j = 0;
        let char = '';
        while (j < this.width) {
          char += 'X';
          j++;
        }
        console.log(char);
        i++;
      }
    }
  }
}

module.exports = Rectangle;
