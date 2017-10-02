#!/usr/bin/env python

import sqlite3
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

db = sqlite3.connect('wigle')
c = db.cursor()

c.execute('SELECT lat,lon FROM location')
data = c.fetchall()
lats = [d[0] for d in data]
lons = [d[1] for d in data]

#print data



m = Basemap(projection='moll',lon_0=0,resolution='c')
x, y = m(lons,lats)
m.scatter(x,y,3,marker='o',color='k')
plt.show()

# Don't forget to zoom in
