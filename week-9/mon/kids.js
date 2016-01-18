'use strict';
var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];


function getAgeByName() {
  var oldestkid = kids[0]
  for (var i = 0; i < kids.length; i++) {
    if (kids[i].age > oldestkid.age)
    oldestkid = kids[i]
  }
  return oldestkid.age
}

console.log(getAgeByName(kids, 'Gerda'));


function getAgeByName(kids, name) {
  var age = 0;
  kids.forEach(function(kid) {
    if (kid.name === name) {
      age = kid.age;
    }
  })
}
