'use strict';

function runIn5Secons (callback) {
  setTimeout(callback, 5000);
}



runIn5Secons(function (callback) {
  console.log('jee');
});


//callback roviditve cb usually
