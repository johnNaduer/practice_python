#!/usr/bin/node

let argv = process.argv
let x;
let y;
let len = argv.length
console.log(len)

if (argv.length === 4)
{
argv[4] = argv[3]
argv[3] = ' is '
}
else
{
if (argv.length == 3)
{
argv[3] = ' is '
argv[4] = y
}
else
{
if (argv.length == 2)
{
argv[2] = x
argv[3] = ' is '
argv[4] = y
}
}
}
console.log(argv[2] + argv[3] + argv[4]);
