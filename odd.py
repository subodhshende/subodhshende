l=[]
a=int(input('enter no:'))
print('enter no:',a,'no. into the list:')
i=0
for i in range(a+1):
    x=int(input())
    l.append(x)
    i=i+1
j=0
while j<a:
    if l[j]%2!=0:
        print(l[j])
    j+=1
