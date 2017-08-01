import numpy as np
import uuid
import csv
import os
outfile = 'bigboy.csv'
outsize = 1024 # MB
with open(outfile, 'ab') as csvfile:
    wtr = csv.writer(csvfile)
    while (os.path.getsize(outfile)//1024**2) < outsize:
        wtr.writerow(['%s,%.6f,%.6f,%i' % (uuid.uuid4(), np.random.random()*50, np.random.random()*50, np.random.randint(1000))])
