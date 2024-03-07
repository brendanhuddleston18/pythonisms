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
def test_list_comprehension():
    linked_list = LinkedList(("node1", "node2", "node3"))

    capital_nodes = [node.upper() for node in linked_list]

    assert capital_nodes == ["NODE1", "NODE2", "NODE3"]

# @pytest.mark.skip("TODO")
def test_conversion():
    reg_list = ["node1", "node2", "node3"]
    linked_list = LinkedList(("node1", "node2", "node3"))
    print([node for node in linked_list])
    assert list(linked_list) == reg_list

def test_equality():
    linked_list_one = LinkedList(("node1", "node2", "node3"))
    linked_list_two = LinkedList(("node1", "node2", "node3"))
    assert linked_list_one == linked_list_two

# @pytest.mark.skip("TODO")
def test_string():
    linked_list = LinkedList(("node1", "node2", "node3"))

    actual = str(linked_list)
    expected = "[ node1 ] -> [ node2 ] -> [ node3 ] -> None"
    assert actual == expected