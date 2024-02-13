#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let iter = 0; iter < this.height; iter++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const rt = this.width;
    this.width = this.height;
    this.height = rt;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
