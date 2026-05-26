class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        flag  = 0
        for i in range(len(nums)):
            dup[nums[i]] = 0
        for i in range(len(nums)):
            dup[nums[i]] += 1
            if(dup[nums[i]]>=2):
                flag = 1
                break
        return flag == 1