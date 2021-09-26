window.onload = onPageLoad()
function onPageLoad() {
  if (document.getElementById("test").checked == true) {
    document.getElementById("test").checked = true
  } else {
    document.getElementById("test").checked = false
  }
}
