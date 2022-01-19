import re
import time

a=input()

start=time.time()

numbers=re.sub(r'[^0-9]','',a)

while True:
  if numbers[0]=='0':
    numbers=numbers[1:]
  else:
    break

print(numbers)

numbers=int(numbers)

ans=0
for i in range(1,numbers+1):
  if numbers%i==0:
    ans+=1

print(ans)

end=time.time()
print(f"{end-start:0.5f} sec")

#0.04511 sec
