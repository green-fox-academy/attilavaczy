'use strict';

var express = require('express');
var url = require('url');
var bodyParser = require('body-parser');

var items = [
  {id: 1, 'text': 'Do the laundries', 'completed': false},
  {id: 2, 'text': 'Make dinner', 'completed': false},
  {id: 3, 'text': 'Do drugs', 'completed': false},
  {id: 4, 'text': 'Take out the dogs', 'completed': false},
  {id: 5, 'text': 'Make love with your wife or husband', 'completed': false}
]

var bodyItem = function () {
  var idcount = id++ //increase with one
  this.id = idcount
  this.text = ""
  this.completed = false
}


var app = express()
app.get('/todos', function(req, res) {
  res.json(items)
});

app.post('/todos', function(req, res) {
  var item = items.push(req.body);
  req.status(201).json(item);
});

app.listen(3000);
