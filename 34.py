from itertools import combinations
y1,v1=map(int,input().split())
w=len(str(y1))
x=list(combinations(str(y1),w-v1))
x=(sorted(x))
y="".join(x[0])
print(y)
