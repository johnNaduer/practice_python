#!/usr/bin/node
/*
Write a class Rectangle that defines a rectangle:

You must use the class notation for defining your class
The constructor must take 2 arguments: w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, create an empty object
Create an instance method called print() that prints the rectangle using the character X

*/

class Rectangle
{
constructor (w, h)
{
if (w <= 0 || h <= 0 || !(Number.isInteger(w)) || !(Number.isInteger(h)))
{
return {}
}
else
{
this.width = w
this.height = h
}
}
print (w, h)
{
let i;
let y;
let d = "#"
for (i = 0; i < this.height; i++)
{
let n = ""
for (y = 0; y < this.width; y++)
{
n = d + n 
}
console.log(n)
}
}
}

module.exports = Rectangle
