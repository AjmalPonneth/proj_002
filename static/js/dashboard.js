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
        label: "# of Votes",
        data: [windows, mac, iphone, android, others],
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
