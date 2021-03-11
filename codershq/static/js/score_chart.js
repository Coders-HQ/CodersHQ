var scores = [
  700,
  800,
  900,
  600,
  500,
  300,
  600,
  700,
  750,
  790,
  810,
  { y: 604, dataLabels: { enabled: true } },
];

Highcharts.chart("container", {
  chart: {
    type: "area",
    backgroundColor: "rgba(0,0,0,0)",
  },
  title: {
    text: new Date().getFullYear(),
  },
  xAxis: {
    categories: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ],
  },
  yAxis: {
    title: {
      text: "Total Score",
    },
    labels: {
      formatter: function () {
        return this.value / 1;
      },
    },
  },
  tooltip: {
    pointFormat: "Score: {point.y}",
  },
  plotOptions: {
    area: {
      pointStart: 0,
      marker: {
        enabled: false,
        symbol: "circle",
        radius: 2,
        states: {
          hover: {
            enabled: true,
          },
        },
      },
    },
  },
  series: [
    {
      name: "Score",
      color: "#da0202",
      data: scores,
    },
  ],
});

if (theme === "light") {
  $("highcharts-color-0").css("fill", "#da0202");
  $("highcharts-color-0").css("stroke", "#da0202");
  $(".highcharts-title").css("fill", "black");
} else {
  $("highcharts-color-0").css("fill", "#da0202");
  $("highcharts-color-0").css("stroke", "#da0202");
  $(".highcharts-title").css("fill", "black");
}
