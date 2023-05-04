#!/usr/bin/node

//function imprimir
function present()
{
console.log('hola mundo!!!')
}
present()

//function sumar
function sumar()
{
let num1 = 10
let num2 = 20
console.log(num1 + num2)
}
sumar()

function tabla5() {
  const tabla = []
  for (let i = 1; i <= 10; i++) {
    tabla.push(5*i)
  }
  console.log(tabla)
}

tabla5()

//Si bien no es aconsejable, podemos acceder a una variable definida fuera de una función.
let altura=10

function imprimirAltura() {
  console.log(altura)
}
imprimirAltura()

//Por supuesto que una variable definida dentro de una función no se puede acceder en otra función. Genera un error.
/*
function function1()
{
let altura3 = 100
}

function function2()
{
console.log(altura3)
}
function2()
*/

function fun1()
{
let date1 = 5
fun2()
}
function fun2()
{
let date2 = 7
console.log(date2)
}
fun1()

sum2()
function sum2()
{
let sum = 2+3
console.log(sum)
}

//funcion con parametros
function adition (x, y)
{
const su = x + y
console.log(su)
}
adition(2, 5)

/*
Los parámetros son datos que llegan a la función para que pueda cumplir su objeto.
En el ejemplo anterior pasamos directamente los valores, pero los datos pueden estar almacenados en variables.
*/
function sr(x, y) {
  let s = x + y
  console.log(s)
}

const valor1 = 10
const valor2 = 20
sr(valor1, valor2)

/*
 Algo sumamente importante cuando pasamos una variable numérica, string o boolean,
 es que se hace una copia del valor que se almacena en el parámetro. Luego si modificamos 
 el valor del parámetro en la función, el valor de la variable que le pasamos no se modifica.
La variable definida fuera de la función y el parámetro pueden tener el mismo nombre.
 */
function intentarCambiar(x) {
  x = 100
}

let x = 1
intentarCambiar(x)
console.log(x)

/*
Si cuando llamamos a una función no le 
pasamos el dato al parámetro, el mismo queda 
inicializado con el valor undefined.
*/

function mostrar(titulo) {
  console.log(titulo)
}

mostrar()

/*
Los resultados de nuestro algoritmo puden ser impredecibles si no 
pasamos valores a los parámetros. Sumar dos valores 
undefined da un resultado NaN.
*/

function sumar(valor1,valor2) {
  const suma=valor1+valor2
  console.log(suma)
}
sumar()

/*
Si sumamos un valor numérico y un string, el resultado es un string.
*/

function sumar(valor1,valor2) {
  const suma=valor1+valor2
  console.log(suma)
}

sumar(10)

/*
Si sumamos un valor numérico y un string, el resultado es un string.
*/
function sumar(valor1,valor2) {
  const suma=valor1+valor2
  console.log(suma)
}

sumar(10,'Hola')

/*
En JavaScript si sumamos un valor numérico y el valor true, 
luego true se transforma en 1, en cambio false en 0.
*/

function sumar(valor1,valor2) {
  const suma=valor1+valor2
  console.log(suma)
}

sumar(10, true)

function operar() {
  const op=true + true + false - true
  console.log(op)
}

operar()



