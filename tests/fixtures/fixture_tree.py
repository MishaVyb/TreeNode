import pytest
from node import BNode

def bnode1():
    "binary tree: 1 depth | 1 node"
    return BNode(0)

def bnode2():
    "binary tree: 2 depth | 3 nodes"
    node2 = BNode(22)
    node1 = BNode(11)
    root = BNode(0, node1, node2)
    return root

def bnode3():
    "bnode3: binary tree: 3 depth | 5 nodes"
    """
             (0)
       (11)       (22)
    (33) (44)  None  None
    """
    node4 = BNode(44)
    node3 = BNode(33)
    node2 = BNode(22)
    node1 = BNode(11, node3, node4)
    root = BNode(0, node1, node2)
    return root

def bnode4():
    "bnode4: binary tree: 3 depth | 5 nodes"
    """
             (0)
       (11)       (22)
    (33) None  (44)  None
    """
    node4 = BNode(44)
    node3 = BNode(33)
    node2 = BNode(22, node4)
    node1 = BNode(11, node3)
    root = BNode(0, node1, node2)
    return root



@pytest.fixture(
    params=[
        pytest.param(bnode1, id=bnode1.__doc__),
        pytest.param(bnode2, id=bnode2.__doc__),
        pytest.param(bnode3, id=bnode3.__doc__),
        pytest.param(bnode4, id=bnode4.__doc__),
    ]
)
def root(request: pytest.FixtureRequest) -> BNode[int]:
    return request.param()
