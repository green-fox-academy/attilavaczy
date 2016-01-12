'use strict';

var candyNumber = 0;
var lollypopNumber = 0;
var speedNumber = 0;
var addLollypop = document.querySelector('.buyLollypops');
var addCandy = document.querySelector('.createCandies');
var changeCandyNumber = document.querySelector('.candies');
var changeLollypopNumber = document.querySelector('.lollypops');
var changeSpeed = document.querySelector('.speed');

addCandy.addEventListener('click', function() {
    candyNumber++
    changeCandyNumber.innerHTML = candyNumber
});

addLollypop.addEventListener('click', function() {
  if (candyNumber >= 10) {
    candyNumber = candyNumber - 10
    lollypopNumber++
    changeLollypopNumber.innerHTML = lollypopNumber
    changeCandyNumber.innerHTML = candyNumber
  }
  changeSpeed.innerHTML = Math.floor(lollypopNumber / 10)
});

  var interval = setInterval(function() {
    candyNumber += Math.floor(lollypopNumber / 10);
    changeCandyNumber.innerHTML = candyNumber;
  }, 1000)
