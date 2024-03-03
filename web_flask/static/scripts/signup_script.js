$(document).ready(function () {
  $("#signup_page").on("submit", function (event) {
    const api = "http://" + "talentpot.calebcodes.tech/api/v1/users";
    const passwd = $("#password").val();
    const rpasswd = $("#rpassword").val();
    if (passwd === rpasswd) {
      $.ajax({
        url: api,
        type: "POST",
        data: JSON.stringify({
          email: $("#email").val(),
          password: passwd,
        }),
        contentType: "application/json",
        dataType: "json",
      }).done(function (data) {
        alert(`User created ${data}`);
      });
    } else {
      alert("The passwords do not match");
    }

    event.preventDefault();
  });
});
