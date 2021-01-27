// fix visual filters on top when scrolling
// credits: https://stackoverflow.com/questions/1216114/how-can-i-make-a-div-stick-to-the-top-of-the-screen-once-its-been-scrolled-to
$(window).scroll(function(e){
    var $el = $('.dsk-visual-filters');
    var isPositionFixed = ($el.css('position') == 'fixed');
    if ($(this).scrollTop() > 100 && !isPositionFixed){
        $el.css({'position': 'fixed', 'top': '130px'});
    }
    if ($(this).scrollTop() < 100 && isPositionFixed){
        $el.css({'position': 'static', 'top': '0px'});
    }
});

// on click, scroll to the top 
$(".scroll-to-top").on("click", function() {
    $("html").scrollTop(0);
});