#!/usr/bin/node
// add two integers received from argument
function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

add(Number(process.argv[2]), Number(process.argv[3]));
