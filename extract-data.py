#importing some libraries
import os
import csv
from datetime import datetime
#Timestamp
dt = datetime.now()
ts = datetime.timestamp(dt)
#Declaring some variables
txtdir = 'C:/Users/Overlord/git-repos/Web-scrap/texts'
all_files = os.listdir(txtdir)
tyear = "Año:"
ttittle = "Titulo"
tresolution = "Resolución: "
exttxt = ".txt"
filename = "titleyear.{}.csv".format(ts)
#initialize new array
newlist = []
#functions
def search_string(file_name, string_searchg):
    lines = []
    with open(file_name, 'r', encoding="utf-8") as f:
        lines = f.readlines
    count = 0
    list_results = []
    final_result = []
    for line in lines:
        count += 1
        d = {}
        if string_searchg in line:
            llist = line.strip()
            d['line'] = count
            d['text'] = llist
        list_results.append(d)
        for elem in list_results:
            print(elem)
            final_result.append(elem)
for file in all_files:
    ffile = "{}".format(file.removesuffix(exttxt))
    dirfile = "{}{}{}".format(txtdir,'/',file)
    result_final = search_string(dirfile, ttittle)
newlist.append(result_final)