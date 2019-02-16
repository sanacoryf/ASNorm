


def makenet(n):  #n is the dimension
	if n<2: return [ (i/10.0,) for i in range(11)]
	else: return [(i/10.0,)+v for i in range(11) for v in makenet(n-1)]

def makeshell(n):  #n is the dimension of the shell
	netn = makenet(n)
	return [a[0:i]+ (1,) + a[i:n]  for i in range(n+1) for a in netn]
	



#print(makenet(3))
'''
N = 2
netN = makenet(N)
shellN = [a[0:i]+ (1,) + a[i:N]  for i in range(N+1) for a in netN]

for item in shellN:
	print(item)

print(N, len(netN), len(shellN))
'''

N = 3
netN = makenet(N)
shellN = makeshell(N)


for vec in shellN:
	print(tuple([i*2 for i in vec]))

print(N, len(netN), len(shellN))




