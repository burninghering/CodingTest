a=list(range(21))
for _ in range(10):
    s, e=map(int, input().split())

    for i in range((e-s+1)//2):
        a[s+i], a[e-i]=a[e-i], a[s+i] #파이썬 인덱스 서로 교환 방식
a.pop(0)
for x in a:
    print(x, end=' ')
