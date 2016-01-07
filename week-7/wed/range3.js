'use strict';

function range(from, to, double) {
  var array = [];
  if (double > 0) {
  for (var i = from; i < to; i+=double) {
    array.push(i);
  }
  return array;
} else if (double < 0) {
  for (var i = from; i < to; i+=double) {
    array.push(i);
  }
}
  return array;
}

console.log(range(4, 8, -1));
