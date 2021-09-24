let form = document.getElementById("register-form")
form.addEventListener("submit", (e) => {
  e.preventDefault()
  const username = document.querySelector("#username").value
  const email = document.querySelector("#email").value
  const phone = document.querySelector("#phone").value
  const password = document.querySelector("#password").value
  const password2 = document.querySelector("#password2").value
  if (password == password2) {
    fetch("register", {
      body: JSON.stringify({
        username: username,
        email: email,
        phone: phone,
        password: password,
      }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data)
      })
  } else {
    document.getElementById("error").textContent = "Password not match!"
  }
})
