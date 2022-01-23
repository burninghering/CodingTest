n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

res=0
s=e=n//2 #인덱스의 규칙성을 변수로 표현할 생각을 못했다..!

for i in range(n):
  for j in range(s,e+1):
    res+=a[i][j] #설명 후 여기까지만 구현 성공 
  
  if i<n//2: #if문을 사용하면 되는구나!
    s-=1
    e+=1

  else:
    s+=1 
    e-=1 


print(res)
