def DFS(L,s,sum):
	global cnt
	if L==k:	#L이란 변수를 넣을 생각을 못함
		if sum%m==0:
			cnt+=1
			return
	else:
		for i in range(s,n):
			DFS(L+1,i+1,sum+a[i])

n,k=map(int,input().split())
a=list(map(int,input().split()))
m=int(input())
cnt=0
DFS(0,0,0)
print(cnt)
