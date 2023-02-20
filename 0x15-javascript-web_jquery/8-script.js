$(document).ready(() => {
	$.getJSON(
		"https://swapi-api.alx-tools.com/api/films/?format=json",
		(data) => {
			data.results.forEach((film) => {
				$("<li>").text(film.title).appendTo("ul#list_movies");
			});
		}
	);
});
