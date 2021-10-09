let form = document.getElementById("profile-form")
form.addEventListener("submit", (e) => {
  e.preventDefault()
  const first_name = document.querySelector("#firstname").value
  const phone = document.querySelector("#phone").value
  fetch("user_profile", {
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      first_name: first_name,
      phone: phone,
    }),
    method: "POST",
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data)
    })
})
