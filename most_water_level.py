def maxArea(nums):
    """
    :type height: List[int]
    :rtype: int
    https://leetcode.com/problems/container-with-most-water/
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
    """
    lp, rp, ans = 0, len(nums) - 1, 0

    while lp < rp:
        width = rp - lp
        height = min(nums[lp], nums[rp])
        curr_water = width * height
        ans = max(ans, curr_water)
        if nums[lp] < nums[rp]:
            lp += 1
        else:
            rp -= 1

    return ans


print('Ans: ', maxArea([1,8,6,2,5,4,8,3,7])) # 49