def solution(n, lost, reserve):
  
    
  borrowed=[]
  d=[False]*(n)

  for i in reserve:
    if i not in lost:
      borrowed.append(i)
  
  if len(borrowed)==0:
    print(0)
    exit()
  
  for i in borrowed:
    if i==1:
      d[i]=True
      d[1]=True
    else:
      d[i]=True
      if d[i-1]:
        d[i+1]=True
      else:
        d[i-1]=True

  cnt=0
  answer=0
  nocnt=0
  
  for i in range(len(d)):
    if d[i]:
      cnt+=1
    else:
      nocnt+=1

  alr=n-nocnt
  answer=alr+cnt
  return answer
  
                
n=3
reserve=[1]
lost=	[3]  
print(solution(n,lost,reserve))


#https://programmers.co.kr/learn/courses/30/lessons/42862
