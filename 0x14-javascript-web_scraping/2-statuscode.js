#!/usr/bin/node

const request = require('request');

request(process.argv[2], (_err, res) => console.log('code:', res.statusCode); // Print the response status code if a response was received);
