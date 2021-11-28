class CountVectorizer:

    def __init__(self, ngram_size):
        self.ngram_size = ngram_size
        self.vocab = {}

    def __get_tokens(self, input_str: str):
        tokens = []
        for i in range(len(input_str) - self.ngram_size + 1):
            token = input_str[i:i + self.ngram_size]
            tokens.append(token)
        return tokens

    def fit(self, corpus):
        self.vocab.clear()
        tokens = set()
        for x in corpus:
            tokens.update(self.__get_tokens(x))
        self.vocab = {value: index for index, value in
                      enumerate(sorted(set(tokens)))}

    def transform(self, corpus):
        input_corpus = {}
        transformed_corpus = []
        for x in corpus:
            input_corpus[x] = self.__get_tokens(x)
        for item in corpus:
            list_of_tokens = [
                input_corpus[item].count(token)
                for token
                in sorted(self.vocab.keys())
            ]
            transformed_corpus.append(list_of_tokens)
        return transformed_corpus

    def fit_transform(self, corpus):
        self.fit(corpus)
        return self.transform(corpus)
