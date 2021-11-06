n = int(input())
possible_nums = set(range(1, n + 1))
answers = []
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess_set = {int(x) for x in guess.split()}
    if len(guess_set) <= len(possible_nums) // 2:
        possible_nums -= guess_set
        answers.append("NO")
    else:
        possible_nums &= guess_set
        answers.append("YES")
print(*answers, sep="\n", end="\n")
print(*sorted(possible_nums))
