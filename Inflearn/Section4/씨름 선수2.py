n=int(input())

people=[]
for i in range(n):
	h,w=map(int,input().split())
	people.append((h,w))

people.sort(reverse=True)
#키 순으로 "내림차순 정렬"을 "한번만" 한다.
#그렇게 하면 아래 사람들은 몸무게만 "바로 위"의 사람보다 크면 되기 때문에

largest=0
cnt=0
for x,y in people:
	if y>largest:
		cnt+=1
		largest=y

print(cnt)
