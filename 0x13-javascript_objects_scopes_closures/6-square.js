#!/usr/bin/node
// class square that defines a square and inherits form rectangle

const Square5 = require('./5-square.js');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let i = 0;
      while (i < this.width) {
        console.log(c.repeat(this.width));
        i++;
      }
    }
  }
}

module.exports = Square;
