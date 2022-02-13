n=int(input())
a=list(map(int, input().split()))

lt=0
rt=n-1
last=0
res=""
tmp=[]

while lt<=rt:   
    if a[lt]>last: 
        tmp.append((a[lt], 'L'))

    if a[rt]>last:
        tmp.append((a[rt], 'R'))

    tmp.sort() #양 쪽에서 작은 것이 둘 다 들어갈 수 있으니까 정렬!

    if len(tmp)==0: #아무것도 안들어갔다면 끝낸다
        break;

    else: #무언가 들어갔다면
        res=res+tmp[0][1] #제일 앞의 문자를 가져온다
        last=tmp[0][0] #제일 앞의 숫자를 가져온다
        if tmp[0][1]=='L': #만약 왼쪽이었다면
            lt=lt+1 #왼쪽 1 더하기
        else:
            rt=rt-1
    tmp.clear() #문자열 초기화

print(len(res))
print(res)