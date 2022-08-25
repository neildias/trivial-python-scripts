x =  list(range(1000))
import sys

sys.setrecursionlimit(150000)

def rev1(x):
    y = list(range(len(x)))
    indexer = 0
    for i in range(len(x)-1, 0, -1):
        y[indexer] = x[i]
        indexer +=1
    return y

def rev2(x):
    if not x: return []
    return [x[-1]] + rev2(x[:-1])

def rev3(x):
    # if not len(x)%2==0:
    stop_after = int(len(x) // 2) 
    reverse_index = len(x) - 1
    for index, _ in enumerate(x):
        if index+1 > stop_after:
            break
        x[index], x[reverse_index] = x[reverse_index], x[index]
        reverse_index-=1
    return x

import time

def timeit(func,lister):
    start = time.time()
    x = func(lister)
    stop = time.time()
    print(stop-start)
    return x


print("forloop")
timeit(rev1,x)

print("halfloop")
timeit(rev3,x)
print("recursion")
timeit(rev2,x)
