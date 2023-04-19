#!/usr/bin/node
const fs = require('fs');

const argv = process.argv;
const filepath = argv[2];

fs.readFile(filepath, 'utf-8', function verify(e, dato){
if (e)
{
   console.log(e);
}
  else
{
console.log(dato);
}
  
});

