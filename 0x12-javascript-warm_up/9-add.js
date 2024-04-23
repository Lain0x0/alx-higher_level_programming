#!/usr/bin/node

const args = process.argv[2];
const args2 = process.argv[3];

function add (a, b) {
  const result = a + b;
  console.log(result);
}

add(Number(args), Number(args2));
