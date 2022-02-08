n,m=map(int,input().split())
a=list(map(int,input().split())
       
lt=0
rt=n-1
while lt<=rt:
  mid=(lt+rt)//2
  if a[mid]==m:
    print(mid+1) #몇번째인지 출력
  elif a[mid]>m:
    rt=mid-1
  else:
    lt=mid+1
