'use strict';

var array = range(5)

function range(number) {
  var array = [];
  for (var i = 0; i < number; i++) {
    array.push(i);
  }
  return array;
}
console.log(array)
