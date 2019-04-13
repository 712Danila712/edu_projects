class Stack:
    def __init__(self):
        self.size = 0
        self.content = []
        self.top = 0
        self.count = 0

    def push(self, item):
        if self.top + 1 == self.size + 1:
            print("Lack of space")
        else:
            self.content.append(item)
            self.top += 1
            self.count += 1

    def pop(self, smh):
        if self.top - 1 == 0:
            print("Out of space")
        else:
            if smh in self.content:
                self.content.remove(smh)
                self.top -= 1
                self.count -= 1

    def write(self):
        print("size:{} content:{} top:{}".format(self.size, self.content, self.top))

    def clear(self):
        del self.content[0:]


if __name__ == '__main__':
    a = Stack()

    a.size = 6

    for i in range(9):
        a.push(7)

    a.write()

    for i in range(9):
        a.pop(7)
    a.clear()

    a.write()
