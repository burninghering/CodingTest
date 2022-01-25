board=[list(map(int,input().split())) for _ in range(7)]

len=10 #가변적
cnt=0

for i in range(3):
  for j in range(7):
    tmp=board[j][i:i+len]
    if tmp==tmp[::-1]:
      cnt+=1
    for k in range(len//2):
      if board[i+k][j]!=board[len-k+i-1][j]:
        break
    else:
      cnt+=1

print(cnt)
