import pytest
from week1.problem1.new_solution import TrieNode

def test_add_child():
    node = TrieNode()
    node.add_child('a')
    assert 'a' in node.children
    assert isinstance(node.get_child('a'), TrieNode)
    assert node.get_child('a').value is None

def test_add_child_with_value():
    node = TrieNode()
    child = node.add_child('a', value='test_value')
    assert node.get_child('a').value == 'test_value'
    assert child.value == 'test_value'

def test_get_child():
    node = TrieNode()
    node.add_child('a')
    assert isinstance(node.get_child('a'), TrieNode)
    assert node.get_child('a') is not None
    assert node.get_child('b') is None

def test_get_child_empty_node():
    node = TrieNode()
    assert node.get_child('a') is None
    assert node.get_child('b') is None

def test_has_child():
    node = TrieNode()
    node.add_child('a')
    assert node.has_child('a') is True
    assert node.has_child('b') is False

def test_has_child_empty_node():
    node = TrieNode()
    assert node.has_child('a') is False
    assert node.has_child('b') is False

def test_repr():
    node = TrieNode()
    assert repr(node) == "TrieNode(children=[], value=None)"
    node.add_child('a')
    assert repr(node) == "TrieNode(children=['a'], value=None)"
    node.add_child('b', value='end')
    assert repr(node) == "TrieNode(children=['a', 'b'], value=None)"
    assert repr(node.get_child('b')) == "TrieNode(children=[], value=end)"
