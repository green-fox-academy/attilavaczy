'use strict';

var fs = require('fs');

function getFirstIndexInAlmaText(letter, cb) {
  fs.readFile('Alma.txt', function(err, content) {
    if (err) {
      return cb(err);
    }
    var stringContent = String(content);
    for (var i = 0; i < stringContent.length; i++) {
      if (stringContent[i] === letter) {
        return cb(err, i);
      }
    }
  });
}

getFirstIndexInAlmaText('p', function(err, index) {
  console.log(index);
});
