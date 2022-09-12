#!/usr/bin/node

const axios = require('axios');
const url = process.argv[2];

axios.get(url)
  .then(response => {
    let count = 0;
    const movies = response.data.results;
    for (const i in movies) {
      const characters = movies[i].characters;
      for (const j in characters) {
        if (characters[j].includes('18')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  })
  .catch(error => {
    console.log(error.response.status);
  });
