import collections
answers = collections.OrderedDict()
while True:
    try:
        string = input()
        if string == "":
            break
        words = string.split()
        for word in words:
            result = answers.get(word, 0)
            answers[word] = result + 1
    except EOFError:
        break

result = dict(sorted(answers.items(), key=lambda item: (-item[1], item[0])))

print(*result, sep="\n", end="")
