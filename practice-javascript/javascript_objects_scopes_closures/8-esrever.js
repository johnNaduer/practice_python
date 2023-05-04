#!/usr/bin/node

exports.esrever = function (list)
{
let n = list.length
let y = 1
let dato = []
for (let i = 0; i < n ; i++)
{
 dato[n - y] = list[i]
y = y + 1  
}
return dato
}
