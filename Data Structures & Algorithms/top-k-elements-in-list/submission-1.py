from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        #counts frequenccyof element
        bucket = defaultdict(list)
        #{ 1(freq):[1,2],2(freq):}
        for key in freq_dict.keys():
            bucket[freq_dict[key]].append(key)
        result = []
        for freq in range(len(nums), 0, -1):  # len(nums) down to 1
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result

            
                
        