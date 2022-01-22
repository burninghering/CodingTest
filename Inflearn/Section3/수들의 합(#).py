n,m=map(int,input().split())
a=list(map(int,input().split()))

lt=0
rt=1
tot=a[0] #lt와 rt까지의 합
cnt=0

while True:
  if tot<m:
    if rt<n:
      tot+=a[rt]
      rt+=1
    else:
      break

  elif tot==m:
    cnt+=1
    tot-=a[lt]
    lt+=1
  else:
    tot-=a[lt]
    lt+=1

print(cnt)

#수열 A[i]~A[j] 까지의 합이므로, 뽑아서 하는게 아닌
#투 포인터로 접근해야 하는 문제 
