from typing import Union
from binary_search_tree import BinarySearchTree


def insert(tree: BinarySearchTree, key: Union[int, float], value: Union[int, float]):
    t = tree
    parent = t
    while t is not None and t.key != key:
        parent = t
        if key < t.key:
            t = t.left
        else:
            t = t.right

    if t is not None:
        t.value = value
    else:
        new_tree = BinarySearchTree(key, value)
        link(parent, new_tree, key)


def link(top: BinarySearchTree, bottom: BinarySearchTree, key: Union[int, float]):
    if key < top.key:
        top.left = bottom
    else:
        top.right = bottom

    if bottom is not None:
        bottom.parent = top
