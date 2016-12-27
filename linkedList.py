class LinkedList(object):
    head = None
    size = 0

    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, x):
        self.size += 1
        new = Node()
        new.val = x

        if not self.head:
            self.head = new
            return

        temp = self.head
        previous = None
        while temp:
            previous = temp
            temp = temp.next
        new.next = temp
        previous.next = new
        return

    def remove(self, index):
        if index < 0 or index > self.size - 1:
            return

        self.size -= 1
        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        previous = None
        for i in range(0, index):
            previous = temp
            temp = temp.next
        previous.next = temp.next
        return

    def get(self, index):
        temp = self.head
        if index < 0 or index > self.size - 1:
            return None
        for i in range(0, index):
            temp = temp.next
        return temp.val


class Node (object):
    val = None
    next = None
#
# list = LinkedList()
# list.add(0)
# list.add(1)
# list.add(2)
# list.add(3)
# list.add(4)
# list.add(5)
#
#
# list.remove()
#
# for i in range(list.size):
#     print list.get(i)
