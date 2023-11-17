$(document).ready(function () {
    $("INPUT#Save").click(function () {
	const api = "http://" + "calebcodes.tech/api/v1/modify/employees/";
	const comp = $("#company".val());
	const eml = $("#email".val());
	$.ajax({
	    url: api + comp + "/" + eml,
	    type: "PUT",
	    data: JSON.stringify({
		company: $("INPUT#company").val(),
		email: $("INPUT#email").val(),
		password: $("INPUT#password").val(),
		DOB: $("INPUT#DOB").val(),
		phone: $("INPUT#phone").val(),
		city: $("INPUT#city").val(),
		address: $("INPUT#address").val(),
		country: $("INPUT#country").val(),
		dept: $("INPUT#dept").val(),
		position: $("INPUT#position").val()
	    }),
	    contentType: "application/json",
	    dataType: "json"
	})
	    .done(function (data) {
		alert("Employee modified sucessfully");
	    });
    });
});
