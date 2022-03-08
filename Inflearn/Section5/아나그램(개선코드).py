a=input()
b=input()

std=dict()

for x in a:
    std[x]=std.get(x,0)+1

for x in b:
    std[x]=std.get(x,0)-1


for x in a:
    if std.get(x)>0:
        print("N0")
        break
else:
    print("YES")
