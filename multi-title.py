import numpy as np
import os
import csv
from datetime import datetime
dt = datetime.now()
ts = datetime.timestamp(dt)
txtdir = 'multi-title'
all_files = os.listdir(txtdir)
tyear = "Año:"
ttittle = "Titulo"
tresolution = "Resolución: "
exttxt = ".txt"
newlist = []
filename = "newtitle.{}.csv".format(ts)
def search_multi_line(file_name, string_to_search):
	line_number = 0
	list_of_results = []
	with open(file_name, 'r', encoding="utf-8") as read_obj:
		for line in read_obj:
			line_number += 1
			d = {}
			if string_to_search in line:
				uniline = line.strip()
				d['line'] = line_number
				d['text'] = uniline
			list_of_results.append(d)

for file in all_files:
    ffile = "{}".format(file.removesuffix(exttxt))
    dirfile = "{}{}{}".format(txtdir,'/',file)
    result_final = search_multi_line(dirfile, ttittle)
newlist.append(result_final)
