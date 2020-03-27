// set aspect ratio for chart
const aspectRatio = 1.778;

// append svg to the body of the page
const svg = d3.select("#draw-here")
    .append("svg");

// allow some margin at the left and top
const chartArea = svg.append("g");

// parse the data
const data = JSON.parse(document.getElementById("line_data").textContent);

// x axis
const x = d3.scaleBand()
    .domain(data.map(function (d) { return d.x_data; }))
    .padding([0.2]);

const xAxis = chartArea.append("g")
                       .attr("class", "custom-axis");

// y axis
const y = d3.scaleLinear()
    .domain([0, d3.max(data, function (d) { return d.y_data; })]);

const yAxis = chartArea.append("g")
                       .attr("class", "custom-axis");

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
        left: 0,
        right: 0.05 * currentWidth
    };
    const outerHeight = Math.round(currentWidth / aspectRatio);
    let innerHeight = outerHeight - margin.top - margin.bottom;

    svg.attr("width", currentWidth)
       .attr("height", outerHeight);

    // update y axis
    y.range([innerHeight, 0]);

    yAxis.call(d3.axisLeft(y));

    // update margin left based on label size
    margin.left = 0;
    yAxis.selectAll("text").each(function () {
        if (this.getBBox().width > margin.left) {
            margin.left = this.getBBox().width;
        }
    });
    margin.left = margin.left + 15; // add a little extra for tick marks

    chartArea.attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

    // update x axis
    x.range([0, currentWidth - margin.left - margin.right]);

    xAxis.attr("transform", "translate(0," + innerHeight + ")")        
         .call(d3.axisBottom(x));
    
    // update margin bottom based on label size
    margin.bottom = 0;
    xAxis.selectAll("text").each(function () {
        if (this.getBBox().height > margin.bottom) {
            margin.bottom = this.getBBox().height;
        }
    });
    margin.bottom = margin.bottom + 15; // add a little extra for tick marks

    innerHeight = outerHeight - margin.top - margin.bottom;

    y.range([innerHeight, 0]);

    yAxis.call(d3.axisLeft(y));

    xAxis.attr("transform", "translate(0," + innerHeight + ")");

    // update bars
    bars.attr("x", function (d) { return x(d.x_data); })
        .attr("width", x.bandwidth())
        .attr("y", function (d) { return y(d.y_data); })
        .attr("height", function (d) { return innerHeight - y(d.y_data); });
}

// initialize the chart
drawChart();

// add an event listener to redraw chart when user resizes window
window.addEventListener("resize", drawChart);