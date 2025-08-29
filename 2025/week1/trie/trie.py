#Uses python3
import sys


class Trie:

    def __init__(self, tree = None):
        if tree is None:
            self._nodes = dict()
        else: 
            self._nodes = tree
        # init root node
        self._nodes[0] = dict()

    def create_node(self):
        new_idx = len(self._nodes.items())
        self._nodes[new_idx] = dict()
        return new_idx

    def get_node(self, node_id):
        return self._nodes[node_id]
    
    def create_edge(self, from_id, to_id, label):
        self._nodes[from_id][label] = to_id
    
    def to_dict(self):
        return self._nodes
    
    def insert(self, text: str):
        idx = 0
        for c in text:
            current_node = self.get_node(idx)
            # if there is a node with label c from current node
            if c in current_node:
                idx = current_node[c]
            else:
                new_idx = self.create_node()
                self.create_edge(from_id=idx, to_id=new_idx, label=c)
                idx = new_idx

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    # write your code here
    trie = Trie(tree=tree)
    tree[0] = {}
    for pattern in patterns:
        trie.insert(pattern)
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
