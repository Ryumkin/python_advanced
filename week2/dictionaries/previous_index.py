answers = dict()
index = 0
while True:
    try:
        string = input()
        if string == "":
            break
        words = string.split()
        for word in words:
            result = answers.get(word, -1)
            print(result, end=" ")
            answers[word] = index
            index += 1
    except EOFError:
        break
