# ---------------- Iterables ---------------- #


def lexicographically_smaller(a, b):
    """
    Check if iterable a is lexicographically smaller than b
    """
    for ai, bi in zip(a, b):
        if ai > bi:
            return False
        if ai < bi:
            return True

    return len(a) <= len(b)


# ---------------- Arrays ---------------- #

def kadanes_algorithm(array):
    """
    Find the maximum sum subarray O(n)
    """
    n = len(array)

    ans = array[0]
    ans_l = ans_r = 0
    sum_ = 0
    last_neg = -1
    
    for r in range(n):
        sum_ += array[r]
        
        if sum_ > ans:
            ans = sum_
            ans_l = last_neg + 1
            ans_r = r
        
        if sum_ < 0:
            sum_ = 0
            last_neg = r

    return ans, ans_l, ans_r

# ---------------- Matrices ---------------- #

def maximum_sum_submatrix(matrix):
    """
    Return the maximum sum submatrix O(n^3)
    """
    
    n, m = len(matrix), len(matrix[0])
    
    ans = float('-inf')
    
    ans_r1 = ans_r2 = ans_c1 = ans_c2 = 0
    
    for l in range(m):
        row_sum = [0] * n
        for r in range(l, m):
            for i in range(n):
                row_sum[i] += matrix[i][r]

            sum_, row_l, row_r = kadanes_algorithm(row_sum)

            if sum_ > ans:
                ans = sum_
                ans_r1, ans_r2, ans_c1, ans_c2 = row_l, row_r, l, r 

    return ans, ans_r1, ans_r2, ans_c1, ans_c2