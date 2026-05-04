class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(' ', '')
        left = 0
        right = len(s)-1
        isPalindrome = True
        while left < right:
            if s[left].isalnum() ==False:
                left+=1
            if s[right].isalnum() == False:
                right -=1
            if s[left] != s[right] and left<right:
                isPalindrome = False
            left+=1
            right-=1
        
        return isPalindrome
