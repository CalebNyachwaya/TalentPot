$(document).ready(function () {
  $("#gentoken").on("submit", function (event) {
    const api = "http://" + "talentpot.calebcodes.tech/api/v2/reset_password";
    $.ajax({
      url: api,
      type: "POST",
      data: JSON.stringify({
        email: $("#email").val(),
      }),
      contentType: "application/json",
      dataType: "json",
    }).done(function (data) {
      alert(`Generated`);
    });
    event.preventDefault();
  });
});