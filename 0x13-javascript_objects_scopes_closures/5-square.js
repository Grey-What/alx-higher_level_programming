#!/usr/bin/node
// class square that defines a square and inherits form rectangle

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}

module.exports = Square;
