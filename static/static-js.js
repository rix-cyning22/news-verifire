$(function() {
    $('input[name="inputchoice"]').on('click', function() {
        if ($(this).val() == 'link') {
            $('#link').show();
			$('#text').hide();
        }
        else {
            $('#text').show();
			$("#link").hide();
        }
    });
});

function submit()
{
	$(function() {
		if ($('input[name="inp"]').val() == "")
			$(this).css({
				"background-color": "#F7F7F7",
				"disabled": true 
			});
			
	});
}

$(".jumbotron").css({ height: $(window).height() + "px" });

$(window).on("resize", function() {
	$(".jumbotron").css({ height: $(window).height() + "px" });
});