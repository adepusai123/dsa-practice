def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    n ^ n = 0 [Bit wise operation helps here]
    n ^ 0 = n
    https://leetcode.com/problems/single-number/
    Input: nums = [4,1,2,1,2]
    Output: 4
    """
    ans = 0
    for i in nums:
        ans = ans ^ i
    return ans

print(singleNumber([4,1,2,1,2])) # 4