#!/usr/bin/node

class Articulo {
  constructor(codigo, descripcion, precio) {
    this.codigo = codigo
    this.descripcion = descripcion
    this.precio = precio
  }
}

const articulo1 = new Articulo(1, "Pizza", 100)
console.log(articulo1.descripcion)


class Articulo2 {
  constructor(codigo, descripcion, precio) {
    this.codigo = codigo
    this.descripcion = descripcion
    this.precio = precio
  }

  aumentarPrecio(porcentaje) {
    this.precio = this.precio * (1 + porcentaje / 100)
  }

}

const articulo2 = new Articulo2(1, "Pizza", 100)
articulo2.aumentarPrecio(20)
console.log(articulo2.precio)




