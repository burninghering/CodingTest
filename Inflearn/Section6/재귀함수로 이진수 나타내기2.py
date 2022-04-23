def DFS(x):
    if x==0:
        return #함수를 종료시켜라
    else:
        DFS(x//2)
        print(x%2, end='')

if __name__=="__main__":
    n=int(input())
    DFS(n)

#함수는 스택에서 자기 할 일을 끝내야만 할당 해제됨
