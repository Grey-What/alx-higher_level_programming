#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;
let count = 0;
const options = {
  url: `${apiUrl}`,
  json: true
};

request.get(options, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    body.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
