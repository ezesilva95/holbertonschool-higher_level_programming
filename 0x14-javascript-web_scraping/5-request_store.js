#!/usr/bin/node

const axios = require('axios');
const fs = require('fs');
const url = process.argv[2];
const file_path = process.argv[3];

axios.get(url)
  .then(response => {
    const content = response.data;
    fs.writeFile(file_path, content, err => {
      if (err) {
        console.error(err);
      }
    });
  });
