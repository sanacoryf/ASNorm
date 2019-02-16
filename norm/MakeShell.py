from sys import argv
args = argv  #args[1] will be the dimension

if len(args)<2:
	N = 3 #Running with dimension n
else:
	N = int(args[1])
	
	



def makenet(n):  #n is the dimension
	if n<2: return [ (i/10.0,) for i in range(11)]
	else: return [(i/10.0,)+v for i in range(11) for v in makenet(n-1)]

def makeshell(n):  #n is the dimension of the shell
	netn = makenet(n-1)
	return [a[0:i]+ (1.0,) + a[i:n]  for i in range(n+1) for a in netn]
	

with open('shell.txt', 'w') as file_handler:
    for item in makeshell(N):
        file_handler.write("{}\n".format(item))


