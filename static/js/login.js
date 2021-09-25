const form = document.getElementById("login-form")
form.addEventListener("submit", (e) => {
  e.preventDefault()
  const usernameVal = document.querySelector("#username").value
  const passwordVal = document.querySelector("#password").value
  if (usernameVal.length > 0) {
    fetch("login", {
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: usernameVal,
        password: passwordVal,
      }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.success == false) {
          document.getElementById("error").textContent =
            "Username or password is incorrect!"
        } else {
          window.location.replace("index")
        }
      })
  }
})
