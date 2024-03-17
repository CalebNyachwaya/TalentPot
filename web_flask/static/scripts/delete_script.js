$(document).ready(function () {
  $("#deleteUserForm").on("submit", function (event) {
    const api =
      "http://" + "www.talentpot.calebcodes.tech/api/v2/delete/employees/";
    const comp = $("INPUT#company").val();
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
