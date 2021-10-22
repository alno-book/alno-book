# Min/Max

Given a Binary Search Tree *T*, *min* (or *max*) returns the node with the lowest (or highest) *key*.

Time complexity: \\(O(n)\\)

## Pseudocode

<pre class="pseudocode">
function min(BinarySearchTree T)
    BinarySearchTree u = T
    if u == Nil then
        return u
    while u.left != Nil then do
        u = u.left
    return u
</pre>