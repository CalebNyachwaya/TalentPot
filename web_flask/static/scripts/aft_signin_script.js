$("#aft_script").click(() => {
  const api = "http://" + "talentpot.calebcodes.tech/api/v2/sessions";
  $.ajax({
    url: api,
    type: "DELETE",
    contentType: "application/json",
    dataType: "json",
  }).done(function (data) {
    alert(`Logged out succesfully`);
  });
});
