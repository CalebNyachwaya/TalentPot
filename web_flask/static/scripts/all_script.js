$(document).ready(function () {
    $('#addUserForm').on('submit', function (event) {
	const api = "http://" + "www.talentpot.calebcodes.tech/api/v2/add/employees/";
	const comp = $("#company").val();
	$.ajax({
	    url: api + comp,
	    type: 'POST',
	    data: JSON.stringify({
		first_name: $('#first_name').val(),
		last_name: $('#last_name').val(),
		company: $('#company').val(),
		email: $('#email').val(),
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
		alert(`Employee added sucessfully ${data.email}`);
	    })
	event.preventDefault();
    })
})
