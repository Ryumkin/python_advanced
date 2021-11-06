number_of_students = int(input())
polyglots = set()
languages = set()

for index_of_student in range(0, number_of_students):
    number_of_languages = int(input())
    local_languages = {input() for i in range(0, number_of_languages)}
    if index_of_student == 0:
        languages = local_languages
    else:
        languages &= local_languages

print(len(languages))
print(*sorted(languages), sep="\n", end="")
