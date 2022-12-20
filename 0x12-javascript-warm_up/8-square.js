#!/usr/bin/node

let size = parseInt(process.argv[2]);
if (isNaN(size) || process.argv[2] === undefined) {
  console.log('Missing size');
}
let sqstr = 'X';
for (let i = 0; i < size - 1; i++) {
  sqstr += 'X';
}
while (size > 0) {
  console.log(sqstr);
  size--;
}
