from collections import deque

n=int(input())
a=list(map(int,input().split()))

a=deque(a)

b=[]
cnt=0
res=0

while a:
    left=a.popleft()
    right=a.pop
    if left<res and right<res:
        if left<right:
            cnt+=1
            b.append('L')
            res=right
        else:
            cnt+=1
            b.append('R')
            res=left

print(cnt)
print(b)      
            
