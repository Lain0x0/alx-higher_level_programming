#!/usr/bin/node

const varNum = process.argv[2];
if (isNaN(varNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + varNum);
}
