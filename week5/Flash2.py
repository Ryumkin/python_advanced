class FlashError(Exception):
    pass


class FlashMaxFileSizeError(FlashError):
    pass


class FlashMemoryLimitError(FlashError):
    pass


class Flash:
    def __init__(self, capacity, max_file_size=None):
        self.capacity = capacity
        self.max_file_size = max_file_size

    def write(self, filesize):
        if self.max_file_size is not None and filesize > self.max_file_size:
            raise FlashMaxFileSizeError
        if self.capacity < filesize:
            raise FlashMemoryLimitError
        self.capacity -= filesize
