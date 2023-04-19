#!/usr/bin/node

const argv = process.argv;

const fs = require('fs');

const filepath = argv[2];

fs.readFile(filepath, 'utf-8', function (err, data)
{
if (err)
{
return console.log(err);
}
else
{
console.log(data);
}
});
