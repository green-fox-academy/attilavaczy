'use strict';

var kids = [
  {name: 'Tibor', candies: 2},
  {name: 'Steve', candies: 3},
  {name: 'Agoston', candies: 0},
  {name: 'Julika', candies: 7},
  {name: 'Krisztian', candies: 4}
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
