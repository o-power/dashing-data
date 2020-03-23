// set the dimensions and margins of the graph
const margin = {top: 30, right: 30, bottom: 70, left: 60};
//const width = 460 - margin.left - margin.right
const height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
const svg = d3.select("#draw-here")
              .append("svg")
              //.attr("width", width + margin.left + margin.right)
              .attr("height", height + margin.top + margin.bottom);

const chartArea = svg.append("g")
                     .attr("transform",
                     "translate(" + margin.left + "," + margin.top + ")");

// Parse the Data
const data = JSON.parse(document.getElementById('bar_data').textContent);

// X axis
const x = d3.scaleBand()
            .domain(data.map(function (d) { return d.x_data; }))
            .padding(0.2);
            //.range([0, width])
            //.domain(data.map(function (d) { return d.x_data; }))
            //.padding(0.2);

const xAxis = chartArea.append("g")
                       .attr("transform", "translate(0," + height + ")");
                       //.call(d3.axisBottom(x))
                       //.selectAll("text")
                       //.attr("transform", "translate(-10,0)rotate(-45)")
                       //.style("text-anchor", "end");

// Add Y axis
const y = d3.scaleLinear()
          .domain([0, 10])
          .range([height, 0]);

const yAxis = chartArea.append("g")
                       .call(d3.axisLeft(y));

// Bars
const bars = chartArea.selectAll("bars")
                .data(data)
                .enter()
                .append("rect")
                //.attr("x", function (d) { return x(d.x_data); })
                .attr("y", function (d) { return y(d.y_data); })
                //.attr("width", x.bandwidth())
                .attr("height", function (d) { return height - y(d.y_data); })
                .attr("fill", "#69b3a2");

// A function that finishes to draw the chart for a specific device size.
function drawChart() {
  // get the current width of the div where the chart appear, and attribute it to Svg
  currentWidth = parseInt(d3.select('#draw-here').style('width'), 10);
  svg.attr("width", currentWidth);

  // Update the X scale and Axis (here the 20 is just to have a bit of margin)
  x.range([0, currentWidth - margin.left - margin.right]);

  xAxis.call(d3.axisBottom(x));
       //.selectAll("text")
       //.attr("transform", "translate(-10,0)rotate(-45)")
       //.style("text-anchor", "end");

  // Add the last information needed for the bars: their X position
  bars.attr("x", function(d) { return x(d.x_data); })
      .attr("width", x.bandwidth());
}

// Initialize the chart
drawChart();

// Add an event listener that run the function when dimension change
window.addEventListener('resize', drawChart);