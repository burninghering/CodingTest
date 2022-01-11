import time

start=time.time()
n,k=map(int,input().split())

cnt=0
for i in range(1,n):
  if n%i==0:
    cnt+=1
    if cnt==k:
      print(cnt)
      break

end=time.time()
print(f"{end-start:.5f} sec")
