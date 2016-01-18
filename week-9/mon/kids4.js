'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];



/*function getTheLongestNamesAge(kids) {
  var count = 0;
  kids.forEach(function(kid) {
    kid.age = kid.name.length
    count ++
  });
  return count
}*/


/*function getTheLongestNamesAge(kids) {
  var output = kids.name;
  for (var i = 0; i < kids.length; i++) {
      if (kids[i].length > output) {
          output = kids[i].length;
      }
  }
  return output;
}*/


function getTheLongestNamesAge(kids) {
  var kidNameCount = kids[0]
  kids.forEach(function (kid) {
    if (kid.name.length > kidNameCount.name.length) {
      kidNameCount = kid
    }
  });
  return kidNameCount.age;
}


console.log(getTheLongestNamesAge(kids));
