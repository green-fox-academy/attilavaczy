'use strict';

var submitButton = document.querySelector('.submit-button');
var addButton = document.querySelector('.add-button');
var deleteButton = document.querySelector('.delete-button');
var todoInput = document.querySelector('todo-input');

submitButton.addEventListener('click', function () {
  var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
  var inputText = todoInput.value;
  var urlWithParams = url + '?inputText=' + encodeURIComponent(inputText);

  createRequest(urlWithParams, onDone);
});

addButton.addEventListener('click', function () {
  var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
  var inputText = todoInput.value;
  var urlWithParams = url + '?inputText=' + encodeURIComponent(inputText);

  createRequest(urlWithParams, onDone);
});

deleteButton.addEventListener('click', function () {
  var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
  var inputText = todoInput.value;
  var urlWithParams = url + '?inputText=' + encodeURIComponent(inputText);

  createRequest(urlWithParams, onDone);
});

todoInput.addEventListener('text', function () {
  var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
  var inputText = todoInput.value;
  var urlWithParams = url + '?inputText=' + encodeURIComponent(inputText);
});
