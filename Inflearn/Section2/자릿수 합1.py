import time

n=int(input())
a=list(input().split())

start=time.time()
def digit_sum(x):
  sum=[]
  for i in x:
    total=0
    for j in range(len(i)):
      total+=int(i[j])
    sum.append(total)
  
  z=max(sum)
  print(a[sum.index(z)])
    
digit_sum(a)
end=time.time()

print(f"{end-start:.5f} sec")
