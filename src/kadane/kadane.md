# Kadane
*Kadane* algorithm finds the maximum sum of contiguous elements inside an array.

- **input** → an array of numbers;
- **output** → a number corresponding the maximum sum;
- **complexity** → \\(\Theta(n)\\).

## Pseudocode
<pre class="pseudocode">
function max_sum_Kadane(values)
    max_so_far = 0
    max_here = 0
    for value in values
        max_here = max (max_here + value, 0)
        max_so_far = max (max_here, max_so_far)
    return max_so_far
</pre>

## Explanation
These two first variables are used to mantain:

- the maximum sum during the values array iteration;
- the max value obtained until a specific position of the iteration.
<pre class="pseudocode">
max_so_far = 0
max_here = 0
</pre>

The `for` loop that follows initializations iterates over the input array of values computing to maximum function. 
<pre class="pseudocode">
for value in values
    max_here = max (max_here + value, 0)
    max_so_far = max (max_here, max_so_far)
</pre>

## Complexity
With \\(n\\) the number of elements inside the input array:
$$
\Theta(n)
$$
The *Kadane* algorithm always iterate on all values of the input arrays.


## Implementations
### Python
```py
# implementations/kadane.py
```

### Rust
```rust
// implementations/kadane.rs
```

##### Input
```
[1, 2, -5, 10, 8]
```

##### Output
```
18
```
