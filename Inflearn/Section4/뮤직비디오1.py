n,m=map(int,input().split())
music=list(map(int,input().split())

def Count(a): #함수 안 if문에서, a라는 dvd 용량은 어떤 노래보다도 크거나 같아야한다는 것을 뜻한다 
	sum=0 #누적 시간
	cnt=1 #dvd 한 장 일단 필요함
	for x in music:
		if sum+x>a: #x는 더이상 dvd에 넣을 수 없다
			cnt+=1 #새로운 dvd 추가
			sum=x #새로운 dvd에 x 시간 걸리는 곡 넣기
		else:		
			sum+=x
	return cnt

lt=0
rt=sum(music)
res=0
maxM=max(music)

while lt<=rt:
	mid=(lt+rt)//2
	if mid>=max and MCount(mid)<=m: #우리가 찾고자하는 dvd 용량은 최소한, 노래길이중 가장 긴 곡을 넣을 수 있어야한다
		res=mid
		rt=mid-1
	else:
		lt=mid+1

print(res)
		
	
