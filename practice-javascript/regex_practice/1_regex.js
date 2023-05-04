#!/usr/bin/node

let dato = "que tal peru";
let testregex = /peru/;
let result = testregex.test(dato);
console.log(result);

let dato2 = "hola mirella como te encuentras";
let search = /mirella/;
let result2 = search.test(dato2);
console.log(result2);
