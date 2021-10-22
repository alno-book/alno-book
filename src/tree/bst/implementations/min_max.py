from binary_search_tree import BinarySearchTree


def min(tree: BinarySearchTree):
    u = tree
    if u is None:
        return u
    while u.left is not None:
        u = u.left
    return u


def max(tree: BinarySearchTree):
    u = tree
    if u is None:
        return u
    while u.right is not None:
        u = u.right
    return u
