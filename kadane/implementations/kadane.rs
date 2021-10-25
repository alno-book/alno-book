use std::cmp::max;

fn max_sum_Kadane(values: Vec<i32>) -> i32 {
    let mut max_so_far = 0;
    let mut max_here = 0;
    for &i in values.iter() {
        max_here = max(max_here + i, 0);
        max_so_far = max(max_here, max_so_far);
    }
    max_so_far
}
