$(document).ready(function () {
  $("#signup_page").on("submit", function (event) {
    const api = "http://" + "talentpot.calebcodes.tech/api/v1/reset_password";
    const passwd = $("#password").val();
    const rpasswd = $("#rpassword").val();
    if (passwd === rpasswd) {
      $.ajax({
        url: api,
        type: "PUT",
        data: JSON.stringify({
          email: $("#email").val(),
          new_password: passwd,
          token: $("#token").val(),
        }),
        contentType: "application/json",
        dataType: "json",
      }).done(function (data) {
        alert(`Password changed ${data}`);
      });
    } else {
      alert("The passwords do not match");
    }

    event.preventDefault();
  });
});
