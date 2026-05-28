from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = defaultdict(list)
        def freq_tuple(s:str):
            anagram = [0]*26
            for i in range(len(s)):
                anagram[ord(s[i])-ord('a')]+=1
            return tuple(anagram)
        for i in range(len(strs)):
            grouping[freq_tuple(strs[i])].append(strs[i])
        return [grouping[key] for key in grouping.keys()]
        
