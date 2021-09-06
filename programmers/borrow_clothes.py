def solution(n, lost, reserve):
    answer = 0
    reserve2=[r for r in reserve if r not in lost]
    lost2=[l for l in lost if l not in reserve]
    
    for r in reserve2:
        if r-1 in lost2:
            lost2.remove(r-1)
        elif r+1 in lost2:
            lost2.remove(r+1)
    answer=n-len(lost2)
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42862
