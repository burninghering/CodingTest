def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer: answer[i[1]]+=1
        else: answer[i[1]]=1
    cnt=1
    for i in answer.values():
        cnt*=(i+1) #입을 때도 있고, 안 입을 때도 있고 
    return cnt-1 #아예 전부 안입을 때도  있으니까 
