#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
const options = {
  url: `${apiUrl}`,
  json: true
};

request.get(options, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    for (let i = 0; i < body.results.length; i++) {
      if (body.results[i].characters.includes(characterUrl)) {
        count++;
      }
    }
    console.log(count);
  }
});
