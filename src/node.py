from __future__ import annotations
from typing import Any, Generator, Generic, Literal, TypeVar, overload

import logging

logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__file__)

_T = TypeVar('_T')
_NT = TypeVar('_NT')


class NotProvidedType:
    ...


NOT_PROVIDED = NotProvidedType()


class Node(Generic[_T]):
    def __init__(self, value: _T, children: list[Node[_T] | None] = []):
        self.value = value
        self.children = children or []


class BNode(Node[_T]):
    def __init__(
        self,
        value: _T,
        left: BNode[_T] | None = None,
        right: BNode[_T] | None = None,
    ):
        super().__init__(value, [left, right])

    @property
    def left(self):
        return self.children[0]

    @left.setter
    def left(self, node: BNode[_T] | None):
        self.children[0] = node

    @left.deleter
    def left(self):
        self.children[0] = None

    @property
    def right(self):
        return self.children[1]

    @right.setter
    def right(self, node: BNode[_T] | None):
        self.children[1] = node

    @right.deleter
    def right(self):
        self.children[1] = None

    # fmt: off
    @overload
    def get_level_values(root, level: int) -> list[_T]: ...
    @overload
    def get_level_values(root, level: int, empty: _NT) -> list[_T | _NT]: ...
    # fmt: on
    def get_level_values(
        root, level: int, empty: _NT | NotProvidedType = NOT_PROVIDED
    ) -> list[_T | _NT]:
        if not root:
            if isinstance(empty, NotProvidedType):
                return []
            return [empty]
        if level == 0:
            return [root.value]

        level -= 1
        if isinstance(empty, NotProvidedType):
            left = BNode.get_level_values(root.left, level)
            right = BNode.get_level_values(root.right, level)
            return left + right
        left = BNode.get_level_values(root.left, level, empty)
        right = BNode.get_level_values(root.right, level, empty)
        return left + right


    def breadth_traversal(root) -> Generator[_T, None, None]:
        """
        Level Order Binary Tree Traversal (BFS).
        """
        level = 0
        while True:
            values = root.get_level_values(level)
            if not values:
                return
            yield from values
            level += 1

    def breadth_traversal_by_levels(root) -> Generator[list[_T | None], None, None]:
        """
        The same as `breadth_traversal` but yield level values nested in lists.
        And replace empty nodes with `None`.
        """
        level = 0
        while True:
            values = root.get_level_values(level, None)
            if set(values) == {None}:
                return
            yield values
            level += 1

    def depth_traversal(
        root, kind: Literal['pre_order', 'in_order', 'post_order']
    ) -> Generator[_T, None, None]:
        """
        Deapth First Traversal (DFS).
        """
        if not root:
            return

        if kind == 'pre_order':
            yield root.value
            yield from BNode.depth_traversal(root.left, kind)
            yield from BNode.depth_traversal(root.right, kind)
        elif kind == 'in_order':
            yield from BNode.depth_traversal(root.left, kind)
            yield root.value
            yield from BNode.depth_traversal(root.right, kind)
        if kind == 'post_order':
            yield from BNode.depth_traversal(root.left, kind)
            yield from BNode.depth_traversal(root.right, kind)
            yield root.value

    def __str__(self) -> str:
        str = ''
        for level in self.breadth_traversal_by_levels():
            str += '\n' + ' '.join([f'<{value}>' for value in level])
        return str

    @classmethod
    def maketree(cls, tree: list[list[_T]]):
       ...
