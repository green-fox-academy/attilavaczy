'use strict';


function Student() {
  this.grade = [];
  this.addGrade = function(grade) {
    this.grade.push(grade);
  }
  this.getAverage = function() {
    return this.sum() / this.grade.length;
  }

  this.sum = function() {
    return this.grade.reduce(function(acc, num) {
      return acc + num;
    }, 0);
  }
}



var jozsi = new Student();
jozsi.addGrade(4);
jozsi.addGrade(3);
jozsi.addGrade(5);
jozsi.addGrade(5);
console.log(jozsi.getAverage()); //4.25
