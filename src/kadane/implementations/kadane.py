def max_sum_Kadame(values: List[int]) -> int:
    max_so_far = 0
    max_here = 0
    for v in values:
        max_here = max(max_here + v, 0)
        max_so_far = max(max_here, max_so_far)
    return max_so_far
