#!/usr/bin/node

let sueldo = 3000;

if (sueldo > 3000)
{
console.log('debo pagar impuestos');
}
else
{
console.log('no debo pagar impuestos');
}

let clave1 = 'abc123'
if (clave1 == 'abc123')
{
console.log('la clave es correcta')
}
else
{
console.log('la calve es incorrecta')
}

let nota1 = 2
let nota2 = 4
let nota3 = 6
let promedio = (nota1 + nota2 + nota3)/3
if (promedio >= 7)
{
console.log('pasate el curso')
}
else
{
console.log('no pasaste el curso')
}

//sin son strings

let valor1 = '10'
let valor2 = 10

if (valor1 == valor2)
{
console.log('iguales')
}
else
{
console.log('no son iguales')
}


let valorn = '10'
let valorm = 10
if (valorn === valorm) {
  console.log('iguales')
} else {
  console.log('no iguales')
}

let altura1 = '190'
let altura2 = 190
if (altura1 !== altura2)
{
console.log('son distintos')
}
else
{
console.log('son iguales')
}

//Se tiene una variable entera cargada por asignación, mostrar si es positivo, negativo o nulo
let num = -30
if (num === 0) {
  console.log("Nulo")
} else {
  if (num > 0) {
    console.log("Positivo")
  } else {
    console.log("Negativo")
  }
}

// el mayor numero
let num1 = 7
let num2 = 20
let num3 = 5

if (num1 > num2 && num1 > num3)
{
console.log(`${num1} es el mayor`)
}
else
{
if (num2 > num3)
{
console.log(`${num2} es el mayor`)
}
else
{
console.log(`${num3} es el amyor`)
}
}

// encontrar una palabra igual
let palabra = 'private'

if (palabra === "let")
{
console.log('es una palabra clave')
}
else
{
if (palabra === 'if')
{
console.log('era un if')
}
else
{
if (palabra === 'else')
{
console.log('era un else')
}
else
{
console.log('no es una clave')
}
}
}
// 
let dia = 25
let mes = 12
let año = 2023

if (dia === 25 && mes === 12)
{
console.log(`es ${año} y hoy es navidad`)
}
// anidados
let x = 1
let y = -4

if (x > 0 && y > 0)
{
console.log('es primer cuadrante')
}
else
{
if ( x < 0 && y > 0)
{
console.log('es segundo cuadrante')
}
else
{
if ( x < 0 && y < 0)
{
console.log('es tercer cuadrante')
}
else
{
if ( x > 0 && y < 0)
{
console.log('es el cuarto cuadrante')
}
}
}
}
// negacion !
let j = 30

if (!(j > 20))
{
console.log('j es menor a 20')
}
else
{
console.log('j es mayor a 20')
}

//boleanos

let ella = true

if (ella)
{
console.log('ella es la indicada')
}
else
{
console.log('ella no es la indicada')
}

let existe = false
if (!(existe))
{
console.log('afiramtivo es falso')
}
else
{
console.log('es verdadero')
}
