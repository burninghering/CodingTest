def solution(name):
    answer = 0
    i=0
    name=list(name)
    
    while True:
        answer+=min(ord(name[i])-ord('A'),ord('Z')-ord(name[i])+1)
        name[i]='A'
        if len(name)==name.count('A'):
            return answer
        
        left=right=1
        for l in range(1,len(name)):
            if name[i-1]=='A':
                left+=1
            else:
                break
        for r in range(1,len(name)):
            if name[i+1]=='A':
                right+=1
            else:
                break
                    
        if right>left:
            answer+=left
            i-=left
        else:
            answer+=right
            i+=right
    
                    
    return answer
