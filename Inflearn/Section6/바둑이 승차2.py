import sys
from collections import deque

def DFS(x,sum,tsum):
    global result
    #sum : 내가 지금까지 만든 부분집합들의 합
    #(total-tsum) : 앞으로 판단해야할 바둑이들의 총 무게
    #sum+(total-tsum) : 현재까지 판단해온 바둑이들의 총 무게 
    
    if sum+(total-tsum)<result: #result보다 좋은 답이 나오지 않는다면
        return
    
    if sum>c:
        return
    
    if x==n:
        if sum>result:
            result=sum
    else:
        DFS(x+1,sum+a[x],tsum+a[x])
        DFS(x+1,sum,tsum+a[x]) #부분집합에 넣지 않았어도 tsum에 일단 넣는

if __name__=="__main__":
    c,n=map(int,input().split())
    a=[0]*n
    result=-2147000000

    for i in range(n):
        a[i]=int(input())

    total=sum(a)
    DFS(0,0,0)
    print(result)
