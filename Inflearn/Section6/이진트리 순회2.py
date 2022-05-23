def DFS_1(v): #전위 순회 
    if v>7:
        return
    else:
        print(v,end=" ") 
        DFS(v*2)
        DFS(v*2+1)
        
def DFS_2(v): #중위 순회 
    if v>7:
        return
    else:
        DFS(v*2)
        print(v,end=" ") 
        DFS(v*2+1)

def DFS_3(v): #후위 순회 (대표적인 병합정렬의 예)
    if v>7:
        return
    else:
        DFS(v*2) #왼쪽 자식 다 처리하고
        DFS(v*2+1) #오른쪽 자식 다 처리한 후 
        print(v,end=" ") 

if __name__=="__main__":
    DFS(1)


#전위 순회 : 부 왼 오
#중위 순회 : 왼 부 오
#후위 순회 : 왼 오 부 
