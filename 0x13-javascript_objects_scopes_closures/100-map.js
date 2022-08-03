#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map((x, index) => x * index);

consle.log(list);
consle.log(newList);
