#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
const options = {
  url: `${apiUrl}`,
  json: true
};

request.get(options, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    for (const character of body.characters) {
      request.get(character, { json: true }, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(body.name);
        }
      });
    }
  }
});
