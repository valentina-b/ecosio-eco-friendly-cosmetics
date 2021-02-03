$(document).ready(function() {
    // close registration prompt
    $("#close-prompt").on("click", function() {
        $("#registration-prompt").addClass('d-none');
   });
    // collapse burger menu after clicking
    $('.navbar-nav>li>a, .navbar-nav>li>button, .top-nav-links>li>a').on('click', function(){
        $('.navbar-collapse').collapse('hide');
    });
});