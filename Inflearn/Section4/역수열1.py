n=int(input())

a=list(map(int,input().split()))

check=[0]*n

for i in range(n): 
    for j in range(n):
        if a[i]==0 and check[j]==0:
            check[j]=i+1
            break #집어넣었으면 이제 다음 i를 체크하자 
        elif check[j]==0:
            a[i]-=1

for x in check:
    print(x,end=' ')
