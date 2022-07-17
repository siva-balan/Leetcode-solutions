class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        reverse = 0
        temp = x
        
        while x > 0:
            reverse = reverse * 10 + x % 10
            x = x // 10
            
        if(reverse == temp):
            return True
        else: return False
