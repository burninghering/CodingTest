n,c=map(int,input().split())
Line=[int(input()) for _ in range(n)]
Line.sort()

def Count(len):
	cnt=1 #말 한마리 일단 첫 번째에 배치
	endPoint=Line[0]
	for i in range(1,n):
		if Line[i]-endPoint>=len:
			cnt+=1
			endPoint=Line[i]
	return cnt
			
lt=Line[0]
rt=Line[-1]

while lt<=rt:
	mid=(lt+rt)//2
	if Count(mid)>=c:
		res=mid
		lt=mid+1
	else:
		rt=mid-1

print(res)