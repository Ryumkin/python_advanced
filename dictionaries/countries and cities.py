countries = int(input())
shit = {k: v for k, *v in (input().split() for _ in range(countries))}
number_of_cities = int(input())
finding_cities = [input() for _ in range(number_of_cities)]
answers = []
for city in finding_cities:
    for country, cities in shit.items():
        if city in cities:
            answers.append(country)
            break

print(*answers, sep="\n", end="")
