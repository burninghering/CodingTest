from collections import deque

#처음 4개 : 상하좌우 / 다음 8개 : 나이트 이동
dx = [0,0,1,-1,-2,-1,1,2,2,1,-1,-2] 
dy = [1,-1,0,0,1,2,2,1,-1,-2,-2,-1]

l=int(input())
m,n=map(int,input().split()) #가로길이는 열, 세로 길이는 행!
a=[list(map(int,input().split())) for _ in range(n)]
dist=[[[-1]*31 for _ in range(200)] for _ in range(200)]
cost = [0,0,0,0,1,1,1,1,1,1,1,1] #이동과 가중치를 같이!

q=deque()
dist[0][0][0]=0
q.append((0,0,0))

while q:
  x,y,c=q.popleft()
  
  for k in range(12):
    nx,ny,nc=x+dx[k],y+dy[k],c+cost[k]
    if 0<=nx<n and 0<=ny<m:
      if a[nx][ny]==1:
        continue
      if nc<=l:
        if dist[nx][ny][nc]==-1:
          dist[nx][ny][nc]=dist[x][y][c]+1
          q.append((nx,ny,nc))

ans=-1
for i in range(l+1):
  if dist[n-1][m-1][i]==-1:
    continue
  if ans==-1 or ans>dist[n-1][m-1][i]:
    ans=dist[n-1][m-1][i] 
print(ans) 

#https://www.acmicpc.net/problem/1600
