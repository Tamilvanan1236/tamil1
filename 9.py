c1=int(input())
if(c1%4==0):
  if(c1%400==0):
    if(c1%100!=0):
      print("yes")
  else:
    print("yes")
else:
  print("no")
