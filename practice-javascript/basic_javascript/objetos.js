#!/usr/bin/node
//respecto este codigo:
const persona1 = {
  nombre: "Juan",
  apellido: "Perez",
  edad: 20,
  esMayorEdad: function () {
    if (this.edad >= 18) {
      console.log(this.nombre + " es mayor de edad")
    }
  },
  mostrarNombreCompleto: function () {
    console.log(this.nombre + ", " + this.apellido)
  }
}
persona1.esMayorEdad()

/*
// esto mostrara un error sintactico
const persona2 = {
  nombre: "Juan",
  apellido: "Perez",
  edad: 20,
  mostrarNombre: function () {
    console.log(nombre)
  }
}
persona2.mostrarNombre()
*/
