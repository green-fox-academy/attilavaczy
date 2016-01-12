'use strict';

var fs = require('fs');

fs.readFile('kotre.txt', function(err, content) {
  if (err) {
    console.log('para volt');
  } else {
    console.log(content);
  }

})
