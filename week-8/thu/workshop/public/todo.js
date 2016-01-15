'use strict';


var url = "http://localhost:3000/todos";

function listTodoItems(callback) {
  var req = new XMLHttpRequest();
  req.open('GET', url);
  req.send();
  req.onreadystatechange = function () {
    if (req.readyState === 4) {
      var items = JSON.parse(req.response);
      return callback(items);
    }
  };
}

function postItemToServer(text, callback) {
var req = new XMLHttpRequest();
req.open('POST', url);
req.setRequestHeader('Content-Type', 'application/json');
req.send(JSON.stringify({'text': text}));
req.onreadystatechange = function() {
  if (req.readyState === 4) {
    var res = JSON.parse(req.response);
    return callback('ok');
    }
  };
}

function updateItemOnServer(id, text, completed, callback) {
  var req = new XMLHttpRequest();
  req.open('PUT', url + '/' + id);
  req.setRequestHeader('Content-Type', 'application/json');
  req.send(JSON.stringify({'text': text, 'complete.readyStated': completed}));
  req.onreadystatechange = function () {
    if (req.readyState === 4) {
      var res = JSON.parse(req.response);
      return callback(res);
    }
  };
}

function deleteItemFromServer(id, callback) {
  var req = new XMLHttpRequest();
  req.open('DELETE', url + '/' + id );
  req.send();
  req.onreadystatechange = function() {
    if (req.readyState === 4) {
      var res = JSON.parse(req.response);
      return callback(res.id);
    }
  }

};

var listCallback = function (response) {
  response.forEach(function(todoItem){
    var newTodoItem = document.createElement('p');
    newTodoItem.innerText = todoItem.text;
    document.querySelector('.todo-container').appendChild(newTodoItem);
  });
}

var refresh = function () {
  document.querySelector('.todo-container').innerHTML = '';
  listTodoItems(listCallback);

}

refresh();
