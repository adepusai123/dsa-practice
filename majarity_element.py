def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    https://leetcode.com/problems/majority-element/description/
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
    """
    count, ans = 0, None
    for num in nums:
        if count == 0:
            ans = num
        count += (1 if num == ans else -1)

    count = 0
    for num in nums:
        if num == ans:
            count += 1
    if count > len(nums) // 2:
        return ans
    return None


print('Ans: ', majorityElement([2,2,1,1,1,2,2]))