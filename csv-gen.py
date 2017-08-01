import numpy as np
import uuid
import csv
import os
outfile = 'bigboy.csv'
outsize = 10 # MB
chunksize = 1000
with open(outfile, 'ab') as csvfile:
    while (os.path.getsize(outfile)//1024**2) < outsize:
        data = [[uuid.uuid4() for i in range(chunksize)],
                np.random.random(chunksize)*50,
                np.random.random(chunksize)*50,
                np.random.randint(1000, size=(chunksize,))]
        csvfile.writelines(['%s,%.6f,%.6f,%i\n' % row for row in zip(*data)])
