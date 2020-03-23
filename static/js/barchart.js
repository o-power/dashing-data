// set the dimensions and margins of the graph
const margin = {top: 30, right: 30, bottom: 70, left: 60};
const height = 400 - margin.top - margin.bottom;

// append svg to the body of the page
const svg = d3.select("#draw-here")
              .append("svg")
              .attr("height", height + margin.top + margin.bottom);

// allow some margin at the left and top
const chartArea = svg.append("g")
                     .attr("transform",
                     "translate(" + margin.left + "," + margin.top + ")");

// parse the data
const data = JSON.parse(document.getElementById('bar_data').textContent);

// x axis
const x = d3.scaleBand()
            .domain(data.map(function (d) { return d.x_data; }))
            .padding([0.2]);

const xAxis = chartArea.append("g")
                       .attr("transform", "translate(0," + height + ")");

// y axis
const y = d3.scaleLinear()
            .domain([0,d3.max(data, function(d) { return d.y_data; })])
            .range([height, 0]);

const yAxis = chartArea.append("g")
                       .call(d3.axisLeft(y));

// bars
const bars = chartArea.selectAll("bars")
                .data(data)
                .enter()
                .append("rect")
                .attr("y", function (d) { return y(d.y_data); })
                .attr("height", function (d) { return height - y(d.y_data); })
                .attr("fill", "#004599");

// A function that finishes drawing the chart
function drawChart() {
  // get the current width of the div containing the chart and use this to set the svg width
  currentWidth = parseInt(d3.select('#draw-here').style('width'), 10);
  svg.attr("width", currentWidth);

  // update x axis
  x.range([0, currentWidth - margin.left - margin.right]);

  xAxis.call(d3.axisBottom(x));

  // update bars
  bars.attr("x", function(d) { return x(d.x_data); })
      .attr("width", x.bandwidth());
}

// initialize the chart
drawChart();

// add an event listener to redraw chart when user resizes window
window.addEventListener('resize', drawChart);