// set aspect ratio for chart
const aspectRatio = 1.778;

// append svg to the body of the page
const svg = d3.select("#draw-here")
    .append("svg");

// allow some margin at the left and top
const chartArea = svg.append("g");

// parse the data
const data = JSON.parse(document.getElementById("bar_data").textContent);

// x axis
const x = d3.scaleBand()
    .domain(data.map(function (d) { return d.x_data; }))
    .padding([0.2]);

const xAxis = chartArea.append("g");

// y axis
const y = d3.scaleLinear()
    .domain([0, d3.max(data, function (d) { return d.y_data; })]);

const yAxis = chartArea.append("g");

// bars
const bars = chartArea.selectAll("bars")
    .data(data)
    .enter()
    .append("rect")
    .attr("fill", "#004599");

// A function that finishes drawing the chart
function drawChart() {
    // get the current width of the div containing the chart and use this to set the svg width
    const currentWidth = parseInt(d3.select("#draw-here").style("width"), 10);
    const margin = {
        top: 0.05 * currentWidth,
        bottom: 0.10 * currentWidth,
        left: 0.15 * currentWidth,
        right: 0.05 * currentWidth
    };
    const height = Math.round(currentWidth / aspectRatio) - margin.top - margin.bottom;

    svg.attr("width", currentWidth)
        .attr("height", height + margin.top + margin.bottom);

    // allow some margin
    chartArea.attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

    // update x axis
    x.range([0, currentWidth - margin.left - margin.right]);

    xAxis.attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

    // update y axis
    y.range([height, 0]);

    yAxis.call(d3.axisLeft(y));

    // update bars
    bars.attr("x", function (d) { return x(d.x_data); })
        .attr("width", x.bandwidth())
        .attr("y", function (d) { return y(d.y_data); })
        .attr("height", function (d) { return height - y(d.y_data); });
}

// initialize the chart
drawChart();

// add an event listener to redraw chart when user resizes window
window.addEventListener("resize", drawChart);