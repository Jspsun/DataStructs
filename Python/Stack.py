class Node(object):

    def __init__(self, value):
        self.val = value
        self.next = None


# simple stack
class Stack(object):

    def __init__(self):
        self.top = None

    # adds node to top of stack
    def push(self, value):
        new = Node(value)
        new.next = self.top
        self.top = new

    # removes node from top and returns it
    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            return temp.val
        return None

# s = Stack()
#
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# s.pop()
# s.push(99)
#
# temp = s.pop()
# while temp:
#     print temp
#     temp = s.pop()
