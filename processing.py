import data
import csv
import json
import urllib.request

def max_value(dic, ky):
  largest_str = ""
  for a in dic:
    for b in a.keys():
      if b == ky:
        if str(a.get(ky)) > str(largest_str):
          largest_str = str(a.get(ky))
  return largest_str


def init_dictionary(x, y):
  new = {}
  for a in x:
    for b in a.keys():
      if b==y:
        v = a.get(b)
        new[v]=0
  return new



def sum_matches(lod, k, v, tgt):
  sum = 0
  for a in lod:
    if a.get(k) == v:
      sum = sum + float(a.get(tgt))

  return float(sum)



def copy_matching(lod, k ,v):
  new = []
  for a in lod:
    if a.get(k) == v:
      new.append(a)
  return new


def bar_chart():
  total_data = data.load_data("saved_data.csv")
  max_val = max_value(total_data, 'date')

  max_dic = copy_matching(total_data, 'date', max_val)

  bar_data = data.make_lists(['location','series_complete_pop_pct'], max_dic)

  both_lst = []
  loc_lst = []
  pop_lst = []
  for x in bar_data:
    loc_lst.append(x[0])
    pop_lst.append(x[1])
  both_lst.append(loc_lst)
  both_lst.append(pop_lst)
  return both_lst

def pie_chart():
  n_list = []
  per_pf = 0.0
  per_mod = 0.0
  per_unk = 0.0
  per_jan = 0.0
  total_adm = 0
  total_mod = 0
  total_pf = 0
  total_jan = 0
  total_unk = 0
  total_data = data.load_data("saved_data.csv")
  max_val = max_value(total_data, 'date')

  max_dic = copy_matching(total_data, 'date', max_val)

  for a in max_dic:
    total_adm = total_adm + int(a['administered_janssen']) + int(a['administered_moderna']) + int(a['administered_pfizer']) + int(a['administered_unk_manuf'])
    total_mod = total_mod + int(a['administered_moderna'])
    total_pf = total_pf + int(a['administered_pfizer'])
    total_jan = total_jan + int(a['administered_janssen'])
    total_unk = total_unk + int(a['administered_unk_manuf'])
  per_jan = total_jan/total_adm * 100
  per_unk = total_unk/total_adm * 100
  per_mod = total_mod/total_adm * 100
  per_pf = total_pf/total_adm * 100
  n_list.append(per_jan)
  n_list.append(per_unk)
  n_list.append(per_pf)
  n_list.append(per_mod)
  return n_list

def key_line(dic):
  return dic['date']
def line_chart(location):
  both_list = []
  p_list = []
  d_list = []
  total_data = data.load_data("saved_data.csv")
  total_data.sort(key=key_line)
  for a in total_data:
    if(a['location'] == location):
      d_list.append(a['date'])
      p_list.append(a['series_complete_pop_pct'])
  both_list.append(d_list)
  both_list.append(p_list)
  return both_list

def line_data():
  total_data = data.load_data("saved_data.csv")
  total_data.sort(key=key_line)
  return total_data
