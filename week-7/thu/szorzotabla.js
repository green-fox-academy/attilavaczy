'use strict'

function Multiply(number) {
  var output = '';
  for (var i = 1; i < 11; i++) {
    output += i + '*' + number + '=' + number*i + '\n';
  }
  return output;
}

for (var i = 1; i < 10; i++) {
  console.log(Multiply(i))
}
