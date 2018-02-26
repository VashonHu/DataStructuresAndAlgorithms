class stack(object):
    def __init__(self):
        self.__stack = []

    def push(self, val):
        self.__stack.append(val)

    def __empty(self):
        return len(self.__stack) == 0

    def pop(self):
        if self.__empty():
            print("this stack is underflow")
            return -1

        element = self.__stack[-1]
        del self.__stack[-1]
        return element
