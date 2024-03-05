$(document).ready(function () {
  $("#resetpass").on("submit", function (event) {
    const api = "http://" + "www.talentpot.calebcodes.tech/api/v2/reset_password";
    const passwd = $("#password").val();
    const rpasswd = $("#rpassword").val();
    if (passwd === rpasswd) {
      $.ajax({
        url: api,
        type: "PUT",
        data: JSON.stringify({
          email: $("#email").val(),
          new_password: passwd,
          reset_token: $("#token").val(),
        }),
        contentType: "application/json",
        dataType: "json",
      }).done(function (data) {
        alert(`Password changed ${data.email}. \n Back to sign-in`);
        window.location.href = "/signin";
      });
    } else {
      alert("The passwords do not match");
    }

    event.preventDefault();
  });
});
