class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for i in range(len(s)):
            if s[i].isalnum():
               s_new+=s[i]
        s_new = s_new.lower()
        i = 0
        j = len(s_new) - 1
        while i<j:
            if s_new[i]!=s_new[j]:
                return False
            i+=1
            j-=1
        return True