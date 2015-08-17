function loadRecommendationFor(nickname, board_name) {
    if (nickname == undefined || board_name == undefined
            || nickname == '' || board_name == ''){
        alert("Please, complete all required fields!")
        return;
      }

      $("#modalWindow").modal('show')

      data = {
        nickname: nickname,
        board_name: board_name
      }

      $.get("/api/v1/recommend", data)
        .done(function( response ) {
            $("#modalWindow").modal('hide')

            if (response['status'] != 0) {
              alert(response['error']);
              return;
            }

            var images = response['data'];
            var image_urls = []
            for (var i = 0; i < images.length; i++) {
                image_urls.push(images[i]['url']);
            }
            displayImages(image_urls)
        })
        .fail(function(jqXHR, textStatus) {
            $("#modalWindow").modal('hide')
            alert('An error occurred: ' + textStatus);
        });
}

var numOfCol = 5;

function displayImages(images) {
    $('#header').html('<p align="center" class="header">Your recommendations</p>')

	html = '';
	for (var i = 0; i < images.length; i++) {
	    html += '<div class="imgholder"><img src="' + images[i] + '" /></div>';
	}
	$('#content').html(html);

    organize();
    var imgLoad = imagesLoaded('#container');
    imgLoad.on( 'progress', function( instance, image ) {
        organize();
    });

    //window resize
	var currentWidth = 1100;
	$(window).resize(function() {
		var winWidth = $(window).width();
		var conWidth;
		if(winWidth < 660) {
			conWidth = 440;
			col = 2
		} else if(winWidth < 880) {
			conWidth = 660;
			col = 3
		} else if(winWidth < 1100) {
			conWidth = 880;
			col = 4;
		} else {
			conWidth = 1100;
			col = 5;
		}

		if(conWidth != currentWidth) {
			currentWidth = conWidth;
			$('#content').width(conWidth);

			numOfCol = col;
			organize();
		}
	});
}

function organize() {
    $('#content').BlocksIt({
        numOfCol: numOfCol,
        offsetX: 8,
        offsetY: 8
    });
}