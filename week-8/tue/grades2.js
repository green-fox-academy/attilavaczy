'use strict';

var grades = [
  {num: 3, subject: 'math'},
  {num: 4, subject: 'math'},
  {num: 5, subject: 'arts'},
  {num: 2, subject: 'sport'},
  {num: 5, subject: 'physics'},
  {num: 4, subject: 'physics'},

];

function countFive(grades) {
  var output = 0 //2
  for (var i = 0; i < grades.length; i++) {
  if (grades[i].num === 5) {
    output ++;
  }

  }
  return output
}

console.log(countFive(grades));


/*grades.forEach(function(grade)) {
if (grade.num ==== 5) {
  count++;
}
});
return count;
}

console.log(countFive(grades));*/
