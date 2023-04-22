#!/usr/bin/node
const request = require('request');
const cheerio = require('cheerio');

request('https://www.bbc.com/news', function(error, response, html) {
  if (!error && response.statusCode == 200) {
    const $ = cheerio.load(html);
    const headlines = $('a.gs-c-promo-heading');
    headlines.each(function() {
      console.log($(this).text().trim());
    });
  } else {
    console.log(error);
  }
});
