from time import time
n=20
def compute_average(n):
    data=[]
    start=time()
    for i in range(n):
        data.append(None)
        end=time()
        return(end-start)/n