import time

n=int(input())

start=time.time()

for i in range(1,n+1):
  a=input()
  a=a.upper()
  b=a[::-1]
  if a==b:
    print(f"#{i} YES")
  else:
    print(f"#{i} NO")

end=time.time()
print(f"{end-start:0.5f} sec")

#0.17702 sec
