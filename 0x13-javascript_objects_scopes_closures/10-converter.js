#!/usr/bin/node
// converts a number to specified base

exports.converter = function (base) {
  function myConverter (num) {
    return (num.toString(base));
  }
  return myConverter;
};
