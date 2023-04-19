#!/usr/bin/node

const fs = require('fs');
const file_ruta = 'ejemplito2.txt';
const mycontenido = 'aqui tengo algunos datos de python';

fs.writeFile(file_ruta, mycontenido, 'utf-8', function()
{
console.log('se logro guardar con exito en el archivo ' + file_ruta);
}
);
