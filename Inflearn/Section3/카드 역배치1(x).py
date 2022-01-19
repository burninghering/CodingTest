a=list(range(21))

for i in range(10):
  n,m=map(int,input().split())
  if ((m-n)//2)%2==1: #홀수 
    for x in range((m-n)//2+1):
          b=a[n+x]
    a[n+x]=a[m-x]
    a[m-x]=b
  else: #짝수 
    for x in range((m-n)//2):
      b=a[n+x]
      a[n+x]=a[m-x]
      a[m-x]=b
    
    else: #5,6과 같은 경우
      b=a[n+1]
      a[n+1]=a[m-1]
      a[m-1]=b
    
print(a[1:])

#풀지 못했다.
