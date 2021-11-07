lines = int(input())
synonyms = dict()

for _ in range(lines):
    k, v = input().split()
    synonyms[k] = v
    synonyms[v] = k

print(synonyms[input()])
