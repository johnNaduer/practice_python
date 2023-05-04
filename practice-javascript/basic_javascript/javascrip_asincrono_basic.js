#!/usr/bin/node

const acciones=[]

function temporizador(ms, fn) {
  setTimeout(() => fn(), ms)
}

temporizador(0, () => {
  acciones.push('caminar')
  temporizador(100, () => {
    acciones.push('correr')
    temporizador(100, () => {
      acciones.push('saltar')
      temporizador(100, () => {
        acciones.push('pesas')
        temporizador(100, () => {
          acciones.push('bicicleta')
          console.log(acciones)
        })
      })
    })
  })
})

acciones.push("prepararse")

console.log('Inicio de programa');

setTimeout(function() {
  console.log('Tarea asincrónica terminada');
}, 3000);

console.log('Fin de programa');


let contador = 1
setTimeout(() => contador++, 1000)

console.log(contador)
