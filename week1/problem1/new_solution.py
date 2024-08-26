class TrieNode:
    def __init__(self, value: None = None):
        self.children: dict = {}
        self.value: None = value

    def __repr__(self) -> str:
        return f"TrieNode(children={list(self.children.keys())}, value={self.value})"

    def add_child(self, key: str, value: None = None) -> 'TrieNode':
        if key not in self.children:
            self.children[key] = TrieNode(value)
        return self.children[key]

    def get_child(self, key: str) -> 'TrieNode':
        return self.children.get(key)

    def has_child(self, key: str) -> bool:
        return key in self.children
