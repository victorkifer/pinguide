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
}

function organize() {
    $('#content').BlocksIt({
        numOfCol: 4,
        offsetX: 8,
        offsetY: 8
    });
}