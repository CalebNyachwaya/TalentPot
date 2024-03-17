document.ready(function () {
  $("#asub").on("submit", function (event) {
    const api = "http://" + "talentpot.calebcodes.tech/api/v2/employees/";
    const comp = stringify($("#company".val()));
    $.ajax({
      url: api + comp,
      type: "POST",
      data: JSON.stringify({
        first_name: $("#first_name").val(),
        last_name: $("#last_name").val(),
        company: $("#company").val(),
        email: $("#email").val(),
        password: $("#password").val(),
        DOB: $("#DOB").val(),
        phone: $("#phone").val(),
        city: $("#city").val(),
        address: $("#address").val(),
        country: $("#country").val(),
        dept: $("#dept").val(),
        position: $("#position").val(),
      }),
      contentType: "application/json",
      dataType: "json",
    }).done(function (data) {
      alert("Employee added sucessfully");
    });
    event.preventDefault();
  });
  $("#msub").on("submit", function (event) {
    const api = "http://" + "calebcodes.tech/api/v2/employees/";
    const comp = stringify($("#company".val()));
    $.ajax({
      url: api + comp,
      type: "PUT",
      data: JSON.stringify({
        company: $("#company").val(),
        email: $("#email").val(),
        password: $("#password").val(),
        DOB: $("#DOB").val(),
        phone: $("#phone").val(),
        city: $("#city").val(),
        address: $("#address").val(),
        country: $("#country").val(),
        dept: $("#dept").val(),
        position: $("#position").val(),
      }),
      contentType: "application/json",
      dataType: "json",
    }).done(function (data) {
      alert("Employee modified sucessfully");
    });
    event.preventDefault();
  });
  $("#dsub").on("submit", function (event) {
    const api = "http://" + "calebcodes.tech/api/v2/employees/";
    const comp = stringify($("#company".val()));
    $.ajax({
      url: api + comp,
      type: "DELETE",
      data: JSON.stringify({
        company: $("#company").val(),
        email: $("#email").val(),
        password: $("#password").val(),
      }),
      contentType: "application/json",
      dataType: "json",
    }).done(function (data) {
      alert("Employee deleted sucessfully");
    });
    event.preventDefault();
  });
});
