answers = dict()
count = 0
while True:
    try:
        string = input()
        if string == "":
            break
        words = string.split()
        for word in words:
            if word in answers:
                answers[word] += 1
            else:
                answers[word] = 1
            count = count > answers[word] and count or answers[word]
    except EOFError:
        break

keys = [k for k, v in answers.items() if v == count]

print(sorted(keys)[0])
