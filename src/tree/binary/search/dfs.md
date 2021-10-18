# DFS
A stack (explicit or implicit) is required to perform this search

## Pseudocode
<pre class="pseudocode">
function preorder_dfs(Tree t)
    if t != Nil then
        print(t.value)
        preorder_dfs(t.left)
        preorder_dfs(t.right)
</pre>

<pre class="pseudocode">
function inorder_dfs(Tree t)
    if t != Nil then
        inorder_dfs(t.left)
        print(t.value)
        inorder_dfs(t.right)
</pre>

<pre class="pseudocode">
function postorder_dfs(Tree t)
    if t != Nil then
        postorder_dfs(t.left)
        postorder_dfs(t.right)
        print(t.value)
</pre>

## Implementation
### Python
```py
# implementations/dfs.py
```
