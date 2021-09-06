total_par=0
dic={}
participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

for par in participant:
  dic[hash(par)]=par
  total_par+=int(hash(par))
for com in completion:
  total_par-=hash(com)


answer=dic[total_par]
print(answer)

#https://programmers.co.kr/learn/courses/30/lessons/42576
