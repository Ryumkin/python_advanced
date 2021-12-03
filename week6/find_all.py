import re

lines = []

while True:
    line = input()
    if not line:
        break
    else:
        lines.append(line)

pattern = re.compile(r'<i>(.*?)</i>')
res = re.findall(pattern, ''.join(lines))
print(*res, sep='\n')
