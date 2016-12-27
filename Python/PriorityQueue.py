class Node(object):

    # constructor that creates a node with a certain value and priority
    def __init__(self, value, priority):
        self.val = value
        self.priority = priority
        self.next = None


class PriorityQueue(object):

    def __init__(self):
        self.head = None
        self.size = 0

    # adds items to the queue
    # equal priority items are added to the end
    # higher priority is closer to the front
    def enqeue(self, value, priority):
        self.size += 1
        new = Node(value, priority)
        if not self.head or priority > self.head.priority:
            new.next = self.head
            self.head = new
            return

        temp = self.head
        previous = None
        while temp and priority <= temp.priority:
            previous = temp
            temp = temp.next
        new.next = temp
        previous.next = new

    # removes the first qeued item and returns it
    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        temp = self.head
        self.head = self.head.next

        return temp.val

# q = PriorityQueue()
# q.enqeue(1, 0)
# q.enqeue(2, 0)
# q.enqeue(3, 0)
# q.enqeue(5, 1)
# q.enqeue(9, 0)
# q.enqeue(5, -1)
#
# for i in range(q.size):
#     print q.dequeue()
