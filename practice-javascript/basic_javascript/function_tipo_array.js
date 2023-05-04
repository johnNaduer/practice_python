#!/usr/bin/node

function cargar(array)
{
let i;
for (i = 0; i <array.length; i++)
{
array[i]
}
}

const arreglo = [0,0,0,0]
cargar(arreglo)
console.log(arreglo)


//array carag e impresion
function cargar(arreglo) {
  arreglo.fill(10)
}

function imprimir(arreglo) {
  console.log(arreglo)
}

const arreglo2 = new Array(5).fill(0)
cargar(arreglo2)
imprimir(arreglo2)

//ordenar arreglos
function cargar(arreglo) {
  arreglo[0] = 10
  arreglo[1] = 80
  arreglo[2] = 2000
  arreglo[3] = 700
  arreglo[4] = 110
}

function orderar(arreglo) {
  arreglo.sort((a, b) => a - b)
}

function imprimir(arreglo) {
  console.log(arreglo)
}

const arreglo4 = new Array(5)
cargar(arreglo4)
orderar(arreglo4)
imprimir(arreglo4)

//obtener el mayor:
function cargar(arreglo) {
  arreglo[0] = 10
  arreglo[1] = 80
  arreglo[2] = 2000
  arreglo[3] = 700
  arreglo[4] = 110
}

function mayor(arreglo) {
  let mayor = arreglo[0]
  for (let i = 1; i < arreglo.length; i++) {
    if (arreglo[i] > mayor) {
      mayor = arreglo[i]
    }
  }
  console.log(mayor)
}

const arreglo3 = new Array(5)
cargar(arreglo3)
mayor(arreglo3)

// una vez seteado con fill no podemos cambiar

function intentarCambiar(arreglo) {
  const arreglo2 = new Array(5).fill(1)
  arreglo = arreglo2
}


const arreglo5 = new Array(5).fill(10)
intentarCambiar(arreglo5)
console.log(arreglo5)
