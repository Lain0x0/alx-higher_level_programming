#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const Newdict = {};

let j = 0;
while (j < valsUniq.length) {
  const list = [];
  let k = 0;
  while (k < totalist.length) {
    if (totalist[k][1] === valsUniq[j]) {
      list.unshift(totalist[k][0]);
    }
    k++;
  }
  Newdict[valsUniq[j]] = list;
  j++;
}

console.log(Newdict);
