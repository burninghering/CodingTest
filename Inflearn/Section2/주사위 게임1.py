import time

t=int(input())

start=time.time()

total_money=[]
for _ in range(t):
  a=list(map(int,input().split()))
  
  cnt=0
  same=[]
  for i in range(1,3):
    if a[i-1]==a[i]:
      cnt+=1
      same.append(a[i])

  money=0
  if cnt==2:
    money=10000+a[0]*1000
  elif cnt==1:
    money=1000+same[0]*100
  else:
    money=100*max(a)

  total_money.append(money)

print(max(total_money))

end=time.time()
print(f"{end-start:0.5f} sec")

#0.07112 sec
