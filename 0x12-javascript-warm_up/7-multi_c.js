#!/usr/bin/node

const args = process.argv[2];
if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  const x = Number(args);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
