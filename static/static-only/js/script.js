$(function(){
	"use strict";
	
	
	var scrollOffset = 100;
	
	$(window).on('scroll', function(){
		
		/*=========================================================================
			Change navigation bar from transparent to white
		=========================================================================*/
		if( $(window).scrollTop() < scrollOffset ){
			$('body').removeClass('scrolled');
		}else{
			$('body').addClass('scrolled');
		}
		
		/*=========================================================================
			Navbar ScrollSpy
		=========================================================================*/
		var scrollPos = $(document).scrollTop(),
			nav_height = $('#navbar').outerHeight();
		
		$('.navbar li a').each(function () {
			var currLink = $(this),
				refElement = $(currLink.attr('href'));
			if( refElement.size() > 0 ){
				if ( ( refElement.position().top - nav_height ) <= scrollPos ) {
					$('.navbar li').removeClass('active');
					currLink.closest('li').addClass('active');
				}else{
					currLink.removeClass('active');
				}
			}
		});
		
		
	});
	
	
	//Initialize smoothscroll plugin
	smoothScroll.init({
		updateURL: false
	});
	
	
	/*=========================================================================
		WOW.js initialization
	=========================================================================*/
	new WOW().init({
		mobile: false
	});
	
	
	/*=========================================================================
		Magnific Popup (Project Popup initialization)
	=========================================================================*/
	$('.view-btn').magnificPopup({
		type: 'image',
		mainClass: 'mfp-with-zoom',
		gallery: {
			enabled: true
		},
		zoom: {
			enabled: true,
			duration: 300,
			easing: 'ease-in-out',
			opener: function(openerElement) {
			  return openerElement.is('img') ? openerElement : openerElement.closest('figure').find('img');
			}
		  }
	});
	
	
	/*=========================================================================
		Video Section Video Popup
	=========================================================================*/
	$('.play-btn').magnificPopup({
		type: 'iframe'
	});
	
	
	/*=========================================================================
		Hide Preloader When Page Is Loaded
	=========================================================================*/
	$(window).on('load',function(){
		$('body').addClass('loaded');
	});
	
	
	/*=========================================================================
		Initialize Material Design Ripples
	=========================================================================*/
	Waves.attach('.btn-custom', 'waves-classic');
	Waves.init();
	
	/*=========================================================================
		Screenshots Slider
	=========================================================================*/
	$('.screenshots-slider').owlCarousel({
		center: true,
		loop:true,
		margin:30,
        autoplay:true,
        autoWidth:true,
		responsive:{
			600:{
				items:3,
				startPosition: 1
			},
			0: {
				items:1,
				startPosition: 0
			},
            1200:{
                items:4,
                startPosition: 1
            },
		}
	});
	
	/*=========================================================================
		Testimonials Slider
	=========================================================================*/
	$('.testimonials-slider').owlCarousel({
		rtl: true,
		items: 1,
		loop: true
	});
	
	$(window).on('resize', function(){
		
		// To fix the parallax.js bug
		window.setTimeout(function(){
			$(window).resize();
		},500);
	
	});
	
	// To fix the parallax.js bug
	var isMobile = {
		Android: function() { return navigator.userAgent.match(/Android/i); }, 
		BlackBerry: function() { return navigator.userAgent.match(/BlackBerry/i); }, 
		iOS: function() { return navigator.userAgent.match(/iPhone|iPad|iPod/i); }, 
		Opera: function() { return navigator.userAgent.match(/Opera Mini/i); }, 
		Windows: function() { return navigator.userAgent.match(/IEMobile/i); }, 
		any: function() { return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows()); }
	};
    jQuery(function($) {
        if (isMobile.any()) {
			document.documentElement.className = document.documentElement.className + " touch";
            $('.parallax').each(function(i, obj) {
                $(this).css("background-image", 'url('+$(this).data('image-src')+')');
                $(this).css("background-color", "#FFFFFF");
                $(this).css("background-size", "cover");
                $(this).css("background-position", "center center");
            });
        }
	});
	
	
	
	
	/*=========================================================================
		Contact Form
	=========================================================================*/
	function isJSON(val){
		var str = val.replace(/\\./g, '@').replace(/"[^"\\\n\r]*"/g, '');
		return (/^[,:{}\[\]0-9.\-+Eaeflnr-u \n\r\t]*$/).test(str);
	}
	$('#contact-form').validator().on('submit', function (e) {
		if (!e.isDefaultPrevented()) {
			// If there is no any error in validation then send the message
			e.preventDefault();
			var $this = $(this),
				//You can edit alerts here
				alerts = {
					success: 
					"<div class='form-group' >\
						<div class='alert alert-success' role='alert'> \
							<strong>پیام با موفقیت ارسال شد!</strong> به زودی با شما تماس خواهیم گرفت\
						</div>\
					</div>",
					error: 
					"<div class='form-group' >\
						<div class='alert alert-danger' role='alert'> \
							<strong>خطا!</strong> خطایی در ارسال پیام رخ داده است. لطفا دوباره تلاش کنید.\
						</div>\
					</div>"
				};
			$.ajax({
				url: 'php/mail.php',
				type: 'post',
				data: $this.serialize(),
				success: function(data){
					if( isJSON(data) ){
						data = $.parseJSON(data);
						if(data['error'] == false){
							$('#contact-form-result').html(alerts.success);
							$('#contact-form').trigger('reset');
						}else{
							$('#contact-form-result').html(
							"<div class='form-group' >\
								<div class='alert alert-danger alert-dismissible' role='alert'> \
									<button type='button' class='close' data-dismiss='alert' aria-label='Close' > \
										<i class='ion-ios-close-empty' ></i> \
									</button> \
									"+ data['error'] +"\
								</div>\
							</div>"
							);
						}
					}else{
						$('#contact-form-result').html(alerts.error);
					}
				},
				error: function(){
					$('#contact-form-result').html(alerts.error);
				}
			});
		}
	});


    /*=========================================================================
    Svg Path
	=========================================================================*/
    (function () {

        // Creating SVG and path elements and insert to DOM

        var svgNS = 'http://www.w3.org/2000/svg';
        var svgEl = document.createElementNS(svgNS, 'svg');
        var svgContainer =document.getElementById("svg");

        var pathEl = document.createElementNS(svgNS, 'path');
        // The `getSinPath` function return the `path` in String format
        pathEl.setAttribute('d', getSinPath());
        pathEl.setAttribute('class', 'path-slider__path');

        svgEl.appendChild(pathEl);
        svgContainer.appendChild(svgEl);


        // Changing `background-image`
        // Firstly, saving the computed `background` of each item, as these are defined in CSS
        // When item is selected, the `background` is set accordingly

        var items = document.querySelectorAll('.path-slider__item');
        var images = [];
        for (var j = 0; j < items.length; j++) {
            images.push(items[j].querySelector('.item__circle').getAttribute('data-img'));
            // alert(items[j].querySelector('.item__circle').getAttribute('data-img'));
            //alert(getComputedStyle(items[j].querySelector('.item__circle')).getPropertyValue('background-image'));
        }

        var imgAnimation;
        var lastIndex;
        var setImage = function (index) {
            if (imgAnimation) {
                imgAnimation.pause();
                //alert(images[lastIndex]);
                sliderContainer.style['background-image'] = images[lastIndex];
                sliderContainerBackground.style['opacity'] = 0;
            }
            lastIndex = index;
            sliderContainerBackground.style['background-image'] = images[index];
            imgAnimation = anime({
                targets: sliderContainerBackground,
                opacity: 1,
                easing: 'linear'
            });
        };


        // Adding the extra element needed to fade the images smoothly
        // Also set the image for the initial current item (the first one)

        var sliderContainer = document.querySelector('.path-slider');
        var sliderContainerBackground = document.createElement('div');
        sliderContainerBackground.setAttribute('class', 'path-slider__background');
        setImage(0);
        sliderContainer.appendChild(sliderContainerBackground);


        // Initializing the slider

        var options = {
            startLength: 'center',
            paddingSeparation: 100,
            easing: 'easeOutCubic',
            begin: function (params) {
                // Item get selected, then set the `background` accordingly
                if (params.selected) {
                    setImage(params.index);
                }
            }
        };

        var slider = new PathSlider(pathEl, '.path-slider__item', options);


        // Regenerate the SVG `path` and update items position on `resize` event (responsive behavior)

        window.addEventListener('resize', function() {
            pathEl.setAttribute('d', getSinPath());
            slider.updatePositions();
        });

    })();

});