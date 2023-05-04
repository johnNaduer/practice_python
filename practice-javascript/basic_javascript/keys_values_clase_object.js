#!/usr/bin/node

const punto1 = {
  x: 10,
  y: 5
}

console.log(Object.keys(punto1))

const persona1 = {
  nombre: "Juan",
  apellido: "Perez",
  edad: 20,
  direccion: "Colon 1234",
  telefono: 4567234
}

const valores = Object.values(persona1)
console.log(valores)

const punto2 = {
  x: 10,
  y: 5
}

const claveValor = Object.entries(punto2)
console.log(claveValor)
console.log(claveValor[0])
console.log(claveValor[1])

const sueldos = {
  juan: 100,
  pedro: 300,
  maria: 500
}

let suma = 0
Object.values(sueldos).forEach(sueldo=> suma += sueldo)

console.log(suma)
