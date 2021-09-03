import sys

def go(a,x,d,k):
  if d==0:
    a[x]=a[x][-k:]+a[x][:-k] # 4+123
  else:
    a[x]=a[x][k:]+a[x][:k] #234+1
  

def check(a):
  n=len(a)-1 #None 빼주기
  m=len(a[1])

  d=[[False]*m for _ in range(n+1)]

  ok=False

  for i in range(1,n+1):
    for j in range(m):
      if a[i][j]==0:
        continue
      if a[i][j]==a[i][(j+1)%m]:
        d[i][j]=d[i][(j+1)%m]=True
      if i+1<=n and a[i][j]==a[i+1][j]: #범위 조건을 무조건 앞에 두자
        d[i][j]=d[i+1][j]=True

  for i in range(1,n+1):
    for j in range(m):
      if d[i][j]:
        ok=True
        a[i][j]=0
  
  return ok

def adjust(a):
  n=len(a)-1
  m=len(a[1])
  total=0
  cnt=0
  for i in range(1,n+1):
    for j in range(m):
      if a[i][j]==0:
        continue
      total+=a[i][j]
      cnt+=1
  
  if cnt==0:
    return

  for i in range(1,n+1):
    for j in range(m):
      if total/cnt>a[i][j]:
        a[i][j]+=1
      elif total/cnt<a[i][j]:
        a[i][j]-=1
        
n,m,t=map(int,input().split())
a=[None]+[list(map(int,input().split())) for _ in range(n)]

for _ in range(t):
  x,d,k=map(int,input().split())

  for y in range(x,n+1,x):
    go(a,y,d,k)
  
  ok=check(a)

  if ok==False:
    adjust(a)

ans=sum(sum(row) for row in a[1:])
print(ans)

#https://www.acmicpc.net/problem/17822
