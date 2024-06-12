// Script that update text color of an HTML Tag #8
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
  $('DIV#character').text(data.name);
});
