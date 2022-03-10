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
            print(hq.heappop(a))

    else:
        hq.heqppush(a, n)

#부모 노드는 항상 자식보다 작아야 하며,
#힙에서 자료를 꺼낼 때는 항상 루트노드가 빠져나간다.
#자료를 꺼내거나 집어넣을 때는 무조건 힙의 구조가 바뀐다.
#처음에 채워질 때는 순서대로 비워진 레벨에채워지나, 부모노드와 자식노드를 비교하여 제일 작은값을 위로 올린다 -> 최소힙 
            
        
        
    
