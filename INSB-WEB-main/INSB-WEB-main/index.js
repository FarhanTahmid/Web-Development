var loadFile = function (event) {
  var image = document.getElementById("output");
  image.src = URL.createObjectURL(event.target.files[0]);
};

// for edit part
var editForm = document.getElementByclass("editProfileMenu");
var updateButton = document.getElementById("btn-submit");
var isEditable = false;

function Editable() {
  if (isEditable === true) {
    editForm.style.display = "block";
    isEditable = false;
  } else {
    editForm.style.display = "none";
    isEditable = true;
  }
}
