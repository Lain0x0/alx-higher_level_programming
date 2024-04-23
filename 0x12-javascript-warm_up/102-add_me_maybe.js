#!/usr/bin/node
exports.addMeFunc = function (number, theFunction) {
  theFunction(++number);
};
