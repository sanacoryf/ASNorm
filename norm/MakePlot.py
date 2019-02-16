import ASNorm
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
nv = (3**(-.5),)*3  #Norming vector




filename = 'allVec.txt'


columns = ['vec', 'ASNorm', 'ENorm', 'Ratio']
df = pd.DataFrame(columns = columns)

with open(filename, 'r') as f:
	for line in f:
		two = line.split(')')
		if len(two)==2:
			vec = two[0]
			others = two[1].split(',')
			row = [tuple(map(float, vec[1:].split(',')))]
			row = row + list(map(float, others[1:]))
			df.loc[len(df)] =  row
	

df = df.sort_values(by=['Ratio'])
RMin = df.iloc[0]
RMax = df.iloc[len(df)-1]


print 'Vector with maximum Ratio is ',RMax[0],' with Ratio of ',RMax[3] 
print 'Vector with minimum Ratio is ',RMin[0],' with Ratio of ',RMin[3]

columns = ['x', 'y', 'ASNorm', 'ENorm', 'Ratio']
Plotdf = pd.DataFrame(columns = columns)


Plotdf = pd.DataFrame(columns = columns)

NumPoints = 100
for i in range(NumPoints+1):
	x = float(i)/NumPoints
	y = float(NumPoints-i)/NumPoints
	vec = tuple(x*np.array(RMax[0])+y*np.array(RMin[0]))
	row= [x,y, ASNorm.asn( vec, nv), np.linalg.norm(vec),  ASNorm.asn( vec, nv)/np.linalg.norm(vec)]
	Plotdf.loc[len(Plotdf)] = row


Plotdf['ASx'] = Plotdf['x'] /  Plotdf['ASNorm']
Plotdf['ASy'] = Plotdf['y'] /  Plotdf['ASNorm']
Plotdf['Ex'] = Plotdf['x'] /  Plotdf['ENorm']
Plotdf['Ey'] = Plotdf['y'] /  Plotdf['ENorm']



plt.plot( 'ASx', 'ASy', data=Plotdf)
plt.plot( 'Ex', 'Ey', data=Plotdf)
#plt.show()
plt.savefig('myfig.png')
