
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        item = self.stack[-1]
        del self.stack[-1]
        return item

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)


# minstack = MinStack()
# minstack.push(-2)
# minstack.push(-1)
# minstack.push(4)
# minstack.push(10)
# minstack.push(0)

# print(f"Min - {minstack.getMin()}")
# print(f"Pop - {minstack.pop()}")
# print(f"Top - {minstack.top()}")
# print(f"Min - {minstack.getMin()}")