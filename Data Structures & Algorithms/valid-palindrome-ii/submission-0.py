class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_valid_pal_range(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1; right -= 1
            return True

        left, right = 0, len(s) -1
        while left < right:
            if s[left] != s[right]:
                return is_valid_pal_range(left+1, right) or is_valid_pal_range(left, right-1)
            left += 1; right -= 1
        return True
        