n=input()

stack=[]
ans=[]

for i in range(len(n)):
    if n[i] not in ['+','-','*','/']:
        ans.append(n[i])
    else:
        if n[i]=='*' or n[i]=='/' or n[i]=='(' or n[i]==')':
            ans.append(n[i])
        else:
            
        
        
