class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        https://leetcode.com/problems/sort-colors/
        DNF Sorting Algorithm
        Input: nums = [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]
        """
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low +=1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid],nums[high]
                high -= 1

        return nums
        
print(Solution().sortColors([2,0,2,1,1,0])) # [0,0,1,1,2,2]