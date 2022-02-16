n=input()

stack=[]
sum=0

for i in range(len(n)):
    if n[i]=='(':
        stack.append(n[i])
    else:
        stack.pop()
        if n[i-1]=='(':
            sum+=len(stack)
        else:
            sum+=1

print(sum)
            
        
