# python3
import sys

class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.offset = None
        self.value = None

    def has_edge(self, ch: str):
        if ch in self.children:
            return True

        return False

    def get_child(self, label: str) -> "Node":
        if label not in self.children:
            return None
        return self.children[label]

    def add_egde(self, label: str) -> "Node":
        new_node = Node()
        self.children[label] = new_node
        return new_node

    def get_children(self) -> dict:
        return self.children


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str, offset: int = None):
        current_node = self.root

        for c in word:
            if current_node.has_edge(c):
                current_node = current_node.get_child(c)
            else:
                current_node = current_node.add_egde(c)
        current_node.is_end_of_word = True
        if offset is not None:
            current_node.offset = offset

    def traverse(self, curr_node: Node = None, prev_label: str = None):
        if curr_node is None:
            curr_node = self.root
        for next_label, next_node in curr_node.get_children().items():
            self.traverse(next_node, next_label)

    def walkdown(self, curr_node: Node, prev_label: str = None):
        offset = set()
        if curr_node is None:
            curr_node = self.root

        stack = []
        stack.append(curr_node)

        
        while len(stack) >0:
            curr = stack.pop()
            if curr.is_end_of_word is True:
                offset.add(curr.offset)
    
            for _,next_node in curr.get_children().items():
                stack.append(next_node)
        return offset

    def match(self, pattern: str):

        curr_node = self.root
        for c in pattern:
            if curr_node.has_edge(c):
                curr_node = curr_node.get_child(c)
            else:
                return []
        offset = self.walkdown(curr_node)
        return offset
    
def solve (text, n, patterns):
    result = set()
    text = text + '$'
    text_len = len(text)
    trie = Trie()
    for i in range(text_len):
        suffix = text[i:]
        if suffix != '$':
            trie.insert(suffix, i)

    for p in patterns:
        offset = trie.match(p)
        result |= set(offset)
    
    return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
    patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
