import bottle
import json
import data
import processing
import os.path


def load_data():
  csv_file = 'saved_data.csv'
  if not os.path.isfile(csv_file):
    url = 'https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27'
    info = data.json_loader(url)
    heads = ['date','location','administered_janssen','administered_moderna','administered_pfizer','administered_unk_manuf','series_complete_pop_pct']
    data.save_data(heads, info, 'saved_data.csv')
load_data()


@bottle.route("/")
def index():
  return bottle.static_file("index.html", root=".")

@bottle.route('/<js_file>.js')
def javascript_code(js_file):
  return bottle.static_file(js_file+".js", root=".")

@bottle.route("/barchart")
def bar_ch():
  bar_dat = processing.bar_chart()
  json_bar_data = json.dumps(bar_dat)
  return json_bar_data

@bottle.route("/piechart")
def pie_ch():
  pie_dat = processing.pie_chart()
  json_pie_data = json.dumps(pie_dat)
  return json_pie_data

@bottle.route("/linedata")
def line_data():
  line_dat = processing.line_data()
  json_line_data = json.dumps(line_dat)
  return json_line_data

@bottle.post("/linegraph")
def line_ch():
  blob = bottle.request.body.read().decode()
  blob = json.loads(blob)
  line_dat = processing.line_chart(blob)
  json_line_data = json.dumps(line_dat)
  return json_line_data



bottle.run(host = "0.0.0.0", port=8080,debug=True)
