$(document).ready(function() {
  // Asignar el evento de clic a los elementos <div> con la clase "card"
  $('.card').on('click', function() {
    var disponibilidad = $(this).data('value');

    // Cambiar el color de fondo según la disponibilidad
    if (disponibilidad === 'disponible') {
      $(this).css('background-color', 'green'); // Cambiar a verde si está disponible
    } else {
      $(this).css('background-color', 'red'); // Cambiar a rojo si no está disponible
    }
  });
});

