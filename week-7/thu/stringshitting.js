'use strict';

function reverse(string) {
  var output = '';
  for (var i = string.length - 1; i >= 0; i--)
    output += string[i];
  return output;
}

console.log(reverse('kutyafasza'));

function reverse2(input) {
    return reverseRecursive(input, input.length - 1);
}


function reverseRecursive(inpit, i) {
  if (i < 0) {
    return '';
  } else {
      return input[i] reverseRecursive(input, i - 1)
    }
}

console.log(reverseRecursive('kacsa', 4));
