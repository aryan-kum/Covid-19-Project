import csv
import json
import urllib.request


def json_loader(x):
  response=urllib.request.urlopen(x)
  content_string=response.read().decode()
  return json.loads(content_string)




def make_values_numeric(x, y):
  for xx in x:
    for keys in y:
      if xx == keys:
        y[keys] = float(y[keys])
  
  return y





def save_data(x, y, z):
  n_list = []
  with open(z, "w") as fw:
    writer = csv.writer(fw)
    writer.writerow(x)
    n_list = make_lists(x, y)
    for something in n_list:
      writer.writerow(something)




def load_data(x):
  big_list = []
  nn_list = []
  with open(x) as fr:
    reader = csv.reader(fr)
    for line in reader:
      n_list= []
      for index in line:
        n_list.append(index)
      nn_list.append(n_list)
  nnn_list = nn_list.pop(0)
  for a in nn_list:
    dic = {}
    for bb, cc in zip(a, nnn_list):
      dic[cc]=bb
    big_list.append(dic)
  return big_list      





def dic_list_gen(x, y):
  b = {}
  a = []
  count = 0
  if len(x) != 1:
    for yyy in y:
      b={}
      count = 0
      for xxx in x:
        b[xxx] = yyy[count]
        count = count+1 
      a.append(b)
  else:
    for xxx in x:
      for yyy in y:
        b = {}
        b[xxx]=yyy[0]
        a.append(b)
  return a





def read_values(x):
  a = []
  with open(x) as fp:
    reader = csv.reader(fp)
    header = next(reader)
    for line in reader:
      a.append(line)  
  return a





def make_lists(x, y):
  aa = []
  for yy in y:
    a = []
    for xx in x:
      a.append(yy.get(xx))
    aa.append(a)
  return aa





def write_values(x, y):
  with open(x, "a") as fw:
    writer = csv.writer(fw)
    for yy in y:
      writer.writerow(yy)


