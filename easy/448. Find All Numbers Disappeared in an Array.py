class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0 for i in range(length)]
        
        for n in nums:
            res[n-1] = -1
                
        for i in range(length):
            if res[i] != -1:
                res[i] = i+1
        
        i = 0
        while i < len(res):
            if res[i] == -1:
                del res[i]
            else:
                i += 1
        
        return res
