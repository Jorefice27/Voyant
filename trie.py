# node class for trie data structure
class Node:
    def __init__(self, val):
        # dict of children where key = child.val, value = child
        self.children = {}
        # value of the node
        self.val = val
        # boolean to represent whether this could be the end of a word
        self.isLeaf = False

    def addNode(self, val):
        self.children[val] = Node(val)

    def hasNode(self, val):
        return val in self.children


class Trie:
    def __init__(self):
        self.root = Node(None)

    # navigates down the trie to add the string, creating new nodes when required
    def add(self, string):
        cur = self.root
        for c in string:
            if c not in cur.children:
                cur.addNode(c)
            cur = cur.children[c]
        cur.isLeaf = True

    # navigates down the trie to see if the provided value is stored
    def contains(self, val):
        cur = self.root
        for c in val:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        # return isLeaf to avoid false positives (ie saying trie.contains('hell') because 'hello' was added)
        return cur.isLeaf
