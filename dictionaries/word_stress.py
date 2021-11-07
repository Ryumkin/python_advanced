numbers = int(input())
dictionary = dict()
for _ in range(numbers):
    word = input()
    key = word.lower()
    if key in dictionary:
        dictionary[key].append(word)
    else:
        dictionary[key] = [word]

words = input().split()
mistakes = 0
for word in words:
    if word.lower() in dictionary:
        if word not in dictionary[word.lower()]:
            mistakes += 1
        continue
    count_supper = sum([1 for symbol in word if symbol.isupper()])
    if count_supper == 1:
        continue
    mistakes += 1
print(mistakes)
