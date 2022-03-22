class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        bottom = 0
        upper = len(nums) - 1
        
        # return in boundaries if it is unique number
        if bottom == upper:
            return nums[0]
        if nums[bottom] != nums[bottom+1]:
            return nums[bottom]
        if nums[upper] != nums[upper-1]:
            return nums[upper]
            
        while bottom <= upper:
            middle = bottom + int((upper - bottom) / 2)
            
            if nums[middle] != nums[middle-1] and nums[middle] != nums[middle+1]:
                return nums[middle]
            
            # decide which part to analyze
            if (middle%2 == 0 and nums[middle] == nums[middle+1]) or (middle%2 == 1 and nums[middle] == nums[middle-1]):
                bottom = middle + 1
            else:
                upper = middle - 1
        
        return -1
