class Node:
    def __init__(self, val):
        self.children = {}
        self.val = val
        self.isLeaf = False

    def addNode(self, val):
        self.children[val] = Node(val)

    def hasNode(self, val):
        return val in self.children


class Trie:
    def __init__(self):
        self.root = Node(None)

    def add(self, string):
        cur = self.root
        for c in string:
            if c not in cur.children:
                # print(c + ' is not in children, creating new node')
                cur.addNode(c)
            cur = cur.children[c]
        cur.isLeaf = True

    def contains(self, val):
        cur = self.root
        for c in val:
            if c not in cur.children:
                # print('Could not find ' + c)
                return False
            cur = cur.children[c]
            # print('Found ' + c)
        return cur.isLeaf
