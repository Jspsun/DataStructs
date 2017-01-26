from collections import deque


def BFS(root):
    s = deque([])
    s.append(root)
    while len(s) > 0:
        x = s.popleft()
        if(x.left != None):
            s.append(x.left)
        if(x.right != None):
            s.append(x.right)
        print(" " + str(x.data))


class Node (object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

'''
   1
 2   3
4 5 6 7
'''
print "Breadth-First-Search : "
BFS(root)
