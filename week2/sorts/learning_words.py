size = int(input())
words = [input() for _ in range(size)]

result = sorted(words, key=lambda item: (len(item), item[::-1]))

print(*result, sep="\n", end="")
