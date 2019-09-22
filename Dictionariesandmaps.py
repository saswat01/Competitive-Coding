import sys

n = int(sys.stdin.readline().strip())

log = dict()
#print(n)
for a in range(n):
    entry = sys.stdin.readline().strip().split(' ')
    log[entry[0]] = entry[1]
#print(log)

query = sys.stdin.readline().strip()

while query:
    #print(query)
    a = log.get(query)
    #print(a)
    if a:
        print(query + "=" + a)
    else:
        print('Not found')
    query = sys.stdin.readline().strip()    