#!/usr/bin/node
// print number of arguments printed and the new argument

let counter = 0;

exports.logMe = function (item) {
  console.log(`${counter}: ${item}`);
  counter++;
};
