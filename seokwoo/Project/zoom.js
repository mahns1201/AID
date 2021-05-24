$(document).ready(function() {
    $(document).on('click', '#Seoul',
    function() {
        var main1x = document.getElementById('korea');
        TweenMax.to(main1x, 0.7, {
            scale: 2.6,
            x: -843,
            y: -255.47,
            ease: Power1.easeInOut,
            transformOrigin: "50% 50%"
        })
    })
})