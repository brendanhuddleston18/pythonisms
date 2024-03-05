import pytest
from pythonisms import LinkedList

# @pytest.mark.skip("TODO")
def test_instantiate():
    assert LinkedList()

# @pytest.mark.skip("TODO")
def test_insert():
    linked_list = LinkedList()
    linked_list.insert("bobby")
    actual = linked_list.head.value
    expected = "bobby"
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_iteration():
    linked_list = LinkedList(("node1", "node2", "node3"))

    nodes_list = []

    for node in linked_list:
        nodes_list.append(node)
    
    assert nodes_list

# @pytest.mark.skip("TODO")
def test_string():
    linked_list = LinkedList(("node1", "node2", "node3"))

    actual = str(linked_list)
    expected = "[ node1 ] -> [ node2 ] -> [ node3 ] -> None"
    assert actual == expected