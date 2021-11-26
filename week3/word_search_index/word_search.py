import json

len_words = int(input())
mydict = dict()
for i in range(len_words):
    word = input()
    sub_dict = mydict.get(word[0], dict())
    lst = sub_dict.get(word[0:2], [])
    lst.append(word)
    sub_dict[word[0:2]] = sorted(lst)
    mydict[word[0]] = sub_dict

with open(input(), "w") as writer:
    writer.write(json.dumps(mydict))

"""
import json
from collections import defaultdict


n_words = int(input())
words = [input() for _ in range(n_words)]
output_filename = input()

search_index = defaultdict(dict)
for word in words:
    search_index[word[0]].setdefault(word[:2], []).append(word)

search_index = {
    key: {a: sorted(b) for a, b in value.items()}
    for key, value in search_index.items()
}

with open(output_filename, 'w') as f:
    json.dump(search_index, f)

"""
