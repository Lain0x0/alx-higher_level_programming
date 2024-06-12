// Script that update an HTML Tag #14

$(document).ready(() => {
  $('INPUT#btn_translate').on('click', () => {
    const lang = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
  $('INPUT#language_code').on('keypress', (e) => {
    if (e.which === 13) {
      const lang = $('INPUT#language_code').val();
      $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (data) => {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
