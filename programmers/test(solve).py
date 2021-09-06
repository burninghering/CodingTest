from itertools import cycle
def solution(answers):
    cycles=[
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5])
    ]
    
    count=[0,0,0]
    
    for answer in answers:
        for i in range(3):
            if answer==next(cycles[i]):
                count[i]+=1
                
        
    return [per+1 for per,score  in enumerate(count) if score==max(count)]
