dx=[1,-1,0,0]
dy=[0,0,1,-1]

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
a=[[False]*n for _ in range(n)]

cnt=0
for x in range(n):
  for y in range(n):
    
    for k in range(4):
      nx=x+dx[k]
      ny=y+dy[k]
      if nx>=0 and nx<n and ny>=0 and ny<n:
        
       
        if a[nx][ny]<a[x][y]:
          if a[x][y]:
            continue
          a[x][y]=True
          cnt+=1

print(cnt)
