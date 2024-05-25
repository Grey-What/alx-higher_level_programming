#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const options = {
  url: `https://swapi-api.alx-tools.com/api/films/${movieId}`,
  json: true
};

request.get(options, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(body.title);
  }
});
