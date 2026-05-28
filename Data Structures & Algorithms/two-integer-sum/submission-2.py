from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(list)
        #for i in range(len(nums)):
            #map[i].append({})
        for i in range(len(nums)):
            num = target - nums[i]
            for element in map[num%len(nums)]:
                (key, value) = list(element.items())[0] 
                if key == num:
                    return [value,i]
            new_key = nums[i] % len(nums)
            map[new_key].append({nums[i]:i})
