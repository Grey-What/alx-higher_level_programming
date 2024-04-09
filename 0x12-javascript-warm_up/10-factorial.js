#!/usr/bin/node
// factorial from argument

function factorial (argVal) {
  if (isNaN(argVal) || argVal === 1) {
    return (1);
  } else {
    return (argVal * factorial(argVal - 1));
  }
}

console.log(factorial(parseInt(process.argv[2])));
