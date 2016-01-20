'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];




function groupBySex (kids) {
  var kidGenderSort = {female: [], male: []};
  kids.forEach(function (kid) {
    kidGenderSort[kid.sex].push(kid);
  });
  return kidGenderSort;
}


console.log(groupBySex(kids));
