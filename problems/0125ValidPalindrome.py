# https://leetcode.com/problems/valid-palindrome/
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        p_s = re.sub(r"[^0-9a-zA-Z]", "", s).lower()
        if len(p_s) <= 1:
            return  True

        for i in range(len(p_s) // 2):
            if p_s[i] == p_s[-(i+1)]:
                continue
            else:
                return False
            
        return True