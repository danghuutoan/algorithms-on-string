class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
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
        new_node: Node = Node()
        self.children[label] = new_node
        return new_node

    def get_children(self) -> dict:
        return self.children


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        current_node = self.root
        for c in word:
            if current_node.has_edge(c):
                current_node = current_node.get_child(c)
            else:
                current_node = current_node.add_egde(c)
        current_node.is_end_of_word = True

    def traverse(self, prev_node: Node = None, prev_label: str = None):
        if prev_node is None:
            prev_node = self.root
        for next_label, next_node in prev_node.get_children().items():
            print(f"{prev_label} -> {next_label} ")
            self.traverse(next_node, next_label)


if __name__ == "__main__":
    trie = Trie()
    trie.insert("pa")
    trie.insert("papa")
    trie.insert("papa")
    # trie.insert("cat")
    # trie.insert("chicken")
    # print(trie)
    trie.traverse()
