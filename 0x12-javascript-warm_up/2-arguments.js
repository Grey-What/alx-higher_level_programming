#!/usr/bin/node
/*
determines if argumnets has been passed to script
*/
let i = 2;

while (process.argv[i]) {
  i++;
}

if (i === 2) {
  console.log('No argument');
} else if (i === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
