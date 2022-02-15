n=int(input())

a=list(map(int,input().split()))

seq=[0]*n

for i in range(n): #a 역수열과 seq 배열을 같이 보려면 2중 for문을 사용하면 되는구나.
    for j in range(n):
        if a[i]==0 and seq[j]==0: #자기 앞의 빈 공간을 확보했으며, 
            seq[j]=i+1 #i index를 0부터 반복문을 돌리고 있어서
            break;
        elif seq[j]==0: #빈 자리가 발견된다면
            a[i]-=1 #내 앞의 빈 자리를 하나씩 추가해준다
            

for x in seq:
    print(x,end=' ')
