const usernameField = document.querySelector("#username")
usernameField.addEventListener("keyup", (e) => {
  const usernameVal = e.target.value
  console.log(usernameVal)
})
