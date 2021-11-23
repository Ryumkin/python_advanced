first = input().split()
second = map(float, input().split())

tuples = filter(lambda x: x[1] > 0.5, zip(first, second))
result = map(lambda x: x[0], sorted(tuples, key=lambda x: x[1], reverse=True))
print(*result, sep="\n", end="")
