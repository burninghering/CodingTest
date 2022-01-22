n=int(input())

a=[list(map(int,input().split())) for _ in range(n)]

sum=0
ans=-1
for i in range(n):
  for j in range(n):
    sum+=a[i][j]
  if sum>ans:
    ans=sum
  sum=0

for i in range(n):
  for j in range(n):
    sum+=a[j][i]
  if sum>ans:
    ans=sum
  sum=0

i=0
for j in range(n-1,-1,-1):
  sum+=a[i][j]
  i+=1

if sum>ans:
  ans=sum

sum=0
i=0
for j in range(n):
  sum+=a[i][j]
  i+=1

if sum>ans:
  ans=sum

print(ans) 
