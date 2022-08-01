#!/usr/bin/node

exports.callMeMoby = function (x, xfunction) {
  for (let i = 0; i < x; i += 1) {
    xfunction();
  }
};
