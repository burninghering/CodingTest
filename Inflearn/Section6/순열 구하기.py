def DFS(x):
    global cnt
    if x==m:
        for i in range(m):
            print(a[i],end=' ')
        print()
        cnt+=1
    else:
        for i in range(x+1,n+1):
            a[x]=i
            DFS(x+1)

n,m=map(int,input().split())
cnt=0
a=[0]*n
DFS(0)
print(cnt)

