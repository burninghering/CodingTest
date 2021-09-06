from collections import Counter
participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']


a=Counter(participant)-Counter(completion)

print(list(a.keys())[0])

