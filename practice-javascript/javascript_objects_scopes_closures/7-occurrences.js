#!/usr/bin/node

const nbOccurences = (a, b) =>
{
let cant = 0
for (let i = 0; i < a.length; i++)
{
if (a[i] === b)
{
cant = cant + 1  
}
}
return cant  
}

exports.nbOccurences = nbOccurences
