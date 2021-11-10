input()
parties = dict()
while True:
    try:
        party = input()
        if party == "VOTES:" or "":
            break
        parties.setdefault(party, 0)
    except EOFError:
        break

while True:
    try:
        party = input()
        if party == "":
            break
        parties[party] += 1
    except EOFError:
        break

answers = []

max_votes = sum(parties.values())

for party, votes in parties.items():
    if (votes / max_votes)*100 > 7:
        answers.append(party)

print(*answers, sep="\n", end="")
