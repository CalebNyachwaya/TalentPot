$(document).ready(function () {
  $("#signin_page").on("submit", function (event) {
    const api = "http://" + "talentpot.calebcodes.tech/api/v2/sessions";
    $.ajax({
      url: api,
      type: "POST",
      data: JSON.stringify({
        email: $("#email").val(),
        password: $("#password").val(),
      }),
      contentType: "application/json",
      dataType: "json",
    }).done(function (data, test) {
      alert(`Signed in` + test);
      // $.cookie("session_id", "cookieValue");
    });
    event.preventDefault();
  });
});
