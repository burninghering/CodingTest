from collections import deque
a=input()

n=int(input())

for i in range(n):
    plan=input()
    q=deque(n)

    for x in plan:
        if x in q:
            if x!=q.popleft():
                print("#%d NO" %(i+1))
                break

    else:
        if len(q)==0: #큐(필수 과정)가 비어있어야만 필수 과정을 교육 과정에 넣은 것
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
            
            
        
