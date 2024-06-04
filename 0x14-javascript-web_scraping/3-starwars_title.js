#!/usr/bin/node

const request = require('request');
const URL_API = 'https://swapi-api.hbtn.io/api/films/';
request(URL_API + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
