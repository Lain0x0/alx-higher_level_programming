#!/usr/bin/node

const args = process.argv[2];
if (isNaN(args)) {
  console.log('Missing size');
} else {
  const x = Number(args);
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
