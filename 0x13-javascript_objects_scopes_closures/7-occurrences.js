#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nbOccurences = 0;
  let i = 0;
  while (i < list.length) {
    if (searchElement === list[i]) {
      nbOccurences++;
    }
    i++;
  }
  return nbOccurences;
};
