a1='qwertyuiopasdfghjklzxcvbnm'
a2='mnbvcxzlkjhgfdsapoiuytrewq'
b1=''
c1=input()
for i in c1:
    b1=b1+a2[a1.index(i)]
print(b1.upper())
b2=''
for i in b1:
    b2=b2+a1[a2.index(i)]
print(b2)
