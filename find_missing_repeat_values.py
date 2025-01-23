def findMissingAndRepeatedValues(grid):
    """
    :type grid: List[List[int]]
    :rtype: List[int]
    https://leetcode.com/problems/find-missing-and-repeated-values/
    Input: grid = [[1,3],[2,2]]
    Output: [2,4]
    Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].
    """
    n = len(grid)
    n2 = n * n

    Se = sum(range(1, n2 + 1))
    Pe = sum(i * i for i in range(1, n2+1))

    Sa = sum(sum(row) for row in grid)
    Pa = sum(num * num for row in grid for num in row)

    # Solve for a and b
    delta = Se - Sa # b - a
    delta_sq = Pe - Pa # b^2 - a^2 

    # (b - a) * (b + a) = delta_sq
    sum_ab = delta_sq // delta

    b = (delta + sum_ab ) // 2
    a = sum_ab - b 

    return [a,b]


print('ANS', findMissingAndRepeatedValues([[1,3],[2,2]])) # [2,4]