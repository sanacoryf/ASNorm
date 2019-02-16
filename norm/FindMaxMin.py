import ASNorm
#import datetime #for the time
import numpy as np
import pandas as pd
from mpi4py import MPI
import sys

nv = (3**(-.5),)*3  #Norming vector

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()


columns = ['vector', 'ASNorm', 'ENorm']
Rawdf  = pd.DataFrame(columns = columns)

#modulus and remainder
modulus = size
remainder = rank


count = 0
with open('shell.txt', 'r') as file_handler:
    for line in file_handler:
		count +=1
		if (count%modulus==remainder):
			vec = tuple(map(float, line[1:-2].split(',')))         
			row = [vec, ASNorm.asn( vec, nv), np.linalg.norm(vec) ]
			Rawdf.loc[len(Rawdf)] = row

        
Rawdf['ASNorm'] = Rawdf['ASNorm'].apply(float)
Rawdf['ENorm'] = Rawdf['ENorm'].apply(float)

Rawdf['Ratio'] = Rawdf['ASNorm'] / Rawdf['ENorm']

maxrow = Rawdf[Rawdf['Ratio']==max(Rawdf['Ratio'])]
minrow = Rawdf[Rawdf['Ratio']==min(Rawdf['Ratio'])]

RMax = maxrow.iloc[0]
RMin = minrow.iloc[0]


filename = 'output/vec'&str(remainder)&'.txt'

with open(filename, 'w') as f:
	f.write(str(RMax)) 
	f.write(str(RMin)) 




sys.stdout.write(
    "Hello, World! Process %d of %d on %s is complete.\n"
    % (rank, size, name))
