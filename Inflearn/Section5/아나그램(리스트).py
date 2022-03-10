a=input()
b=input()

#0~25는 대문자, 26~51까지는 소문자
str1=[0]*52
str2=[0]*52

for x in a:
    if x.isupper(): #x가 대문자인가?
        str1[ord(x)-65]+=1
    else:
        str1[ord(x)-71]+=1 #소문자 97에서 71을 빼야 26부터의 공간을 사용 가능

for x in b:
    if x.isupper():
        str2[ord(x)-65]+=1
    else:
        str2[ord(x)-71]+=1


for i in range(52):
    if str1[i]!=str2[i]:
        print("NO")
        break

else:
    print("YES")

        

