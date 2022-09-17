# python3
import sys


class Node:
    def __init__(self, ch: str, node_id: int) -> None:
        self.value = ch
        self.node_id = node_id
        self.chidren = dict()
        self.isEndOfWord = False

    def addChild(self, ch: str, node_id: int):
        new_node = Node(ch, node_id)
        self.chidren[ch] = new_node
        return new_node

    def getChild(self, ch: str):
        return self.chidren[ch]

    def hasChild(self, ch: str):
        return ch in self.chidren


class Trie:
    def __init__(self) -> None:
        self.root = Node("", 0)
        self.nodes = dict()
        self.latest_id = 0

    def insert(self, word: str):
        word = word + '$'
        current = self.root

        for ch in word:
            if not current.hasChild(ch):
                new_node = current.addChild(ch, self.latest_id + 1)
                self.latest_id = self.latest_id + 1
                self.updateNodeDict(current_node=current, new_node=new_node)
            current = current.getChild(ch)
        current.isEndOfWord = True

    def updateNodeDict(self, current_node: Node, new_node: Node):
        if current_node.node_id not in self.nodes:
            self.nodes[current_node.node_id] = {}

        self.nodes[current_node.node_id][new_node.value] = new_node.node_id

    def prefixMatch(self, text: str):
        if len(text) < 1:
            return False

        s = iter(text)
        current = self.root

        while True:
            ch = next(s, None)

            if current.hasChild('$') is True:
                return True

            if ch is None:
                return False

            if not current.hasChild(ch):
                return False

            current = current.getChild(ch)

    def match(self, text: str):
        result = []
        for i in range(len(text)):
            if self.prefixMatch(text[i:]):
                result.append(i)

        return result


def solve(text, n, patterns):
    trie = Trie()

    for p in patterns:
        trie.insert(p)
    
    result = trie.match(text=text)

    #  write your code here

    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]

    ans = solve(text, n, patterns)

    sys.stdout.write(" ".join(map(str, ans)) + "\n")
