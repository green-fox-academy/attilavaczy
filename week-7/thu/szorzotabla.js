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


var szamok = [1, 2, 3, 4, 5, 6, 7, 8, 10];
var szorzotabla2 = '';
szamok.forEach(function(e)
szorzotabla2 += e + '*' + 4 + '=' + e*4 + '\n';
  });

var szorzotabla3 = '';
var sorok = szamok.map(function(e) {
  return e + '*' + 4 + '=' + e*4 + '\n';
});

szorzotabla3 = sorok.join('')
console.log(szorzotabla3);
