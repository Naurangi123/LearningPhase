import sys # provides getsizeof function
data = [ ]
n=10
for k in range(n): # NOTE: must fix choice of n
    a = len(data) # number of elements
    b = sys.getsizeof(data) # actual size in bytes
    print("Length:{0:3d}; Size in bytes: {1:4d}" .format(a, b))
    data.append(None)