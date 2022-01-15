import time

n=int(input())
b=list(input().split())

start=time.time()
def reverse(a):
  a=a[::-1]
  while a[0]=='0':
    try:
      a=a[1:]
    except:
      break
  return a

def is_prime(a):
  if a==1:
    return False
  for i in range(2,a//2+1):
    if a%i==0:
      return False
  else:
    return True

answer=[]
for i in range(n):
  rev=reverse(b[i])
  ans=is_prime(int(rev))
  if ans==False:
      continue
  else:
    print(rev,end=' ')
end=time.time()
print()
print(f"{end-start:0.5f} sec")

#0.02611
