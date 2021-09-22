$(document).ready(function () {
  $(".login").on("submit", function () {
    $.ajax({
      url: "validate",
      type: "POST",
      dataType: "json",
      data: {
        username: $("#username").val(),
        password: $("#password").val(),
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken").val(),
      },
      success: function (json) {
        console.log(json.success)
      },
    })
  })
})
