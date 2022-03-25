import os
import csv
import pandas as pd
import numpy
from datetime import datetime
dt = datetime.now()
ts = datetime.timestamp(dt)
txtdir = 'C:/Users/Overlord/git-repos/Web-scrap/texts/'
sourcedir = 'C:/Users/Overlord/git-repos/Web-scrap/'
all_files = os.listdir(txtdir)
ttitle = "Titulo"
exttxt = ".txt"
newlist = []
filename = "{}multi.line.{}.csv".format(sourcedir,ts)
def readmultiple(logfile,searchstring):
    with open(logfile, encoding="utf-8") as search:
        count = 0
        d = {}
        for line in search:
            line = line.rstrip()
            if searchstring in line:
                count += 1
        if count >= 2:
            print(dirfile)
            offender = dirfile
            d['File'] = offender
        newlist.append(d)
for file in all_files:
    dirfile = "{}{}".format(txtdir,file)
    readmultiple(dirfile, ttitle)
with open(filename,'w', newline='', encoding="utf-8") as f:
    w = csv.DictWriter(f,['File'])
    w.writeheader()
    w.writerows(newlist)
