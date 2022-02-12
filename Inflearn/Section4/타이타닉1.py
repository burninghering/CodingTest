n,m=map(int,input().split())
a=list(map(int,input().split()))

a.sort()

cnt=0
for i in range(n):
    if m-a[i]>0:
        m-=a[i]
        continue
    else:
        m=m
        cnt+=1
    

print(cnt)
