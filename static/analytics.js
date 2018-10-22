// Set the Dimensions
function renderGroupedBarChart(date) {
  var url;
  if(date){
    url = location.href + 'api?date=' + date;
  } else {
    url = location.href + 'api?date=all';
  }
  d3.selectAll("svg > *").remove(); // clear all svg elements before 
  d3.json(url,{
    method:"GET",
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  })
  .then((results) => {
      keys = [];
      values = [];
      var date = '';

      for(var key in results.data) {
        if(key != 'date') {
          keys.push(key);
          values.push(results.data[key].conversion_value__avg);
        } 
        if(key = 'date'){
          date = results.data[key];
        }
      }

      var title = 'Averages over all dates';
      if(date != 'all'){
        title= 'Averages on ' + date
      } 
      $("h1").remove();
      $('body').prepend("<h1>"+title+"</h1>")

      d3.select("svg").remove();
      var width = 960;
      var height = 500;
      var svg = d3.select("#chart")
        .append("svg").attr("width", width).attr("height", height),      
        margin = {top: 20, right: 20, bottom: 30, left: 40},
        width = +svg.attr("width") - margin.left - margin.right,
        height = +svg.attr("height") - margin.top - margin.bottom,
        g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

       // console.log(results);
      var parseTime = d3.timeParse("%d-%b-%y");

      var color = d3.scaleOrdinal()
      .range(["coral", "tomato", "orange"]);

      // Define the div for the tooltip
      var tooltip = d3.select("body")
        .append("div")
        .style("position", "absolute")
        .style("z-index", "10")
        .style("visibility", "hidden");

      var x = d3.scaleBand()
        .rangeRound([0, width])
        .padding(0.1);

      var y = d3.scaleLinear()
        .rangeRound([height, 0]);

      x.domain(keys.map(function (d) {
        return d;
      }));

      y.domain([0, d3.max(values, function (d) {
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
      .text("Conversion Value");

      g.selectAll(".bar")
      .data(keys)
      .enter().append("rect")
      .style("fill", function(d) { return color(d); })
      .attr("class", "bar")
      .attr("x", function (d) {
        return x(d);
      })
      .data(values)
      .attr("y", function (d) {
        return y(Number(d));
      })
      .attr("width", x.bandwidth())
      .attr("height", function (d) {
        return height - y(Number(d));
      })
      .on("mouseover", function(){
        return tooltip.style("visibility", "visible");
      })
      .on("mousemove", function(d){
        return tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px").html("<br>" + "Average Conversion Value: " + d);
      })
      .on("mouseout", function(){
        return tooltip.style("visibility", "hidden");
      });

      var legend = g.append("g")
          .attr("font-family", "sans-serif")
          .attr("font-size", 10)
          .attr("text-anchor", "end")
          .selectAll("g")
          .data(keys)
          .enter().append("g")
          .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

      legend.append("rect")
          .attr("x", width - 19)
          .attr("width", 19)
          .attr("height", 19)
          .attr("fill", color);

      legend.append("text")
          .attr("x", width - 24)
          .attr("y", 9.5)
          .attr("dy", "0.32em")
          .text(function(d) { return d; });

      return results;
   
  })
  .then((results) => {
      $(function() {
        $('[data-toggle="datepicker"]').datepicker({
            startDate: new Date(results.mindate),
            endDate: new Date(results.maxdate),
            format: 'yyyy-mm-dd',
            pick: function (e) {
              renderGroupedBarChart(new Date(e.date).toISOString().slice(0,10))
            }
        });
      });
  })
  .catch(function(error){ 
    throw error
  });
}