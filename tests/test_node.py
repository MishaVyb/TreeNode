import pytest
from node import BNode

import logging
logger = logging.getLogger(__file__)


@pytest.mark.parametrize(
    'tree',
    [
        pytest.param(
            [
                # fmt: off
                [0],
                [100, 200],
                [110, 120], [210, 220],
                # fmt: on
            ],
            id='01 - simple binary tree test',
        ),
        pytest.param(
            [
                # fmt: off
                [0],
                [100, 200],
                [110, 120], [210, 220],
                [None, 112], [], [], [None, 222],
                [333, 444], [None, 555],
                [], [], [12345],
                # fmt: on
            ],
            id='02 - binary tree test',
        ),
    ],
)
def test_bnode_tree_creation(tree: list[list[int]]):
    pytest.skip('Not implemented yet.')


def test_bnode_breadth_traversal(root: BNode):
    logger.info(root)
    logger.info(list(root.breadth_traversal()))


def test_bnode_depth_traversal(root: BNode):
    logger.info(root)
    logger.info('--- pre_order ---')
    logger.info(list(root.depth_traversal('pre_order')))
    logger.info('--- in_order ---')
    logger.info(list(root.depth_traversal('in_order')))
    logger.info('--- post_order ---')
    logger.info(list(root.depth_traversal('post_order')))




