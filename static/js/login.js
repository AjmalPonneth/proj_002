const btn = document.getElementById("login")
btn.addEventListener("click", (e) => {
  e.preventDefault()
  const usernameVal = document.querySelector("#username").value
  const passwordVal = document.querySelector("#password").value
  if (usernameVal.length > 0) {
    fetch("login", {
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