// Ejemplo de código para el archivo script.js

// Obtener referencia al botón del menú hamburguesa
const navbarToggler = document.querySelector('.navbar-toggler');

// Obtener referencia al menú desplegable
const navbarCollapse = document.querySelector('.navbar-collapse');

// Agregar evento clic al botón del menú hamburguesa
navbarToggler.addEventListener('click', function() {
  // Alternar la clase 'show' en el menú desplegable
  navbarCollapse.classList.toggle('show');

  // Añadir/eliminar clase 'vertical' al botón del menú hamburguesa
  navbarToggler.classList.toggle('vertical');
});

