#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i += 1) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    this.height = [this.width, (this.width = this.height)][0];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
