# python3
import sys


class Node:
    def __init__(self, start: int, length: int) -> None:
        self.start = start
        self.length = length
        self.children = {}

    def addChild(self, key: str, start: int, length: int):
        new_node = Node(start=start, length=length)
        self.chidren[key] = new_node
        return new_node

    def getChild(self, ch: str):
        return self.chidren[ch]

    def hasChild(self, ch: str):
        return ch in self.chidren


class SuffixTree:
    def __init__(self, text=None) -> None:
        self.root = Node(0, 0)
        # self.nodes = dict()
        # self.latest_id = 0
        self.text = text
        self.text_length = len(text)

    def insert(self, offset: int):
        current = self.root

        while True:
            if not current.hasChild(self.text[offset]):
                current = current.addChild(0, self.text_length - offset)
            else:
                if len(self.text) > current.length:
                    pass
                elif self.text_length - offset < current.length:
                    for i in range(current.length):
                        if (
                            self.text[offset + i]
                            != self.text[current.start + i + offset]
                        ):
                            current.addChild(
                                current.start + i + offset, current.length - i
                            )
                            current.length = i
                            current.addChild(offset + i, self.text_length - i)
                else:
                    pass

    def build(self):
        for i in range(len(self.text)):
            self.insert(i)

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

            if current.hasChild("$") is True:
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


def build_suffix_tree(text):
    """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding
  substrings of the text) in any order.
  """
    result = []
    # Implement this function yourself
    return result


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))

