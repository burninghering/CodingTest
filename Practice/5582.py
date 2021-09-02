a=input()
b=input()
n=len(a)
m=len(b)

a=' '+a #인덱스 1부터 시작해야, i-1을 할 때 범위를 안벗어나니까
b=' '+b

d=[[0]*(m+1) for _ in range(n+1)]
v=[[0]*(m+1) for _ in range(n+1)]


for i in range(1,n+1):
  for j in range(1,m+1):
    if a[i]==b[j]:
      d[i][j]=d[i-1][j-1]+1
      v[i][j]=1
    else:
      d[i][j]=0

ans=0
for i in range(n+1):
  for j in range(m+1):
    if ans<d[i][j]:
      ans=d[i][j]
print(ans)

#https://www.acmicpc.net/problem/5582
