
def check(a):
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10

        for j in range(9):
            ch1[a[i][j]]=1 #행 가로 -> a[i][j]에 있는 값을 check의 인덱스로 하여 1을 넣는다 
            ch2[a[j][i]]=1 #열 세로 

        if sum(ch1)!=9 or sum(ch2)!=9: #만약 중복해서 나오더라도 1을 넣어주면, 한 칸이 비어서 9가 안되기 때문에
            return False

    for i in range(3): #9개의 그룹을 보겠다
        for j in range(3):
            ch3=[0]*10

            for k in range(3): #1개의 그룹 안에 9개를 보겠다  
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1 #Z모양으로 검사중

            if sum(ch3)!=9:
                return False

    return True

a=[list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")