import pytest
from week1.problem1.new_solution import Trie, TrieNode

@pytest.fixture
def trie():
    return Trie()

def test_insert_single_word(trie):
    trie.insert("ATAGA")
    assert len(trie.nodes) == 5
    assert trie.root.has_edge('A')
    assert trie.root.get_edge('A').has_edge('T')
    assert trie.root.get_edge('A').get_edge('T').has_edge('A')
    assert trie.root.get_edge('A').get_edge('T').get_edge('A').has_edge('G')
    assert trie.root.get_edge('A').get_edge('T').get_edge('A').get_edge('G').has_edge('A')
    print("Trie after inserting 'ATAGA':")
    # trie.print_trie()

def test_insert_multiple_words(trie):
    trie.insert("ATAGA")
    trie.insert("ATC")
    trie.insert("GAT")
    
    # Visual representation of the trie after inserting "ATAGA", "ATC", and "GAT":
    #
    # Root
    # ├── A
    # │   └── T
    # │       ├── A
    # │       │   └── G
    # │       │       └── A
    # │       └── C
    # └── G
    #     └── A
    #         └── T
    
    # Check that the total number of nodes is as expected
    assert len(trie.nodes) == 9
    
    # Verify the structure of the trie
    # Check that the root has edges 'A' and 'G'
    assert trie.root.has_edge('A')
    assert trie.root.has_edge('G')
    
    # Check the structure under the 'A' edge
    assert trie.root.get_edge('A').has_edge('T')
    assert trie.root.get_edge('A').get_edge('T').has_edge('A')
    assert trie.root.get_edge('A').get_edge('T').has_edge('C')
    
    # Check the structure under the 'G' edge
    assert trie.root.get_edge('G').has_edge('A')
    assert trie.root.get_edge('G').get_edge('A').has_edge('T')
    print("Trie after inserting 'ATAGA', 'ATC', and 'GAT':")
    trie.print_trie()

def test_update_node_dict(trie):
    trie.insert("ATAGA")
    assert trie.root in trie.nodes
    assert 1 in trie.nodes[trie.root]
    assert trie.nodes[trie.root][1].value == 1