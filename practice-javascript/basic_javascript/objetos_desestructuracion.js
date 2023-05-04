#!/usr/bin/node

/*
https://caniuse.com/#feat=destructuring"
*/
const articulo1 = {
  codigo: 1,
  descripcion: 'Sandia',
  precio: 12.55,
  stock: 10
}

const { codigo, ...articulo } = articulo1
console.log(articulo)

const empleado1 = {
  dni: 12345678,
  nombre: 'Juan',
  apellido: 'Perez',
  sueldos: [1000, 2000, 3000]
}

const { dni, apellido, ...datosEmpleado1 } = empleado1
console.log(datosEmpleado1)

const inmueble1 = {
  codigo: 1,
  direccion: 'Colon 101',
  precio: 100000,
  tipo: 'casa',
  posicion: {
    lat: 6.44,
    lng: 2.35
  }
}

const { posicion, ...parteInmueble } = inmueble1
console.log(posicion)
