$(document).ready(function () {
    $('#modifyUserForm').on('submit', function (event) {
	const api = "http://" + "calebcodes.tech/api/v1/modify/employees/";
	const comp = $("#company").val();

	const eml = $("#email".val());
	$.ajax({
	    url: api + comp,
	    type: 'POST',
	    data: JSON.stringify({
		company: $('#company').val(),
		email: $('#email').val(),
		password: $('#password').val(),
		DOB: $('#DOB').val(),
		phone: $('#phone').val(),
		city: $('#city').val(),
		address: $('#address').val(),
		country: $('#country').val(),
		dept: $('#dept').val(),
		position: $('#position').val()
	    }),
	    contentType: 'application/json',
	    dataType: 'json',
	})
	    .done(function (data) {
		alert("Employee modified sucessfully");
	    })
	event.preventDefault();
    })
})
