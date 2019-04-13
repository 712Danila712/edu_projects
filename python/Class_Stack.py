class Stack:
    def __init__(self):
        self.size = 0
        self.content = []
        self.top = 0
        self.count = 0

    #def push(self, item):
     #   if self.top + 1 == self.size:
        
a = Stack()
print("{} {} {} {}".format(a.size, a.content, a.top, a.count))
