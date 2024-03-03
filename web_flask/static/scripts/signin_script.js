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
    }).done(function (data) {
      alert(`Signed in ${data.email}`);
      // $.cookie("session_id", "cookieValue");
      document.cookie = `cookieName=data.session_id`;

      // Set a cookie with expiration time (in days)
      var expirationDate = new Date();
      expirationDate.setDate(expirationDate.getDate() + 7); // Expires in 7 days
      document.cookie =
        "session_id=cookieValue; expires=" + expirationDate.toUTCString();
      window.location.href = "/aft_signin";
    });
    event.preventDefault();
  });
});
