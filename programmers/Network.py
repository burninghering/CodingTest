def solution(n, computers):
    def dfs(s):
        ch[s]=True
        for i in a[s]:
            if ch[i]==False:
                dfs(i)
                
    a=[[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1:
                a[i].append(j)
                a[j].append(i)
                
    ch=[False]*n
    count=0
    for i in range(n):
        if ch[i]==False:
            count+=1
            dfs(i)
    return count

