
# Partitioning a set
def make_partition(n,numberofparts):
    if (numberofparts < 2): return [(n,)]
    if (n<numberofparts): return []
    if (n==numberofparts): return [tuple([1 for i in range(1,n+1)])]
    partitions = []
    for i in range(1,n-numberofparts+2):
        partitions.extend([(i,) + v for v in make_partition(n-i,numberofparts-1)])
    return partitions


# Compute the c_0 (maximum) norm given a vector as a tuple
def c_0(v):
    return max(v)


# Compute the dot product given two tuple vectors
# If vector is length n then it assumes all entries 
#   after n are zero    
def dot(v1,v2):
    value = 0
    length = min(len(v1),len(v2))
    for i in range(0,length):
        value = value + v1[i]*v2[i]
    return value


# Compute the dot product given two tuple vectors
# If v1 and v2 have different length, altdot picks the 
#   partiton with the largest value
# In our application the vector will always be less than 
#   or equal to in length of the norming vectorof the norming 
def altdot(v1,v2):
    value = 0
    length = min(len(v1),len(v2))
    for i in range(0,length):
        value = value + v1[i]*v2[i]
    return value





# Computing the Bellenot norm of v (a tuple) using the 
#   given norming vector (a tuple)

def bellnorm(v, normingvector):
    length = len(v)
    nvlength = len(normingvector)
    if length == 0: return 0
    valuelist = [c_0(v)]
    if length >= 2:
        parts = make_partition(length, nvlength)
        for p in parts:
            p_plus = (0,)+p+(length,)
                #bp is the break points            
            bp = [sum([p_plus[j] for j in range(0,i)]) for i in range(1,len(p_plus)) ]                
            tempvectors = [v[bp[i]:bp[i+1]] for i in range(0,len(bp)-1) ]
            babyvec = tuple([bellnorm(tv, normingvector) for tv in tempvectors])
            valuelist.append(dot(babyvec,normingvector))
    return max(valuelist)        

def asn(v, normingvector):
    absv = tuple([abs(x) for x in v])
    return bellnorm(absv, normingvector)




