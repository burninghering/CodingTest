from collections import deque
a=input()

n=int(input())

for i in range(n):
    c=input()
    q=deque(n)

    for x in c:
        if x in q:
            if x!=q.popleft():
                print("NO")
                break
    else:
        if len(q)==0:
            #len이 0?
        
