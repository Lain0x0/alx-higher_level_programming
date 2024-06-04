#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (err, status) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + status.statusCode);
  }
});
