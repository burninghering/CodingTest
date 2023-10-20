# def solution(players, callings):
#     answer=players
    
#     for i in range(len(callings)):
#         found=answer.index(callings[i]) 
#         answer[found-1],answer[found]=answer[found],answer[found-1]
        
#     return answer

def solution(players, callings):
    
    result={player: i for i,player in enumerate(players)} # index 함수 대신 딕셔너리를 사용한다

    for who in callings:
        idx=result[who] #호명된 사람의 현재 등수
        
        #딕셔너리의 value값을 고쳐준다
        result[who]-=1 
        result[players[idx-1]]+=1
        
        players[idx],players[idx-1]=players[idx-1],players[idx]
               
    return players