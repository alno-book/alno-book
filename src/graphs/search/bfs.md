# BFS
The Breadth-first search (BFS) algorithm has the aim to visit at increasing distance from the starting point.
It visits nodes with distance \\(k\\) before nodes at distance \\(k+1\\).

It can be used to calculate the fastest path to each node, in case edges have either no cost or the same one.

Time complexity: \\(O(m+n)\\)

Space complexity: \\(O(n)\\)

## Pseudocode
<pre class="pseudocode">
function bfs(Graph G, Node r)
    Queue Q = Queue()
    S.enqueue(r)
    boolean[] visited = new boolean[G.size()]
    foreach u \(\in\) G.V() - {r} do
        visited[u] = false
    
    visited[r] = true
    
    while not Q.isEmpty() do
        Node u = Q.dequeue()
        // visit node u
        foreach v \(\in\) G.adj(u) do
            // visit edge (u, v)
            if not visited[v] then
                visited[v] = true
                Q.enqueue(v)
</pre>


## Complexity
Time complexity: \\(O(m+n)\\), because you will visit each node and edge at most one single time.

Space complexity: \\(O(n)\\), since you may have at most \\(n\\) nodes in the queue. A more strict limit would be \\(O(w)\\), where \\(w\\) represents the width of the graph.

## Implementation
### Python
```py
# implementations/bfs.py
```
