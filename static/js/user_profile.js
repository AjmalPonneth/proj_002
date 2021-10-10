let form = document.getElementById("profile-form")
form.addEventListener("submit", (e) => {
  e.preventDefault()
  const first_name = document.querySelector("#firstname").value
  const phone = document.querySelector("#phone").value
  const user_exp = document.getElementById("#exp").value
  fetch("user_profile", {
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      first_name: first_name,
      phone: phone,
      user_exp: parseInt(user_exp),
    }),
    method: "POST",
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.phone_exists == true) {
        document.querySelector("#error").textContent =
          "This phone number is already in use!"
      }
    })
})
