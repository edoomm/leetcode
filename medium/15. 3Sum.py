def getfirstposindex(arr: int) -> int:
    n = float('-inf')
    for i in range(len(arr)):
        n = arr[i]
        if n == 0:
            return i
    return -1

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        d = {}
        
        for n in nums:
            if n not in d.keys():
                d[n] = 1
            else:
                d[n] += 1
        
        # Three cases
        '''
            1. 2*n - m = 0, where n = nums[i] = nums[j] & m = nums[k]
            2. n + m|=0 + n = 0, , where n = nums[i] = -nums[j] & m = nums[k] = 0
            3. n + n + n = 0, where n = nums[i] = nums[j] = nums[k] = 0
            4. n + m + o = 0
                4.1 where n,m < 0; o > 0
                4.2 where n < 0; m,o >0
        '''
        for k in d.keys():
            # First case
            if d[k] >= 2 and k != 0:
                if -k*2 in d.keys():
                    res.append([k, k, -k*2])
            # Second case
            if -k in d.keys() and k != 0: # d[k] == 1
                if 0 in d.keys():
                    first = k if k < -k else -k
                    second = -first
                    res.append([first, 0, second])
        
        # Third case
        if 0 in d.keys():
            if d[0] >= 3:
                res.append([0, 0, 0])
        
        # Fourth case
        nums.sort()
        # removing duplicates of original array
        i = 0
        while i < len(nums):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        # Fourth case (1)
        i = 0
        j = 1
        n = len(nums) - 1
        limit = getfirstposindex(nums) - 1
        print(nums, limit)
        while True:
            print(nums[i])
            if nums[i] <= -nums[n]:
                i += 1
                j = i + 1
            elif nums[i] + nums[j] < -nums[n]:
                n -= 1
            else:
                if -(nums[i] + nums[j]) in d.keys():
                    res.append([nums[i], nums[j], -(nums[i] + nums[j])])
                else:
                    j += 1
            
            if j >= limit+1:
                i += 1
                j += 1
                n -= 1
            
            if i > limit - 1:
                break
        
        # Removing duplicates
        resdict = {}
        for i in range(len(res)):
            if res[i] not in resdict.values():
                resdict[i] = res[i]
        
        return resdict.values()
