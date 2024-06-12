// Script that update an HTML Tag #12
$(document).ready(function () {
  $('#add_item').on('click', () => {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('#remove_item').on('click', () => {
    $('UL.my_list li:last-child').remove();
  });
  $('#clear_list').on('click', () => {
    $('UL.my_list').empty();
  });
});
