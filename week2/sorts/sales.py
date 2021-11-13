mycollection = dict()
while True:
    try:
        string = input()
        if string == "":
            break
        words = string.split()
        items = mycollection.get(words[0], dict())
        number = items.get(words[1], 0)
        items[words[1]] = number + int(words[2])
        mycollection[words[0]] = items
    except EOFError:
        break

for person in sorted(mycollection):
    print(person, ":", sep="")
    items = mycollection[person]
    for i in sorted(items):
        print(i, items[i])
