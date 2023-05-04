#!/usr/bin/node

const add = (a, b) =>
{
c = parseInt(a) + parseInt(b)
return c
}
add(process.argv[2], process.argv[3])
console.log(add(process.argv[2], process.argv[3]))
