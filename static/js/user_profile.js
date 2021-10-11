let form = document.getElementById("profile-form")
form.addEventListener("submit", (e) => {
  e.preventDefault()
  const first_name = document.querySelector("#firstname").value
  const phone = document.querySelector("#phone").value
  const user_exp = document.getElementById("exp").value
  const user_goal = document.getElementById("goal").value
  const user_best = document.getElementById("best").value
  const user_current_project = document.getElementById("project").value
  const user_fav_lang = document.getElementById("fav").value
  fetch("user_profile", {
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      first_name: first_name,
      phone: phone,
      user_exp: parseInt(user_exp),
      user_goal: user_goal,
      user_best: user_best,
      user_current_project: user_current_project,
      user_fav_lang: user_fav_lang,
    }),
    method: "POST",
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.phone_exists == true) {
        document.querySelector("#error").textContent =
          "This phone number is already in use!"
      } else {
        document.querySelector("#error").textContent = ""
        window.location.reload()
      }
    })
})
