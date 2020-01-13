(function($) {
"use strict";

/*------------------------------------------------------------------
[Table of contents]


/*-------------------------------------------
  js wow
--------------------------------------------- */
 new WOW().init();
/*-------------------------------------------
    isotope activation 
--------------------------------------------- */
//=================
$('container').imagesLoaded(function () {
	// filter items on button click
	$('.filtering-button').on('click', 'a', function () {
		var filterValue = $(this).attr('data-filter');
		$grid.isotope({ filter: filterValue });
    });
    $('.filtering-button').on('click', 'a', function () {
        $('.filtering-button a').removeClass('active');
        $(this).addClass('active');
    });
	var $grid = $('.grid').isotope({
		// set itemSelector so .grid-sizer is not used in layout
		itemSelector: '.grid-item',
		percentPosition: true,
		animationOptions: {
			duration: 500,
			easing: 'zoom-in'
		},
		masonry: {
			// use element for option
			columnWidth: '.grid-item'
		},
		transitionDuration: '.9s'
	})
});
/*-------------------------------------------
slide-happyclint
--------------------------------------------- */
$(".slide-happyclint").owlCarousel({
	autoPlay: true, 
	slideSpeed:5000,
	pagination:false,
	navigation:true,	  
	items : 1,
	navigationText:["<i class='flaticon-left-arrow'></i>","<i class='flaticon-right-arrow'></i>"],
	itemsDesktop : [1199,1],
	itemsDesktopSmall : [980,1],
	itemsTablet: [768,1],
	itemsMobile : [479,1],
}); 
/*-------------------------------------------
slide-testimonai
--------------------------------------------- */
$(".slide-testimonai.owlCarousel").owlCarousel({
	autoPlay: false, 
	slideSpeed:5000,
	pagination:false,
	navigation:false,	  
	items : 1,
	navigationText:["<i class='fa fa-long-arrow-left'></i>","<i class='fa fa-long-arrow-right'></i>"],
	itemsDesktop : [1199,1],
	itemsDesktopSmall : [980,1],
	itemsTablet: [768,1],
	itemsMobile : [479,1],
});
/*-------------------------------------------
Sticky Header
--------------------------------------------- */

/*-------------------------------------------
progress-bar
--------------------------------------------- */
$('#progress-bar').appear(function() {
	$('#bar1').barfiller({ barColor: '#00a651', duration: 3000 });
	$('#bar2').barfiller({ barColor: '#00a651', duration: 3000 });
	$('#bar3').barfiller({ barColor: '#00a651', duration: 2000 });
	$('#bar4').barfiller({ barColor: '#00a651', duration: 4000 });
	$('#bar5').barfiller({ barColor: '#00a651', duration: 4000 });
	$('#bar6').barfiller({ barColor: '#ff7200', duration: 3000 });
	$('#bar7').barfiller({ barColor: '#ff7200', duration: 3000 });
	$('#bar8').barfiller({ barColor: '#ff7200', duration: 2000 });
	$('#bar9').barfiller({ barColor: '#ff7200', duration: 4000 });
	$('#bar10').barfiller({ barColor: '#ff7200', duration: 4000 });
	
});
/*-------------------------------------------
google  map
--------------------------------------------- */
if ($('#gmap').length > 0) {
	new GMaps({
		div: '#gmap',
		lat: 23.7947172, // 23.7947172,90.3971412
		lng: 90.3971412,
		scrollwheel: false,				
		styles: [
			{
				"featureType": "landscape",
				"elementType": "geometry",
				"stylers": [
					{
						"color": "#dddddd"
					},
					{
						"lightness": 20
					}
				]
			},
			{
				"featureType": "road.highway",
				"elementType": "geometry.fill",
				"stylers": [
					{
						"color": "#ffffff"
					},
					{
						"lightness": 17
					}
				]
			},
			{
				"featureType": "road.highway",
				"elementType": "geometry.stroke",
				"stylers": [
					{
						"color": "#ffffff"
					},
					{
						"lightness": 29
					},
					{
						"weight": 0.2
					}
				]
			},
			{
				"featureType": "road.arterial",
				"elementType": "geometry",
				"stylers": [
					{
						"color": "#ffffff"
					},
					{
						"lightness": 18
					}
				]
			},
			{
				"featureType": "road.local",
				"elementType": "geometry",
				"stylers": [
					{
						"color": "#dddddd"
					},
					{
						"lightness": 16
					}
				]
			},
			{
				"featureType": "poi",
				"elementType": "geometry",
				"stylers": [
					{
						"color": "#ffffff"
					},
					{
						"lightness": 21
					}
				]
			},
			{
				"featureType": "poi.park",
				"elementType": "geometry",
				"stylers": [
					{
						"color": "#ffffff"
					},
					{
						"lightness": 21
					}
				]
			},
			{
				"elementType": "labels.text.stroke",
				"stylers": [
					{
						"visibility": "on"
					},
					{
						"color": "#ffffff"
					},
					{
						"lightness": 16
					}
				]
			},
			{
				"elementType": "labels.icon",
				"stylers": [
					{
						"visibility": "on"
					}
				]
			}
		]
	}).addMarker({
		lat: 23.792930, //23.792930, 90.403798
		lng: 90.403798,
		infoWindow: {
			content: '<p> loaction</p>'
		}
		});

}


})(jQuery);