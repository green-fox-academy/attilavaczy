'use strict';

function Student() {
  this.grades = {};
  this.addGrade = function(subject, grade) {
  //  if (this.grades[subject] === undefined) {
    if (!(subject in this.grades)) {
      this.grades[subject] = [];
    }
    this.grades.push[subject].push[grade];
  };
  this.getCount = function() {
    var output = {};
    for (var subject in this.grades) {
      output[subject] = this.grades[subject].length;
    }
    return output;
  };

  this.getAverage = function(){
    var sum = 0;
    var count = 0;
    for (var subject in this.grades) {
      this.grades[subject].forEach(function {
        sum += grade;
        count += 1
      });
      return sum / count;
    }
  };
}
/*
  this.addSubject = function(subject) {
    this.naplo.push(subject)
  }

  this.getAverage = function() {
    return this.sum() / this.grade.length
  }
  */

/*
  this.getCount = function() {
    return this.grades.reduce(function(output, grade) {
    if (!(grade.subject in output)) {
    output[grade.subject] = 0;
  }
      output[grade.subject]++;
      return output;
    }, {});
  }*/
}



var dezso = new Student();
dezso.addGrade('matek', 5);
dezso.addGrade('matek', 4);
dezso.addGrade('matek', 4);
dezso.addGrade('rajz', 1);
dezso.addGrade('rajz', 3);
dezso.addGrade('magyar', 4);
console.log(dezso.naplo)
console.log(dezso.naplo[0].subject)
console.log(dezso.getCount()); //'rajz':2, 'matek': 3
/*console.log(dezso.getAverage()); // 3.4*/
//szorgalmi

//dezso.getAverageBySubject() //'matek', 4.3, 'rajz', 2*/
