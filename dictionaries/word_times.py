answers = dict()
while True:
    string = input()
    if string == "":
        break
    words = string.split()
    for word in words:
        if word in answers:
            answers[word] += 1
        else:
            answers[word] = 0
        print(answers[word], end=" ")
