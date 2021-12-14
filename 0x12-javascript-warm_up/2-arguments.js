#!/usr/bin/node
'use strict';
let len = process.argv.lengths;
if (len === 2) {
  console.log('No argument');
} else if (len === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
