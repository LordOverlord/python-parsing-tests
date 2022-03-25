from asyncio.windows_events import NULL
import os
import csv
from datetime import datetime
dt = datetime.now()
ts = datetime.timestamp(dt)
txtdir = 'C:/Users/Overlord/git-repos/Web-scrap/texts'
all_files = os.listdir(txtdir)
tyear = "Año:"
ttittle = "Titulo"
tresolution = "Resolución: "
exttxt = ".txt"
filename = "titleyear.{}.csv".format(ts)
newlist = []
for file in all_files:
    global ffile 
    ffile = "{}".format(file.removesuffix(exttxt))
    dirfile = "{}{}{}".format(txtdir,'/',file)
    f = open(dirfile, 'r', encoding="utf-8")
    content = f.read()
    d = {}
    d['File'] = ffile
    for item in content.split("\n"):
        if ttittle in item:
            mtitle = item.strip()
            d['Title'] = mtitle
    for item in content.split("\n"):
        if tyear in item:
            tempy = item.strip()
            myear = "{}".format(tempy.removeprefix(tyear))
            d['Year'] = myear
    newlist.append(d)
    content = NULL
    mtitle = NULL
    myear = NULL
    ffile = NULL
with open(filename,'w', newline='', encoding="utf-8") as f:
    w = csv.DictWriter(f,['File','Title','Year'])
    w.writeheader()
    w.writerows(newlist)