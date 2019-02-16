import ASNorm
import datetime #for the time
import numpy as np
import pandas as pd


n = 6 #Running with dimension n
nv = (3**(-.5),)*3  #Norming vector


def makenet(n):  #n is the dimension
	if n<2: return [ (i/10.0,) for i in range(11)]
	else: return [(i/10.0,)+v for i in range(11) for v in makenet(n-1)]

def makeshell(n):  #n is the dimension of the shell
	netn = makenet(n-1)
	return [a[0:i]+ (1.0,) + a[i:n]  for i in range(n+1) for a in netn]
	
startTime = datetime.datetime.now()







columns = ['vector', 'ASNorm', 'ENorm']
Rawdf  = pd.DataFrame(columns = columns)

for vec in makeshell(n):
	row = [vec, ASNorm.asn( vec, nv), np.linalg.norm(vec) ]
	Rawdf.loc[len(Rawdf)] = row
        
Rawdf['ASNorm'] = Rawdf['ASNorm'].apply(float)
Rawdf['ENorm'] = Rawdf['ENorm'].apply(float)

Rawdf['Ratio'] = Rawdf['ASNorm'] / Rawdf['ENorm']

maxrow = Rawdf[Rawdf['Ratio']==max(Rawdf['Ratio'])]
minrow = Rawdf[Rawdf['Ratio']==min(Rawdf['Ratio'])]

RMax = maxrow.iloc[0]
RMin = minrow.iloc[0]

with open('norms.txt', 'w') as f:
	f.write(str(RMax)) 
	f.write(str(RMin)) 



# make 
columns = ['x', 'y', 'ASNorm', 'ENorm', 'Ratio']


Plotdf = pd.DataFrame(columns = columns)

NumPoints = 100
for i in range(NumPoints+1):
	x = float(i)/NumPoints
	y = float(NumPoints-i)/NumPoints
	vec = tuple(x*np.array(RMax[0])+y*np.array(RMin[0]))
	row= [x,y, ASNorm.asn( vec, nv), np.linalg.norm(vec),  ASNorm.asn( vec, nv)/np.linalg.norm(vec)]
	print(row)
	Plotdf.loc[len(Plotdf)] = row


Plotdf['ASx'] = Plotdf['x'] /  Plotdf['ASNorm']
Plotdf['ASy'] = Plotdf['y'] /  Plotdf['ASNorm']
Plotdf['Ex'] = Plotdf['x'] /  Plotdf['ENorm']
Plotdf['Ey'] = Plotdf['y'] /  Plotdf['ENorm']


print(Plotdf)


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


plt.plot( 'ASx', 'ASy', data=Plotdf)
plt.plot( 'Ex', 'Ey', data=Plotdf)
plt.show()




timedelta = datetime.datetime.now() - startTime
print(timedelta)


