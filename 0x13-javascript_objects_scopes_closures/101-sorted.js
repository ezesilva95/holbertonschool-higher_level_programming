#!/usr/bin/node

const dict = require('./101-data').dict;

const nDic = {};
for (const key in dict) {
  if (nDic[dict[key]] === undefined) {
    nDic[dict[key]] = [];
  }
  nDic[dict[key]].push(key);
}

console.log(nDic);
