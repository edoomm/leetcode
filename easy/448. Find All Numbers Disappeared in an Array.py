class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        r = len(nums)
        res = []
        s = set()
        
        print(r)
        
        for n in nums:
            s.add(n)
        
        for i in range(1, r+1):
            if i not in s:
                res.append(i)
                
        return res
