#최대힙은 부모의 노드값이 두 자식의 노드값보다 커야함
#힙에 push할 때, 레벨 순으로 입력된 뒤 자식노드랑 비교(업힙)

import heapq as hq

#힙을 만들려면 리스트가 하나 필요함
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
			#루트 노드의 값을 pop하고 무조건 최소힙 만듦
			#그러므로 부호를 바꿔서 넣으면 최대힙이 된다

	else:
		hq.heappush(a,-n)
		#heappush를 하면 무조건 최소힙
		#부호를 바꿔서 넣자
		
