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
      headers: {
        "Content-Type": "application/json",
      },
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
        if (data.usesr_name_exists == true) {
          document.querySelector("#error").textContent =
            "This username already exists!"
        } else if (data.email_exists == true) {
          document.querySelector("#error").textContent =
            "This email already exists!"
        } else if (data.phone_exists == true) {
          document.querySelector("#error").textContent =
            "This phone number already exists!"
        } else {
          window.location.replace("login")
        }
      })
  } else {
    document.getElementById("error").textContent = "Password not match!"
  }
})
