'use strict';

var submitButton = document.querySelector('.submit-button');
var addButton = document.querySelector('.add-button');
var deleteButton = document.querySelector('.delete-button');
var todoInput = document.querySelector('.todo-input');

submitButton.addEventListener('click', function () {
  postItemToServer(todoInput.value, refresh)
});

addButton.addEventListener('click', function () {
  updateItemOnServer(todoInput.value, refresh)
});

deleteButton.addEventListener('click', function () {
  deleteItemFromServer(todoInput.value, refresh)
});
