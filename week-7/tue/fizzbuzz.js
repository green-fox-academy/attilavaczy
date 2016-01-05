'use strict';

for (var c = 1; c <= 100; c+= 1) {
  if (c % 3 === 0 && c % 5 === 0) {
    console.log('fizzbuzz')
  } else if (c % 3 === 0) {
    console.log('fizz');
  } else if (c % 5 === 0 ) {
    console.log('buzz');
  } else {
    console.log(c)
  }
}
