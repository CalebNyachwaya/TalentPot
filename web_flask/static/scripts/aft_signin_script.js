$("a#aft_script").click(function () {
  const api = "http://" + "www.talentpot.calebcodes.tech/api/v2/sessions";
  $.ajax({
    url: api,
    type: "DELETE",
    contentType: "application/json",
    dataType: "json",
    data: JSON.stringify({
      email: 1,
    }),
  }).done(function (data) {
    alert(`Logged out succesfully`);
    window.location.href = "/";
  });
});
