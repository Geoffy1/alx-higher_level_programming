$(document).ready(() => {
	$("INPUT#btn_translate").click(fetchTranslation);
	$("INPUT#language_code").keyup((event) => {
		if (event.keyCode === 13) {
			fetchTranslation();
		}
	});

	(fetchTranslation) => {
		const language_code = $("INPUT#language_code").val();
		$.getJSON(
			`https://fourtonfish.com/hellosalut/hello/?lang=${language_code}`,
			(data) => {
				$("#hello").text(data.hello);
			}
		);
	}
});
