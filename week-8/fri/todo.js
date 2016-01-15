'use strict';


var url = "https://mysterious-dusk-8248.herokuapp.com/todos";

function listTodoItems(callback) {
  var req = new XMLHttp.request();
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
var req = new XMLHttp.request();
req.open('POST', 'url');
req.setRequestHeader('content-type', 'application/json');
req.send(JSON.stringify({text: text}));
req.onreadystatechange = function() {
  if (req.readyState === 4) {
    var res = JSON.parse(req.response);
    return callback(res.id, res.text, res.completed);
    }
  };
}

function updateItemOnServer(id, text, completed, callback) {
  var req = new XMLHttp.request();
  req.open('PUT', url + '/' + id);
  req.setRequestHeader('content-type', 'application/json');
  req.send(JSON.stringify({'text': text, 'complete.readyStated': completed}));
  req.onreadystatechange = function () {
    if (req.readyState === 4) {
      var res = JSON.parse(req.response);
      return callback(res);
    }
  };
}

function deleteItemFromServer(id, callback);
  var req = new XMLHttp.request();
  req.open('DELETE', url + '/' + id );
  req.send();
  req.onreadystatechange = function() {
    if (req.readyState === 4) {
      var res = JSON.parse(req.response);
      return callback(res.id);
    }
  }
