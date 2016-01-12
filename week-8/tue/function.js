'use strict';



var button = document.querySelector('button');

button.addEventListener('click', function() {
  shout('kacsa');
});


function shout(word) {
  alert('ajajajajajaj');
  alert('ajajajajajaj');
  alert('ajajajajajaj', word);
  alert('ajajajajajaj');
  alert('ajajajajajaj');
};




var human = {
  word: ['Kacsa', 'Macska', 'Mammlasz']
  name: 'Tibbor'
  speak: speak
}

function speak(){
  var _this = this;
  this.word.forEach(function(w){
    console.log('I am' + this.name);
    console.log('blabla' + this.w[i]);
  });
}

human.speak();
