from collections import deque

def solution(numbers, target):
    
    answer = 0
    q=deque()
    q.append((0,0))
    
    while q:
        cur_sum,num=q.popleft()
        
        if num==len(numbers):
            if cur_sum==target:
                answer+=1
        else:
            number=numbers[num]
            q.append((cur_sum+number,num+1))
            q.append((cur_sum-number,num+1))
    return answer
