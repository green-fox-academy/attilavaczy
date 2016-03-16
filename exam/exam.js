'use strict';

var fs = require('fs');
var filename = './kolbasz.json';
var object;
  fs.readFile(filename, function (err, data) {
    if (err) throw err;
      object = JSON.parse(data);
});

function processFile(t) {
  console.log(object);
  setTimeout(function () {
    processFile(t)}, t);
}
  processFile(2000);

function jsonWriter(filename, object) {
var exampleObject = JSON.stringify(object)
    fs.writeFile(filename, exampleObject function (err, data) {
      if (err) throw err;)
}
