#!/usr/bin/node
const request = require('request');
const cheerio = require('cheerio');

// URL de la página web que queremos extraer
const url = 'https://www.example.com';

// Realizamos la petición GET a la página web
request(url, (error, response, html) => {
  if (!error && response.statusCode == 200) {
    // Cargamos el HTML de la página web en la biblioteca cheerio
    const $ = cheerio.load(html);

    // Extraemos el título de la página web
    const title = $('title').text();

    // Imprimimos el título en la consola
    console.log(title);
  }
});
