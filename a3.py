p1=input()
q1=len(p1)
r1=""
for i in range (q1):
  if((i%2)==0):
    r1+=p1[i+1]
  else:
    r1+=p1[i-1]
print (r1)
