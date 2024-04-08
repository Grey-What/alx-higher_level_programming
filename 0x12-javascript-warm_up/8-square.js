#!/usr/bin/node
// print a square
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const myNum = Number(process.argv[2]);
  for (let i = 0; i < myNum; i++) {
    console.log('X'.repeat(myNum));
  }
}
