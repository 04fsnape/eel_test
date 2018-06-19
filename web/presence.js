function presenceCheck() {
  var inputs = document.getElementsByClassName("inputs");
  for (var i = 0; i < inputs.length; i++) {
    if inputs[i].value.length == 0 {
      inputs[i].style.borderBottom = "1px solid red !important";
    }
}
}
