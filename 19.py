a=int(input())
t=a
s=0
while a!=0:
    r=a%10
    s=s+r**3
    a=a//10
if(t==s):
    print('yes')
else:
    print('no')
