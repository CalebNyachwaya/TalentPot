$(document).ready(function () {
  $("#signup_page").on("submit", function (event) {
    const api = "http://" + "talentpot.calebcodes.tech/api/v1/users";
    $.ajax({
      url: api,
      type: "POST",
      data: JSON.stringify({
        email: $("#email").val(),
        password: $("#password").val(),
      }),
      contentType: "application/json",
      dataType: "json",
    }).done(function (data) {
      alert(`Signed in ${data}`);
    });
    event.preventDefault();
  });
});
