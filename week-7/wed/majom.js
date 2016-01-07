'use strict';

var pics = [
  'http://lorempixel.com/image_output/abstract-q-c-640-480-5.jpg',
  'http://lorempixel.com/image_output/abstract-q-c-640-480-4.jpg',
  'http://lorempixel.com/image_output/abstract-q-c-640-480-8.jpg',
  'http://lorempixel.com/image_output/abstract-q-c-640-480-9.jpg',
  'http://lorempixel.com/image_output/abstract-q-c-640-480-4.jpg',
  'http://lorempixel.com/image_output/abstract-q-c-640-480-2.jpg',
  'http://lorempixel.com/image_output/abstract-q-c-640-480-7.jpg',
  'http://lorempixel.com/image_output/abstract-q-c-640-480-10.jpg',
  'http://lorempixel.com/image_output/abstract-q-c-640-480-3.jpg',
  'http://lorempixel.com/image_output/abstract-q-c-640-480-6.jpg',
];

var rightbutton = document.querySelector('.rightbutton');
var leftbutton = document.querySelector('.leftbutton');
var changepics = document.querySelector('.changepics');

var i = 0

leftbutton.addEventListener('click', function (){
  i -= 1
  if (i > 0 && pics.length - 1 > i) {
    changepics.setAttribute('src', pics[i]);
} else {
  i = pics.length - 1
  changepics.setAttribute('src', pics[pics.length - 1]);
  }
});

rightbutton.addEventListener('click', function (){
  i += 1
  if (i > 0 && pics.length - 1 > i) {
    changepics.setAttribute('src', pics[i]);
} else {
  i = 0
  changepics.setAttribute('src', pics[i]);
  }
});
