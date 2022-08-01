#!/usr/bin/node

const arry = process.argv.slice(2);
function SecndMax (array) {
  if (array.length < 2) {
    return (0);
  } else {
    array.sort((x, y) => x - y);
    array.pop();
    return (array.pop());
  }
}
console.log(SecndMax(arry));
