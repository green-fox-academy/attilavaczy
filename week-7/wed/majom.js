'use strict';

var pics = [
  'https://41.media.tumblr.com/84729c469ca431c8c80dad1cd4281205/tumblr_o08zo7SJan1tx21ogo1_540.jpg',
  'http://lorempixel.com/image_output/food-q-c-640-480-8.jpg',
  'http://lorempixel.com/400/200/sports/1/',
  'http://lorempixel.com/g/400/200/',
  'http://lorempixel.com/image_output/food-h-c-640-959-8.jpg',
  'http://lorempixel.com/image_output/cats-h-c-640-959-4.jpg',
  'http://lorempixel.com/image_output/nightlife-h-c-640-959-6.jpg',
  'http://lorempixel.com/image_output/people-q-c-640-460-8.jpg',
  'http://lorempixel.com/image_output/technics-q-c-640-460-9.jpg',
  'http://lorempixel.com/image_output/fashion-q-c-640-460-7.jpg',
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
