(function ($) {
    $(function () {
      
      $('.js-carousel').slick({
        infinite: true,
        autoplay: false,
        slidesToShow: 2,
        slidesToScroll: 1,
        prevArrow: '.js-ag-carousel-arrow_prev',
        nextArrow: '.js-ag-carousel-arrow_next',
        responsive: [{
          breakpoint: 1600,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
          {
            breakpoint: 980,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }]
      });
      
  
    });
  })(jQuery);

function playSound(soundFile) {
    console.log("Button clicked! Sound will be played.");
    var audio = document.getElementById('audio');
    audio.src = soundFile;
    audio.play();
}