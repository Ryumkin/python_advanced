first = map(int, input().split())
second = map(int, input().split())


def custom_map(x, y):
    return x ^ y


t = map(lambda x: custom_map(x[0], x[1]), zip(first, second))
print(*t)

"""
from author solution
print(
    *map(
        lambda x: x[0] ^ x[1],
        zip(
            map(int, input().split()),
            map(int, input().split())
        )
    )
)

"""

