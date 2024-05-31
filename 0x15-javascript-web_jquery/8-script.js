$(document).ready(function () {
    $.ajax({
	url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
	method: 'GET',
	success: function (response) {
	    response.results.forEach(function (film) {
		$("<li>").text(film.title).appendTo("ul#list_movies");
	};
    });
});
