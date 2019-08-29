import sys
base = list(map(int, sys.stdin.readline().split()))
idx = -1
gan = base[1]
max_n = base[0]
humans= [x for x in range(1, max_n+1)]
result = []
while len(humans) != 1:
    if idx + gan < len(humans):
        idx += gan
    else:
        idx = (idx+gan) % len(humans)
    result.append(humans.pop(idx))
    idx -= 1
result.append(humans.pop())
result = list(map(str, result))
result = ", ".join(result)
print('<'+result+'>')