# Erdos
This is an application of the BFS algorithm. It consists of calculating the distance, measured in the number of edges, between the starting point and each other node in the graph.

Time complexity: \\(O(m+n)\\)

Space complexity: \\(O(n)\\)

## Pseudocode
<pre class="pseudocode">
function bfs(Graph G, Node r, int[] erdos, Node[] parent)
    Queue Q = Queue()
    S.enqueue(r)
    foreach u \(\in\) G.V() - {r} do
        erods[u] = \(\infty\)
    
    erods[r] = 0
    parent[r] = Nil
    
    while not Q.isEmpty() do
        Node u = Q.dequeue()
        foreach v \(\in\) G.adj(u) do
            if erods[v] == \(\infty\) then
                erods[v] = erods[u] + 1
                parent[v] = u
                Q.enqueue(v)
</pre>


## Complexity
Time complexity: \\(O(m+n)\\), as BFS.

Space complexity: \\(O(n)\\), since all the data structures contain \\(n\\) elements.

## Implementation
### Python
```py
# implementations/erdos.py
```
