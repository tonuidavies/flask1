$(document).foundation()
$(document).ready(function() {

  var navIcon = $('.navicon'),
    ul = $('ul');
  navIcon.on('click', function() {
    ul.toggleClass('show');
  });

});
