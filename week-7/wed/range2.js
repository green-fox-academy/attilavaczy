'use strict';

var array = range(3, 7);

function range(from, to) {
  var array = [];
  for (var i = from; i < to; i++) {
    array.push(i);
  }
  return array;
}

console.log(array);
