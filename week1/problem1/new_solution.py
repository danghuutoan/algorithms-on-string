class TrieNode:
    def __init__(self, value: None = None):
        self.edges: dict = {}
        self.value: None = value

    def __repr__(self) -> str:
        return f"TrieNode(edges={list(self.edges.keys())}, value={self.value})"

    def add_edge(self, key: str, value: None = None) -> "TrieNode":
        if key not in self.edges:
            self.edges[key] = TrieNode(value)
        return self.edges[key]

    def get_edge(self, key: str) -> "TrieNode":
        return self.edges.get(key)

    def has_edge(self, key: str) -> bool:
        return key in self.edges


class Trie:
    def __init__(self) -> "Trie":
        self.root = TrieNode()
        self.latest_id = 0
        self.nodes = {}

    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            if not current.has_edge(ch):
                new_node = current.add_edge(ch, self.latest_id + 1)
                self.latest_id += 1
                self.update_nodes(current, new_node)
            current = current.get_edge(ch)

    def update_nodes(self, current_node: TrieNode, new_node: TrieNode) -> None:
        if current_node not in self.nodes:
            self.nodes[current_node] = {}
        self.nodes[current_node][new_node.value] = new_node
