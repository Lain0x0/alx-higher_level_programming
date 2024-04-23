#!/usr/bin/node

let numberarg = 0;

exports.logMe = function (item) {
  console.log(numberarg + ': ' + item);
  numberarg++;
};
