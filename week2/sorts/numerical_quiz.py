def sort(number):
    result = 0
    for i in range(len(number)//2):
        result += int(number[i]) - int(number[-(i+1)])
    return result


size = int(input())
words = [input() for _ in range(size)]

result = sorted(words, key=lambda item: (sort(item), int(item)))

print(*result, sep="\n", end="")
