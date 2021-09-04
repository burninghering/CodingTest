def solution(lottos, win_nums):
  zer=0
  match=0
  for i in range(6):
    if lottos[i]==0:
      zer+=1
    for j in range(6):
      if lottos[i]==win_nums[j]:
        match+=1

  answer=[]
  if zer==6:
    tw1=number(match)
    tw2=number(abs(match-zer))
    answer.append([tw1,tw2])
  elif 5>=zer>0:
    tw1=number(match)
    tw2=number(match+zer)
    answer.append([tw1,tw2])
  elif zer==0:
    one=number(match)
    answer.append([one,one])
      
  answer[0].sort()
  return answer[0]

def number(check):
  if check==0:
    return 6
  elif check==1:
    return 6
  elif check==2:
    return 5
  elif check==3:
    return 4
  elif check==4:
    return 3
  elif check==5:
    return 2
  elif check==6:
    return 1

lottos=[45, 4, 35, 20, 3, 9]
win_nums=[20, 9, 3, 45, 4, 35]
answer=solution(lottos, win_nums)
print(answer)

#https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3
