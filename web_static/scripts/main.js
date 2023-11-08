// document.addEventListener("DOMContentLoaded", function () {
//   const addUserButton = document.getElementById("addUserButton");
//   const userForm = document.getElementById("userForm");

//   addUserButton.addEventListener("click", function () {
//     userForm.classList.remove("hidden");
//   });

//   const addUserForm = document.getElementById("addUserForm");
//   addUserForm.addEventListener("submit", function (e) {
//     e.preventDefault();
//     // Handle the form submission, e.g., send data to the server.
//     // You can use JavaScript to process form data or make AJAX requests here.
//     // After processing, you can hide the form if needed.
//     userForm.classList.add("hidden");
//   });
// });

document.addEventListener("DOMContentLoaded", function () {
  const addUserButton = document.getElementById("addUserButton");
  const userFormOverlay = document.getElementById("userFormOverlay");
  const userForm = document.getElementById("userForm");

  addUserButton.addEventListener("click", function () {
    userFormOverlay.style.display = "block";
    userForm.style.display = "block";
  });

  const addUserForm = document.getElementById("addUserForm");
  addUserForm.addEventListener("submit", function (e) {
    e.preventDefault();
    // Handle form submission as needed
    // Hide the modal and overlay
    userFormOverlay.style.display = "none";
    userForm.style.display = "none";
  });
});
