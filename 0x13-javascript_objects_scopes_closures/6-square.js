#!/usr/bin/node

class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i += 1) {
        console.log(c.repeat(this.height));
      }
    }
  }
}

module.exports = Square;
