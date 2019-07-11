aa1=int(input())
aa2=input()
aa4=["a","e","i","o","u"]
aa3=[]
for i in aa2:
    if i not in aa4:
        aa3.append(i)
print(''.joins(aa3[::-1]))
