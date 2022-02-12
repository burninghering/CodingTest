from collections import deque

n, limit=map(int, input().split())
p=list(map(int, input().split()))

p.sort()
p=deque(p)

cnt=0

while p:
    if len(p)==1:
        cnt+=1
        break
    if p[0]+p[-1]>limit: #제일 가벼운 사람, 제일 무거운 사람을 먼저 태우는 게 최선이라고 생각하심
        p.pop()
        cnt+=1
    else:
        p.popleft() #아니라면 양쪽 사람을 빼주고 배 1+ 
        p.pop()
        cnt+=1
print(cnt)

