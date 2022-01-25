dx=[1,-1,0,0]
dy=[0,0,1,-1]

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

a.insert(0,[0]*n) #위 0 다섯개 -> 행 1개 추가 
a.append([0]*n) #아래 0 다섯개 -> 행 1개 추가

for x in a:
  x.insert(0,0) #행마다 0 앞에 추가 (왼쪽)
  x.append(0)   #행마다 0 뒤에 추가 (오른쪽)

cnt=0
for x in range(1,n+1):
  for y in range(1,n+1):
    
    if all(a[x][y]>a[x+dx[k]][y+dy[k]] for k in range(4)):
      # all 함수란 ()안의 결과가 모두 True여야 True 반환
      cnt+=1
      

print(cnt)
