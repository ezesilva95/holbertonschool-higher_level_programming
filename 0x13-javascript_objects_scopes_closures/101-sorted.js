#!/usr/bin/node

const dict = require('./101-data').dict;

let nDic = {};
for (let key in dict) {
  if (nDic[dict[key]] === undefined) {
    nDic[dict[key]] = [];
  }
  nDic[dict[key]].push(key);
}

console.log(nDic);
