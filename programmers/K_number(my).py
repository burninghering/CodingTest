answer=[]
def solution(array, commands):
    for c in range(len(commands)):
        global answer
        i=commands[c][0]
        j=commands[c][1]
        k=commands[c][2]
        
        if i==j:
            a=array[i-1]
            answer.append(a)
        else:
            b=array[i-1:j+1]
            b.sort()
            ans=b[k-1]
        
            answer.append(ans)
    
    
    return answer
