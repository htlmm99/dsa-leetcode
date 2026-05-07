class Solution:
    def isPalindrome(self, s: str) -> bool:
        right, left = 0, len(s) -1
        s = s.lower()
        while right < left:
            if not s[right].isalnum():
                right +=1
                continue 
            if not s[left].isalnum():
                left -=1
                continue 
            if s[right] == s[left]:
                right +=1
                left -= 1
                continue 
            else:
                return False 
        return True