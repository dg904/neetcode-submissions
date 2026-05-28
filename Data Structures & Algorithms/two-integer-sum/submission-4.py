''' Creating hash table like this 
            {
            1(hash value):[{key(nums[i]):value(index in nums)},{},{}]
            2:[{},{},{}]
            3:[{},{},{}]
            ...
            ...
            }
'''
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(list)
        #creating a dict where values are list
        for i in range(len(nums)):
            num = target - nums[i]
            #searching for num in dict
            for element in map[num%len(nums)]:
                (key, value) = list(element.items())[0] 
                if key == num:
                    return [value,i]
            map[nums[i] % len(nums)].append({nums[i]:i})
           