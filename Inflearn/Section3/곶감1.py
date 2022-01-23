n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

m=int(input())
for _ in range(m): 
  x,y,z=map(int,input().split())
  if y==0:
    a[x-1]=a[x-1][z:]+a[x-1][0:z]
  else:
    a[x-1]=a[x-1][n-z:]+a[x-1][:n-z]


res=0                                                                                               
s=0
e=n

for i in range(n):
  for j in range(s,e):
    res+=a[i][j]
  
  if i<n//2:
    s+=1
    e-=1

  else:
    s-=1
    e+=1

    
print(res)

