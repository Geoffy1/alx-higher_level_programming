$(document).ready(() => {
	$("INPUT#btn_translate").click(() => {
		const language_code = $("INPUT#language_code").val();
		$.getJSON(
			`https://fourtonfish.com/hellosalut/hello/?lang=${language_code}`,
			(data) => {
				$("#hello").text(data.hello);
			}
		);
	});
});
