class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, digit):
        if digit > 0:
            super().append(digit)
        else:
            raise NonPositiveError
