class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = [0]*26
        for i in range(len(s)):
            anagram[ord(s[i])-ord('a')]+=1
        for i in range(len(t)):
            anagram[ord(t[i])-ord('a')]-=1
        for i in range(26):
            if anagram[i]!=0:
                return False
        return True