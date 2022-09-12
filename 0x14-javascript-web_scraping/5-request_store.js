#!/usr/bin/node

const axios = require('axios');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];

axios.get(url)
  .then(response => {
    const content = response.data;
    fs.writeFile(filepath, content, err => {
      if (err) {
        console.error(err);
      }
    });
  });
