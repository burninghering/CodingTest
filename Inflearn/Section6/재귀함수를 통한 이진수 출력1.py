n=int(input())

def DFS(n):
    if n==1:
        print(1,end='')
        return
    else:
        DFS(n//2)
        print(n%2,end='')

DFS(n)
