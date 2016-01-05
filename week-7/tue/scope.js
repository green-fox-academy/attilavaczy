'use strict';

var g = 123;

function printg() {
  console.log(g);
  g = 333;
}

printg()
console.log(g);


function printLocalG() {
  var g = 7
  console.log(g);
}

printLocalG();
console.log(g);
