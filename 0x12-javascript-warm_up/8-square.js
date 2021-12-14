#!/usr/bin/node
'use strict';
let val - process.argv[2];
if (isNan(val)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < val; i++) {
    console.log('X'.repeat(val));
}
