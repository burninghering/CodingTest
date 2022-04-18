#힙은 완전이진트리로 구현된 자료구조
#힙은 부모의 노드값이 자식의 노드값보다 작아야함
#힙에 push할 때, 레벨 순으로 입력된 뒤 부모노드랑 비교(업힙)
#최소힙 완성
#맨 위 루트노드가 pop되면, 가장 밑 레벨 가장 오른쪽의 노드를 루트로 옮김
#그럼 또 루트노드를 다시 자식과 비교(다운힙)

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
			print(hq.heappop(a)) 
			#루트 노드의 값을 pop함

	else:
		hq.heappush(a,n)
		#a에 최소힙 형태로 n을 넣는다
