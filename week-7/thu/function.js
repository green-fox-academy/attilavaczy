'use strict'

function greet(name) {
  console.log('csaa ' + name)
}

greet('att');


var koszontes = greet;

koszontes('Gyuri');

var print = console.log;

function greeter(name, log) {
    log('csovi ' + name);
}

greeter('Lajoskam', print)


var add = function (a, b) { return a + b };

console.log(add(1, 2));
