// set aspect ratio for chart
const aspectRatio = 1.778;

// append svg to the body of the page
const svg = d3.select("#draw-here")
    .append("svg");

// allow some margin at the left and top
const chartArea = svg.append("g");

// parse the data
const unparsed_data = JSON.parse(document.getElementById("line_data").textContent);
const date_format = JSON.parse(document.getElementById("date_format").textContent);
const parseTime = d3.timeParse(date_format);
data = unparsed_data.map(function (d) { return {"x_data": parseTime(d.x_data), "y_data": d.y_data}; })

// x axis
const x = d3.scaleTime()
            .domain(d3.extent(data, function(d) { return d.x_data; }));

const xAxis = chartArea.append("g")
                       .attr("class", "custom-axis");
                       
// y axis
const y = d3.scaleLinear()
    .domain([0, d3.max(data, function (d) { return d.y_data; })]);

const yAxis = chartArea.append("g")
                       .attr("class", "custom-axis");

// line
const lines = chartArea.append("path")
                       .datum(data)
                       .attr("fill", "none")
                       .attr("stroke", "#004599")
                       .attr("stroke-width", 2);

// x grid lines
const x_grid_lines = chartArea.append("g")			
                              .attr("class", "grid");
                              
// y grid lines
const y_grid_lines = chartArea.append("g")
                              .attr("class", "grid");

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
    let innerWidth = currentWidth - margin.left - margin.right;
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
    innerWidth = currentWidth - margin.left - margin.right;

    x.range([0, innerWidth]);

    xAxis.attr("transform", "translate(0," + innerHeight + ")")      
         .call(d3.axisBottom(x)
                 .ticks(parseInt(Math.max(innerWidth/50, 2)))
              );
    
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

    yAxis.call(d3.axisLeft(y)
                 .ticks(parseInt(Math.max(innerHeight/50, 2)))
              );

    xAxis.attr("transform", "translate(0," + innerHeight + ")");

    // update lines
    lines.attr("d", d3.line()
                .x(function (d) { return x(d.x_data); })
                .y(function (d) { return y(d.y_data); })
              );
    
    // update grid lines
    y_grid_lines.call(d3.axisLeft(y)
                        .ticks(parseInt(Math.max(innerHeight/50, 2)))
                        .tickSize(-innerWidth)
                        .tickFormat("")
                     );

    x_grid_lines.attr("transform", "translate(0," + innerHeight + ")")
                .call(d3.axisBottom(x)
                        .ticks(parseInt(Math.max(innerWidth/50, 2)))
                        .tickSize(-innerHeight)
                        .tickFormat("")
                     );
}

// initialize the chart
drawChart();

// add an event listener to redraw chart when user resizes window
window.addEventListener("resize", drawChart);