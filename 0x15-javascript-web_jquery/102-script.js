// Script that update an HTML Tag #13
$(document).ready(() => {
  $('INPUT#btn_translate').on('click', () => {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
    const lang = $('INPUT#language_code').val();
    $.get(url + lang, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
