# DFS
The Depth-first search (DFS) algorithm has the aim to visit at increasing distance from the starting point.
It visits nodes with distance \\(k\\) before nodes at distance \\(k+1\\).

It can be used to calculate the fastest path to each node, in case edges have either no cost or the same one.

Time complexity: \\(O(m+n)\\)

Space complexity: \\(O(n)\\)

## Pseudocode
There are two possibilities for implementing the DFS algorithm:
- by an explicit stack;
- by an implicit stack, obtained by function calls. It is quite risky in big graphs, since the stack depth is fixed.


### Explicit stack
<pre class="pseudocode">
function dfs(Graph G, Node r)
    Stack S = Stack()
    S.push(r)
    boolean[] visited = new boolean[G.size()]

    foreach u \(\in\) G.V() do
        visited[u] = false

    while not S.isEmpty() do
        Node u = S.pop()
        if not visited[u] then
            // pre-order visit of node u
            visited[u] = true
            foreach v \(\in\) G.adj(u) do
                // visit the edge (u, v)
                S.push(v)
</pre>

### Implicit stack
<pre class="pseudocode">
function dfs(Graph G, Node r, boolean[] visited)
    visited[u] = true
    // pre-order visit of node u

    foreach v \(\in\) G.adj(u) do
        if not visited[v] then
        // visit the edge (u, v)
        dfs(G, v, visited)

    // post-order visit of node u
</pre>


## Complexity
Time complexity: \\(O(m+n)\\), you can insert more than one time a node in the stack, but you can insert a maximum of \\(m\\) times. The single node visit costs \\(O(n)\\).

Space complexity: \\(O(n)\\), since you may have at most \\(n\\) nodes in the stack.

## Implementation
### Python
```py
# implementations/dfs.py
```
