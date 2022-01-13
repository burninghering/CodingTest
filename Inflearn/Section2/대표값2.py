import time
n=int(input())
math=list(map(int,input().split()))
start = time.time()
s=round(sum(math)/n)

ans=[]
for index,value in enumerate(math):
  if value>=s:
    ans.append((value,index))

ans.sort()
print(s, ans[0][1]+1)

end = time.time()
print(f"{end - start:.5f} sec")
