import time
n,m=map(int,input().split())
start = time.time()

cnt=[0]*(n+m+3)
for i in range(1,n+1):
  for j in range(1,m+1):
    cnt[i+j]+=1

x=max(cnt)

for i in range(len(cnt)):
  if cnt[i]==x:
    print(i,end=' ')
print()
end = time.time()
print(f"{end - start:.5f} sec")
