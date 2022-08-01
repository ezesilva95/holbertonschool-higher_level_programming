#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = num; i > 0; i -= 1) {
    console.log('C is fun');
  }
}
