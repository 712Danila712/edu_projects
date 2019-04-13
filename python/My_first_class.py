class node:

    def __init__(self):
        self.data = 0
        self.next = None

    def print_list(self):
        temp = self

        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()


class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def print_(self):
        print("({}, {})".format(self.x, self.y))

    def set_(self, x, y):
        self.x = x
        self.y = y

    def sum_(self, p2):
        return Point(self.x + p2.x, self.y + p2.y)


if __name__ == '__main__':
    head = node()
    head.data = 4

    head.print_list()

    l = node()
    l.data = 2
    head.next = l

    head.print_list()

    l = node()
    l.data = 9

    l.next = head.next
    head.next = l
    head.print_list()

    print()
    print()
    
    p1 = Point(12, 4)
    p2 = Point(5, -8)

    p = p1.sum_(p2)
    p.print_()
    p1.print_()
    p2.print_()
