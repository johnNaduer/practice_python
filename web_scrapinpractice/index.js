#!/usr/bin/node
const cheerio = require('cheerio');
const request = require('request-promise');
/* estas primerias lineas serviran apra el web scraping */

async function init() {
const $ = await request({
  uri: 'http://quotes.toscrape.com/',
  transform: body => cheerio.load(body)
})
const websiteTitle = $('head');
console.log(websiteTitle.text());
}
init();
/* la function init la que arancara todo el srcipt  tendre todos los datos del script*/

