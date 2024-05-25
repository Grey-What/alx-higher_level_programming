#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const options = {
  url: `${apiUrl}`,
  json: true
};

request.get(options, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const completedTask = {};
    body.forEach((todo) => {
      if (todo.completed) {
        if (!completedTask[todo.userId]) {
          completedTask[todo.userId] = 1;
        } else {
          completedTask[todo.userId] += 1;
        }
      }
    });
    console.log(completedTask);
  }
});
