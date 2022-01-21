n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

c=a+b
c=sorted(c)
print(c,end='')
