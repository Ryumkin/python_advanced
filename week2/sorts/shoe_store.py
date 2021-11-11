size = int(input())
sizes = sorted({int(i) for i in input().split() if int(i) >= size})

result = []
for i in sizes:
    if len(result) == 0:
        result.append(i)
    else:
        if i >= result[-1] + 3:
            result.append(i)

print(len(result))
