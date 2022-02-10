n=int(input())
meeting=[]

for i in range(n):
    a, b=map(int, input().split())
    meeting.append((a, b)) #튜플 형태로 집어넣기 
meeting.sort(key=lambda x : (x[1], x[0])) #정렬의 기준을 meeting의 한 요소를 람다 함수 x로 받는다. 그리고 x[1]이 우선순위가 되고 x[0]이 차순위가 된다.
#그냥 sort로 정렬하면, 앞의 값을 기준으로 정렬한다.
et=0
cnt=0
for x, y in meeting: #끝나는 시간을 기준으로 정렬했으니 한번만 for문 돌면 된다.
    if x>=et:
        et=y
        cnt+=1

print(cnt)