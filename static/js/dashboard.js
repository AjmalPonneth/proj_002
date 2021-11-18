var ctx = document.getElementById("myChart").getContext("2d")
let windows = document.getElementById("windows").value
let mac = document.getElementById("mac").value
let iphone = document.getElementById("iphone").value
let android = document.getElementById("android").value
let others = document.getElementById("others").value
var myChart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: ["Windows", "Android", "Mac", "Iphone", "Others"],
    datasets: [
      {
        label: "# Windows",
        data: [windows, android, mac, iphone, others],
        backgroundColor: [
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(255, 206, 86, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(153, 102, 255, 0.2)",
          "rgba(255, 159, 64, 0.2)",
        ],
        borderColor: [
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)",
          "rgba(75, 192, 192, 1)",
          "rgba(153, 102, 255, 1)",
          "rgba(255, 159, 64, 1)",
        ],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
})



var chart2 = document.getElementById("sessionChart").getContext("2d")
let python = document.querySelector("#python").value
let js = document.querySelector("#js").value
let c = document.querySelector("#c").value
let java = document.querySelector("#java").value
let csharp = document.querySelector("#csharp").value
let cpp = document.querySelector("#cpp").value
let php = document.querySelector("#php").value
let r = document.querySelector("#r").value
let ruby = document.querySelector("#ruby").value
let go = document.querySelector("#go").value
let other = document.querySelector("#other").value
var myChart = new Chart(chart2, {
  type: "pie",
  data: {
    labels: ["Python", "Javascript", "PHP", "Java", "C++","C#","Ruby","Go","R","Other"],
    datasets: [
      {
        label: "# Session",
        data: [python,js, php, java, cpp, csharp,ruby,go,ruby,r,other],
        backgroundColor: [
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(255, 206, 86, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(153, 102, 255, 0.2)",
          "rgba(255, 159, 64, 0.2)",
        ],
        borderColor: [
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)",
          "rgba(75, 192, 192, 1)",
          "rgba(153, 102, 255, 1)",
          "rgba(255, 159, 64, 1)",
        ],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
})