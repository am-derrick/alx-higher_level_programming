$(function () {
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, textStatus) {
	if (textStatus === 'success') {
	    $('#hello').text(data.hello);
	}
    });
});
