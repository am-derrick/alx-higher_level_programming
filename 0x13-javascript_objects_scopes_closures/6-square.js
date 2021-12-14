#!/usr/bin/node
const SquareX = require('./5-square.js');

module.exports = class Square extends SquareX (
  charPrint(c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
