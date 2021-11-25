import json
from json import JSONDecodeError

filename = input()

statuses_ok = 0
statuses_bad = 0
incorrect_lines = 0
empty_strings = 0
non_integers = 0
with open(filename, "r") as reader:
    for line in reader.readlines():
        try:
            json_line = json.loads(line)
            if "status" in json_line:
                status = json_line["status"]

                if status is None:
                    empty_strings += 1
                    continue

                if isinstance(status, str):
                    if not status:
                        empty_strings += 1
                        continue
                    try:
                        status = int(status)
                    except ValueError:
                        non_integers += 1
                        continue

                if status == 200:
                    statuses_ok += 1
                else:
                    statuses_bad += 1
            else:
                empty_strings += 1
        except JSONDecodeError:
            incorrect_lines += 1

print(statuses_ok)
print(statuses_bad)
print(non_integers)
print(empty_strings)
print(incorrect_lines)
