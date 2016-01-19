'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];

 //{female: 2, male: 3}

function countBySex (kids) {
  var kidGenderCount = {female: 0, male: 0};
  kids.forEach(function (kid) {
    if (kid.sex === 'female') {
      kidGenderCount['female']++;
    }
    if (kid.sex === 'male') {
      kidGenderCount['male']++;
    }
  });
  return kidGenderCount.;
}


function countBySex (kids) {
  var kidGenderCount = {female: 0, male: 0};
  kids.forEach(function (kid) {
    kidGenderCount[kid.sex]++;
  });
  return kidGenderCount.;
}

//ha nem tudjuk mi lesz a szex
function countBySex (kids) {
  var kidGenderCount = {};
  kids.forEach(function (kid) {
    if (kidGenderCount[kid.sex] === undefined) {
      kidGenderCount[kid.sex] = 0;
    }
    kidGenderCount[kid.sex]++;
  });
  return kidGenderCount.;
}

console.log(countBySex(kids));
