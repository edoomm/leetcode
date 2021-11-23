def getfirstposindex(arr: int) -> int:
    for i in range(len(arr)):
        if arr[i] >= 0:
            return i
    return -1

def getfirstnegindex(arr: int) -> int:
    for i in range(len(arr)):
        if arr[i] <= 0:
            return i
    return -1


def getfourthcases(nums: List[int], keys, limit: int, case: str) -> List[int]:
    '''
    case: 'p' for positive, 'n' for negative
    '''
    i = 0
    j = 1
    n = len(nums) - 1
    res = []
    
    while i <= limit-1 and n > limit:
        if abs(nums[i]) >= abs(nums[n]):
            i += 1
            j = i+1
            continue
        if abs(nums[i] + nums[j]) > abs(nums[n]):
            n -= 1
            continue

        if case == 'n' and abs(nums[i] + nums[j]) in keys:
            res.append([nums[i], nums[j], abs(nums[i] + nums[j])])
        elif (nums[i] + nums[j])*-1 in keys:
            res.append([(nums[i] + nums[j])*-1, nums[j], nums[i]])

        j += 1
        if j > limit:
            i += 1
            j = i+1
    
    return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        d = {}
        
        for n in nums:
            if n not in d.keys():
                d[n] = 1
            else:
                d[n] += 1
        
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
        
        print(nums)
        print(nums[::-1])
        
        res += getfourthcases(nums, d.keys(), getfirstposindex(nums) - 1, 'n')
        res += getfourthcases(nums[::-1], d.keys(), getfirstnegindex(nums[::-1]) - 1, 'p')
    
        # Removing duplicates
        resdict = {}
        for i in range(len(res)):
            if res[i] not in resdict.values():
                resdict[i] = res[i]
        
        return resdict.values()
