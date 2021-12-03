import json
import pickle


def load_document(filepath: str, encoding: str = "utf8") -> dict:
    with open(filepath, "r", encoding=encoding) as reader:
        return {int(key): value.strip() for key, value in
                (i.split(maxsplit=1) for i in reader.readlines())}


def build_inverted_index(articles):
    inverted_indexes = {}
    for article_id, string in articles.items():
        for word in set(string.split()):
            article_ids = inverted_indexes.setdefault(word, set())
            article_ids.add(int(article_id))
    return InvertedIndex(inverted_indexes)


class InvertedIndex:
    def __init__(self, inverted_indexes: dict):
        self.inverted_indexes = inverted_indexes

    def query(self, words):
        sets = [self.inverted_indexes.get(word, set()) for word in words]
        return set(set.intersection(*sets))

    def dump(self, filepath):
        pickle.dump(self, open(filepath, 'wb'))

    @classmethod
    def load(cls, filepath):
        obj = pickle.load(open(filepath, 'rb'))
        return obj
