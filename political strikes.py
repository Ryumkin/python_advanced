days_in_year, parties = [int(i) for i in input().split()]
strikes = set()

for i in range(0, parties):
    a, b = [int(i) for i in input().split()]
    day = 0
    index = 0
    strikes_for_party = set()
    while True:
        day = a + b*index
        if day > days_in_year:
            break
        index += 1
        if (day % 7) % 6 != 0 and (day % 7) % 7 != 0:
            strikes_for_party.add(day)
    strikes |= strikes_for_party

print(len(strikes))
