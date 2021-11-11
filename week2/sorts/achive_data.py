size, users_count = map(int, input().split())

users_data = []
for i in range(users_count):
    user_size = int(input())
    users_data.append(user_size)
users_data.sort()

possible_archive_users = 0
total_archive_data = 0
for i in users_data:
    if total_archive_data + i <= size:
        possible_archive_users += 1
        total_archive_data += i
    else:
        break

print(possible_archive_users)
