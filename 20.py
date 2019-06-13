a=int(input())
j=1
if a<0:
  print()
elif a==0:
  print("1")
else:
  for i in range(1,a+1):
    j=j*i
  print(j)
