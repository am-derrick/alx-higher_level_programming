$(function () {
    $.get('https://swapi.co/api/films/?fomrat=json', function (data, testStatus) {
	if (textStatus === 'success') {
	    let films = data.results;
	    for (let i in films) {
		$('#list_movies').append('<li>' + films[i].title + '</li>');
	    }
	}
    });
});
