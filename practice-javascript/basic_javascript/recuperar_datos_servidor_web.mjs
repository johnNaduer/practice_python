#!/usr/bin/node

const fetch = require('node-fetch').default;

async function recuperarRubros() {
  const datos = await fetch('https://www.scratchya.com.ar/apifetch/recuperarrubros.php');
  const rubrostxt = await datos.text();
  const rubrosobj=JSON.parse(rubrostxt);
  console.log(rubrosobj.length);
}

recuperarRubros();

