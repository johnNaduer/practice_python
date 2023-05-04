#!/usr/bin/node

async function recuperarUsuarios() {
  const datos = await fetch('https://jsonplaceholder.typicode.com/users')
  const usuarios = await datos.json()
  const usuariosConPunto = usuarios.map(usuario => usuario.username)
                                   .filter(nombre => nombre.includes("."))
  console.log(usuariosConPunto)
}

recuperarUsuarios()
