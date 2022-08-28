# Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.


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
        current = self.root

        for ch in word:
            if not current.hasChild(ch):
                new_node = current.addChild(ch, self.latest_id + 1)
                self.latest_id = self.latest_id + 1
                self.updateNodeDict(current_node=current, new_node=new_node)
            current = current.getChild(ch)

    def updateNodeDict(self, current_node: Node, new_node: Node):
        if current_node.node_id not in self.nodes:
            self.nodes[current_node.node_id] = {}

        self.nodes[current_node.node_id][new_node.value] = new_node.node_id


def build_trie(patterns):
    trie = Trie()
    for p in patterns:
        trie.insert(p)

    return trie.nodes


if __name__ == "__main__":
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))


# 0->1:A
# 1->2:T
# 2->3:A
# 3->4:G
# 4->5:A
# 2->6:C
# 0->7:G
# 7->8:A
# 8->9:T
