class Buffer:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.buffer = []

    def add(self, *a):
        self.buffer.extend(a)
        self.__flush()

    def get_current_part(self):
        return self.buffer

    def __flush(self):
        while len(self.buffer) >= self.maxsize:
            print(sum(self.buffer[:self.maxsize]))
            self.buffer = self.buffer[self.maxsize:]
