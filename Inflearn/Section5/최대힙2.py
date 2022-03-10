import heapq as hq

a=[]

while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(-hq.heappop(a))

    else:
        hq.heqppush(a, -n)

#힙은 기본적으로 최소 힙으로 작동함
#그러므로 최대힙을 하려면 push를 할때 요소에 -를 붙인다 
