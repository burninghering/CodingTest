a=input()

res=[]



for x in a:
    if x.isdecimal():
      res.append(x)
    else:
        if len(res)>=2:
            if x=='+':
                a=res.pop()
                b=res.pop()
                c=int(b)+int(a)
                res.append(str(c))

            elif x=='-':
                a=res.pop()
                b=res.pop()
                c=int(b)-int(a)
                res.append(str(c))
  
            elif x=='*':
                a=res.pop()
                b=res.pop()
                c=int(b)*int(a)
                res.append(str(c))

            elif x=='/':
                a=res.pop()
                b=res.pop()
                c=int(b)/int(a)
                res.append(str(c))
              

print(res[0])
            
