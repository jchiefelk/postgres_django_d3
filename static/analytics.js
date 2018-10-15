// Set the Dimensions
function renderGroupedBarChart(date) {
  var url;

  if(date){
    url = 'http://127.0.0.1:8000/api?date='+date;
  } else {
    url = 'http://127.0.0.1:8000/api'
  }
  d3.selectAll("svg > *").remove(); // clear all svg elements before 
  d3.json(url,{
    method:"GET",
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  })
  .then(function(results) {

      console.log(results);

      var width = 960;
      var height = 500;
      var svg = d3.select("#groupedchart")
        .append("svg").attr("width", width).attr("height", height),      
        margin = {top: 20, right: 20, bottom: 30, left: 40},
        width = +svg.attr("width") - margin.left - margin.right,
        height = +svg.attr("height") - margin.top - margin.bottom,
        g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

       // console.log(results);
      var parseTime = d3.timeParse("%d-%b-%y");

      var x = d3.scaleBand()
        .rangeRound([0, width])
        .padding(0.1);

      var y = d3.scaleLinear()
        .rangeRound([height, 0]);

      var obj = {
        data: [4, 8, 15, 16, 23, 42],
        speed: [100, 50, 150, 80, 40, 20]
      };

      x.domain(obj.data.map(function (d) {
        return d;
      }));

      y.domain([0, d3.max(obj.speed, function (d) {
        return Number(d);
      })]);

      g.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x))

      g.append("g")
      .call(d3.axisLeft(y))
      .append("text")
      .attr("fill", "#000")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", "0.71em")
      .attr("text-anchor", "end")
      .text("Speed");

      g.selectAll(".bar")
      .data(obj.data)
      .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function (d) {
        return x(d);
      })
      .data(obj.speed)
      .attr("y", function (d) {
        return y(Number(d));
      })
      .attr("width", x.bandwidth())
      .attr("height", function (d) {
        return height - y(Number(d));
      });

        /**
        // format the data
        data.forEach(function(d) {
          d.sales = +d.sales;
        });

        // Scale the range of the data in the domains
        x.domain(data.map(function(d) { return d.salesperson; }));
        y.domain([0, d3.max(data, function(d) { return d.sales; })]);

        // append the rectangles for the bar chart
        svg.selectAll(".bar")
            .data(data)
          .enter().append("rect")
            .attr("class", "bar")
            .attr("x", function(d) { return x(d.salesperson); })
            .attr("width", x.bandwidth())
            .attr("y", function(d) { return y(d.sales); })
            .attr("height", function(d) { return height - y(d.sales); });

        // add the x Axis
        svg.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x));

        // add the y Axis
        svg.append("g")
            .call(d3.axisLeft(y));
        ***/
  })
  .then(() => {
      $(function() {
        $('[data-toggle="datepicker"]').datepicker({
            startDate: new Date(2018, 5, 8),
            endDate: new Date(2018, 5, 16),
            format: 'yyyy-mm-dd',
            pick: function (e) {
              renderGroupedBarChart(new Date(e.date).toISOString().slice(0,10))
            }
        });
      });
  })
  .catch(function(error){ 
    return error
  });
}