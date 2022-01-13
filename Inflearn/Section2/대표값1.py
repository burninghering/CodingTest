n=int(input())
math=list(map(int,input().split()))

s=round(sum(math)/n)

ans=[]
for i in range(n):
  if math[i]>=s:
    ans.append(math[i])

ans.sort()
print(s, math.index(ans[0])+1)
