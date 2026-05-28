class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def detect_anagram(s:str,t:str):
            if len(s) != len(t):     
                return False
            anagram = [0]*26
            for i in range(len(s)):
                anagram[ord(s[i])-ord('a')]+=1
            for i in range(len(t)):
                anagram[ord(t[i])-ord('a')]-=1
            return anagram == [0]*26
        grouping = []
        detect_list= [False]*len(strs)
        #to check if it is already included in a list
        for i in range(len(strs)):
            anagrams = []
            if detect_list[i] == False:
                anagrams.append(strs[i])
                for j in range(i+1,len(strs)):
                    if detect_list[j] == False:
                        if detect_anagram(strs[i],strs[j]):
                            anagrams.append(strs[j])
                            detect_list[j] = True
                grouping.append(anagrams)
            else: 
                pass
            detect_list[i]=True
        return grouping
