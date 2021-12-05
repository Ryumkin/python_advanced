import argparse
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


def build(args):
    articles = load_document(args.dataset)
    inv_index = build_inverted_index(articles)
    inv_index.dump(args.index)


def query(args):
    inv_index = InvertedIndex.load(args.index)
    with open(args.query_file, 'r', encoding="utf-8") as f:
        for line in f:
            print(*sorted(inv_index.query(line.split())), sep=",", end="\n")


def parse(command_line):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    build_parser = subparsers.add_parser('build')
    build_parser.add_argument('--dataset', type=str)
    build_parser.add_argument('--index', type=str)
    build_parser.set_defaults(function=build)

    query_parser = subparsers.add_parser('query')
    query_parser.add_argument('--index', type=str)
    query_parser.add_argument('--query_file', type=str)
    query_parser.set_defaults(function=query)
    return parser.parse_args(command_line)


def main(command_line=None):
    parsed_command = parse(command_line)
    parsed_command.function(parsed_command)


if __name__ == '__main__':
    main()
