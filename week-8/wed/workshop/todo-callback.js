'use strict';


var url = "https://mysterious-dusk-8248.herokuapp.com/todos";
var todoContainer = document.querySelector('.todo-container');

var listCallback = function (response) {
  var todoItems = JSON.parse(response);
  todoItems.forEach(function(todoItem){
    var newTodoItem = document.createElement('p');
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);
  })
}

var refresh = function () {
  createRequest('GET', url, {}, listCallback);
}

refresh();

var newTodo = JSON.stringify({text: 'Menj el a boltba'});
var createTodoCallback = function (response) {
  refresh();
}

'use strict';


function createRequest (method, url, data, callback) {
  var probaRequest = new XMLHttpRequest();
  probaRequest.open(method, url);
  probaRequest.setRequestHeader('Content-Type', 'application/json');
  probaRequest.send(data);
  probaRequest.onreadystatechange = function () {
    console.log('allapot: ', probaRequest.readyState);
    if (probaRequest.readyState === 4) {
      callback(probaRequest.response);
    }
  };
}


createRequest('POST', url, newTodo, createTodoCallback);
