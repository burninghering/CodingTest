def solution(name, yearning, photo):
    
    info = dict(zip(name,yearning))
    
    result = []
    
    for people in photo:
        score=0
        for person in people:
            score+=info.get(person,0)
        result.append(score)
        
    
    return result