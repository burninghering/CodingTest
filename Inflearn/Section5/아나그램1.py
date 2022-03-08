a=input()
b=input()

str1=dict()
str2=dict()

for x in a:
    str1[x]=str1.get(x,0)+1 #x가 있으면 x의 value값 반환, x가 없으면 0 반환

for x in b:
    str2[x]=str2.get(x,0)+1

for i in str1.keys(): #키값들만 가지고 오고 싶다
    if i in str2.keys(): #str1의 키가 str2의 키들 중에 없다면 아나그램이 아니다.
        if str1[i]!=str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
