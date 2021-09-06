def solution(phone_book):
    for i in phone_book:
        for j in phone_book:
            if i==j:
                continue
            leng=len(i)
            leng2=j[:leng]
            
            if i==leng2:
                answer=False
                return answer
            
    return True
