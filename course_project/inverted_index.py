def load_document(filepath, encoding="utf8"):
    with open(filepath, "r", encoding=encoding) as reader:
        return {key: value for key, value in
                (i.split(maxsplit=1) for i in reader.readlines())}
