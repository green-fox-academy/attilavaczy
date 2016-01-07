'use strict';

var benaSzavak = [
  'kuty',
  'macs',
  'alm',
  'kacs'
];

var faszaSzabak = [];
benaSzavak.forEach(function(szo) {
  faszaSzabak.push(szo + 'a');
});

console.log(faszaSzabak)


var faszaSzabak3 = benaSzavak.map(function(szo) {
  return szo + 'a';
});

console.log(faszaSzabak3);
