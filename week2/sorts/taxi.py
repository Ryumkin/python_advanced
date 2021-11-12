kilometers = sorted(map(int, input().split()))
tariffs = sorted(map(int, input().split()), reverse=True)

result = 0

for i in range(len(kilometers)):
    result += kilometers[i]*tariffs[i]

print(result)
