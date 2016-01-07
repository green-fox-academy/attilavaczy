'use strict';

var kids = [
  {name: 'Tibor', candies: 9},
  {name: 'Luluka', candies: 3},
  {name: 'Nyeree', candies: 0},
  {name: 'Jskdms', candies: 4},
  {name: 'Herion', candies: 3},
  {name: 'Julika', candies: 10}
];

function getRichestKidsName(kids) {
  var richestkid = kids[0];
  for (var i = 0; i < kids.length; i++) {
    if (kids[i].candies > richestkid.candies)
      richestkid = kids[i]
  }
  return richestkid.name;
}

console.log(getRichestKidsName(kids)); //Julikakell
