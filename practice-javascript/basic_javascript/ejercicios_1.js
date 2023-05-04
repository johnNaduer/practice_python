#!/usr/bin/node

console.log("hola mundo");

let v1 = 4;
let v2 = 3;
let suma = v1 + v2;
console.log(suma);

let valor = 10;
valor = 11;


let lado = 4;
let superficie = lado*lado;
console.log(superficie);

// si queres que se mantenga con el tiempo podemos usar const
const pi = 3.14;
let superficie2 = 2*2*pi;
console.log(superficie2);

//ejemplo de usar const que fallara
/*
const pi2 = 3.14;
pi2 = 3.17;
*/

let valor1 = 10;
let valor2 = 20;
let suma2 = valor1 - valor2;
console.log(suma2);


//si no le damos valor a una variable nos dara undefined
let base
console.log(base)

/*
// si no definimos una constante nos dara error
const pi;
console.log(pi);
*/

let num1 = 3;
let num2 = 4;
console.log(num1 + num2);

let distancia1 = 100
let distancia2 = 10
let dias = 4
let total = distancia1 + distancia2 * dias
console.log(total)

let inicio = 10;
let fin = 2;
let result = inicio + fin**2;
console.log(result);
