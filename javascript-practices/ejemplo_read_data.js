#!/usr/bin/node

fs = require('fs');

const filepath = 'ejemplito.txt';
const contenido = 'aqui tengo mis memorias';

fs.writeFile(filepath, contenido, 'utf-8', function(error)
{
if (error)
  {
  return console.log(error);
  }
console.log('el contenido se a guardado correctamente en ' + filepath);
}
);

