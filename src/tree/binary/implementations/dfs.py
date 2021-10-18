from .tree import Tree


def preorder_dfs(t: Tree):
    if not t is None:
        print(t.value)
        preorder_dfs(t.left)
        preorder_dfs(t.right)


def inorder_dfs(t: Tree):
    if not t is None:
        inorder_dfs(t.left)
        print(t.value)
        inorder_dfs(t.right)


def postorder_dfs(t: Tree):
    if not t is None:
        postorder_dfs(t.left)
        postorder_dfs(t.right)
        print(t.value)
