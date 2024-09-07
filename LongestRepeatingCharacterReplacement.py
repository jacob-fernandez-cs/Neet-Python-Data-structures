class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #hashmap to count the occurences of character
        result = 0
        l = 0
        # r - l + 1 is the length of the window (right pointer - left pointer + 1)

        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],  0)
            while(r - l + 1) - max(count.values()) > k:
                 #while the size of the window minus the character with the highest value is greater than K (not a valid window)
                 #decrease the value of the char at the left position and move the left pointer forward 1
                 count[s[l]] -= 1
                 l += 1

             

            result = max(result, r - l + 1)
        return result

s = "AABABBA"
k = 1
Solution = Solution()
print(Solution.characterReplacement(s,k))