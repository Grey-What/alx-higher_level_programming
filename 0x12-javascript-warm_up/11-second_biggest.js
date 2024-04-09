#!/usr/bin/node
// search for second biggest integer in list

function second (intArray) {
  let i = 2;

  while (intArray[i]) {
    i++;
  }

  if (i <= 2) {
    return (0);
  } else {
    let max = intArray[2];
    let next = 0;
    let j = 2;
    while (intArray[j]) {
      j++;
      if (intArray[j] > max) {
        next = max;
        max = intArray[j];
      } else if (intArray[j] < max && intArray[j] > next) {
        next = intArray[j];
      }
    }
    return (next);
  }
}

console.log(second(process.argv));
