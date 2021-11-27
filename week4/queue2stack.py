from collections import deque


class Queue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, elem):
        self.s1.append(elem)

    def pop(self):
        if not self.s1 and not self.s2:
            raise IndexError('pop from an empty queue')
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()


"""
class Queue:
    def __init__(self):
        self.left_stack = []
        self.right_stack = []

    def push(self, x):
        self.left_stack.append(x)

    def pop(self):
        if not self.right_stack and self.left_stack:
            self.right_stack.extend(reversed(self.left_stack))
            self.left_stack = []

        if self.right_stack:
            return self.right_stack.pop()
        else:
            raise IndexError('pop from an empty queue')

"""
