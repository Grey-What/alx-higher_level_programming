#!/usr/bin/node
/*
function returns number of occurence of a number in a list

Args:
list: list of numbers
searchElement: element to search for
*/

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return (count);
};
