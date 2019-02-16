import ASNorm
import datetime #for the time
n = 5
nv = (3**(-.5),)*3



def makenet(n):  #n is the dimension
	if n<2: return [ (i/10.0,) for i in range(11)]
	else: return [(i/10.0,)+v for i in range(11) for v in makenet(n-1)]



with open("net.txt", "w") as f: 
    for i in makenet(n):
        f.write(str(i)[1:-1]+"\n") 



with open('net.txt', 'r') as f:
    for count, line in enumerate(f, start=1):
        if count % 128 == 0:
			print(line, ASNorm.asn( tuple(map(float, line.split(','))), nv) )


