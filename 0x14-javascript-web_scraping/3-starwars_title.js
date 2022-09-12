#!/usr/bin/node

const axios = require('axios');
const episode = process.argv[2];

axios.get(`https://swapi-api.hbtn.io/api/films/${episode}`)
  .then(response => {
    console.log(response.data.title);
  })
  .catch(error => {
    console.log(error.response.status);
  });
