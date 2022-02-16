n=input()

n=list(map(str,n))

stack=[]
sum=0

for i in range(len(n)):
    if i=='(':
        stack.append(n[i])
    else:
        stack.pop()
        sum+=len(stack)
        
        
#막대기의 끝을 어떻게 처리해야할 지 몰라서 멈췄다..
#'('만 계속 스택에 넣다가, ')'가 나타나면 레이저로 자르던지, 막대기의 끝인지 판단한다. 어렵다~
