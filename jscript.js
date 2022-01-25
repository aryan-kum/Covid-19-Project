"use strict";
var hi;
var va;
function data(){
  ajaxGetRequest("barchart", bar);
  ajaxGetRequest("piechart", pie);
}
function data_line_chart(){
  hi = document.getElementById("stuff");
  va = hi['value'];
  let json = JSON.stringify(va);
  ajaxPostRequest("linegraph", json, line);
}
function line(hello){
  let data = JSON.parse(hello);
  let p_list = data[1]; 
  let d_list = data[0];
  let trace = {
  x: d_list,
  y: p_list,
  type: 'scatter'
};
let format = {
    title: "% of " + va + " Fully Vaccinated by Date",
    xaxis: {title: "Date"},
    yaxis: {title: "% Fully Vaccinated"}
  };

let data2 = [trace];

Plotly.newPlot('linegr', data2, format); 
}
function bar(hello){
  let data = JSON.parse(hello);
  let p_list = [];
  let l_list = [];
  p_list.push(data[1]);
  l_list.push(data[0]);

  let chart = [
  {
    x: data[0],
    y: data[1],
    type: 'bar'
  }
];
  let format = {
    title: "Fully Vaccinated By Location",
    xaxis: {title: "Location"},
    yaxis: {title: "% Fully Vaccinated"}
  };
Plotly.newPlot('barch', chart, format);
}

function pie(hello){
  let data = JSON.parse(hello);
  let val = [
  {
    values: data,
    labels: ['Janssen', 'Unknown', 'Pfizer', 'Moderna'],
    type: 'pie'
  }
];
  let format = {
    title: "Vaccine Manufacturer Market Share",
  };
Plotly.newPlot('piech', val, format);
}
