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
        # queue = deque()

        stack.append(curr_node)
        # queue.append(curr_node)
        
        while len(stack) >0:
            curr = stack.pop()
            if curr.is_end_of_word is True:
                offset.add(curr.offset)
    
            for _,next_node in curr.get_children().items():
                stack.append(next_node)
                # queue.append(next_node)
        return offset
    
    def compact(self):
        curr_node = self.root

        stack = []

        stack.append(curr_node)

        while len(stack) >0:
            curr = stack.pop()
            if curr.is_end_of_word is True:
              print("end")
            
            for _, next_node in curr.get_children().items():
                stack.append(next_node)


    def match(self, pattern: str):

        curr_node = self.root
        for c in pattern:
            if curr_node.has_edge(c):
                curr_node = curr_node.get_child(c)
            else:
                return []
        offset = self.walkdown(curr_node)
        return offset
    
    def suffix_match(self, suffix: str):
        
        curr_node = self.root

        
        for c in suffix:
            if curr_node.is_end_of_word:
                return True

            if curr_node.has_edge(c) is False:
                return False

            curr_node = curr_node.get_child(c)

        if curr_node.is_end_of_word:
            return True
        
        return False

def build_suffix_tree(text):
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding 
  substrings of the text) in any order.
  """
  result = []
  trie = Trie()
  for i in range(len(text)):
      print(text[i:])
      trie.insert(text[i:])
  # Implement this function yourself
  print(trie)
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))