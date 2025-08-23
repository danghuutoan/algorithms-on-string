import pytest
from week1.problem1.new_solution import TrieNode

def test_add_edge():
    node = TrieNode()
    node.add_edge('a')
    assert 'a' in node.edges
    assert isinstance(node.get_edge('a'), TrieNode)
    assert node.get_edge('a').value is None

def test_add_edge_with_value():
    node = TrieNode()
    child = node.add_edge('a', value='test_value')
    assert node.get_edge('a').value == 'test_value'
    assert child.value == 'test_value'

def test_get_edge():
    node = TrieNode()
    node.add_edge('a')
    assert isinstance(node.get_edge('a'), TrieNode)
    assert node.get_edge('a') is not None
    assert node.get_edge('b') is None

def test_get_edge_empty_node():
    node = TrieNode()
    assert node.get_edge('a') is None
    assert node.get_edge('b') is None

def test_has_edge():
    node = TrieNode()
    node.add_edge('a')
    assert node.has_edge('a') is True
    assert node.has_edge('b') is False

def test_has_edge_empty_node():
    node = TrieNode()
    assert node.has_edge('a') is False
    assert node.has_edge('b') is False

def test_repr():
    node = TrieNode()
    assert repr(node) == "TrieNode(edges=[], value=None)"
    node.add_edge('a')
    assert repr(node) == "TrieNode(edges=['a'], value=None)"
    node.add_edge('b', value='end')
    assert repr(node) == "TrieNode(edges=['a', 'b'], value=None)"
    assert repr(node.get_edge('b')) == "TrieNode(edges=[], value=end)"